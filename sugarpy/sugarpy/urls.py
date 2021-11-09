"""sugarpy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken.views import obtain_auth_token

from readings.views import ReadingDetail, ReadingList, ReadingListTimeSpan
from user_details.views import SinglerUserDetail, UserDetailList, UserList, UserDetail, NewUser, UserSelfDetail, Logout, ChangePassword, LoginStatus, CheckUsernameAvailability

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()

# Wire up our API using automatic URL routing
# Additionally, we include login URLs for the browsable API
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('users/', UserList.as_view()),
    path('user_info/', UserSelfDetail.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('check_username/<username>/', CheckUsernameAvailability.as_view()),
    path('register/', NewUser.as_view()),
    path('user/login_status/', LoginStatus.as_view()),
    path('user/login/', obtain_auth_token),
    path('user/logout/', Logout.as_view()),
    path('user/change_password/', ChangePassword.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/readings/', ReadingList.as_view()),
    path('api/readings/<int:pk>/', ReadingDetail.as_view()),
    path('api/readings_since/<int:days_ago>/', ReadingListTimeSpan.as_view()),
    path('api/user_details/', UserDetailList.as_view()),
    path('api/user_details/<int:pk>/', SinglerUserDetail.as_view())
]
