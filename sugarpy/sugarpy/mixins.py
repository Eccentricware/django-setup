from __future__ import unicode_literals
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings

class InjectUrlDataMixin:
    #We are trying to get url captures into serializers
    def get_serializer(self, *args, **kwargs):
        #They say this is the standard logic
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)