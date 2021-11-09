from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from sugarpy.mixins import InjectUrlDataMixin
from user_details.models import UserDetail as UserDetailModel
from user_details.serializers import UserDetailSerializer, UserSerializer, RegisterUserSerializer
from user_details.permissions import IsAdminOrCurrentUser

class LoginStatus(APIView):
  def get(self, request):
    if self.request.user.is_anonymous:
      return Response(False)
    else:
      return Response(True)

class Logout(APIView):
  def post(self, request):
    return self.delete_auth_token(request)

  def delete_auth_token(self, request):
    request.user.auth_token.delete()
    return Response('User logged out successfully')

class ChangePassword(APIView):
  def post(self, request):
    return self.update_password(request)

  def update_password(self, request):
    password = request.data['password']
    request.user.set_password(password)
    request.user.save()
    return Response('Password updated')

class NewUser(generics.ListCreateAPIView):
  def get_queryset(self):
    if self.request.user.is_staff == True:
      return User.objects.all()
    elif not self.request.user.is_anonymous:
      auth_token = self.request.user.auth_token
      return User.objects.filter(user_id=user_id)
    else:
      return
  serializer_class = RegisterUserSerializer
  permissions_classes = (
    IsAdminOrCurrentUser
  )

  @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
  def perform_create(self, serializer):
    serializer.save()

class CheckUsernameAvailability(APIView, InjectUrlDataMixin):
  def get(self, request, *args, **kwargs):
    username = self.kwargs['username']
    user = User.objects.filter(username=username)
    if len(user) > 0:
      return Response(False)
    else:
      return Response(True)

class UserList(generics.ListCreateAPIView):
  def get_queryset(self):
    if self.request.user.is_staff == True:
      return User.objects.all()
    elif not self.request.user.is_anonymous:
      id = self.request.user.id
      return User.objects.filter(id=id)
    else:
      return
  serializer_class = UserSerializer
  permissions_classes = (
    IsAdminOrCurrentUser
  )

  @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
  def perform_create(self, serializer):
    serializer.save()

class UserSelfDetail(generics.ListCreateAPIView):
  def get_queryset(self):
    if self.request.user.is_staff == True:
      return User.objects.filter(id=id)
    elif not self.request.user.is_anonymous:
      id = self.request.user.id
      return User.objects.filter(id=id)
    else:
      return
  serializer_class = UserSerializer
  permissions_classes = (
    IsAdminOrCurrentUser
  )

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  def get_queryset(self):
    id = self.kwargs['pk']
    if self.request.user.is_staff == True:
      return User.objects.filter(id=id)
    elif not self.request.user.is_anonymous:
      user = self.request.user.id
      return User.objects.filter(user=user)
    else:
      return
  serializer_class = UserSerializer
  permissions_classes = (
    IsAdminOrCurrentUser
  )

class UserDetailList(generics.ListCreateAPIView):
  def get_queryset(self):
    if self.request.user.is_staff == True:
      return UserDetailModel.objects.all()
    elif not self.request.user.is_anonymous:
      user = self.request.user.id
      return UserDetailModel.objects.filter(user=user)
    else:
      return
  serializer_class = UserDetailSerializer
  permissions_classes = (
    IsAdminOrCurrentUser
  )

  @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
  def perform_create(self, serializer):
    if self.request.data['date_of_birth'] == '1970-01-01':
      date_of_birth = None
    else:
      date_of_birth = self.request.data['date_of_birth']
    if self.request.data['timezone'] == '':
      timezone = 'UTC'
    else:
      timezone = self.request.data['timezone']
    serializer.save(
      user_id=self.request.user.id,
      date_of_birth=date_of_birth,
      timezone=timezone)

class SinglerUserDetail(generics.RetrieveUpdateDestroyAPIView):
  def get_queryset(self):
    id = self.kwargs['pk']
    if self.request.user.is_staff == True:
      return UserDetailModel.objects.filter(id=id)
    elif not self.request.user.is_anonymous:
      user = self.request.user.id
      return UserDetailModel.objects.filter(id=id, user=user)
    else:
      return
  serializer_class = UserDetailSerializer
  permissions_classes = (
    IsAdminOrCurrentUser
  )
