# django-setup
Install pip
  for Debian/Ubuntu:
    `sudo apt install python3-pip`

Install a virtual environment (venv)
  `python3 -m venv {project-name}`
  activate virtual environment with `source {project-name}/bin/activate`
    (Deactive with `deactivate`)

Install Django
  `python -m pip install Django`

Start a Django project
  `django-admin startproject {project-name}`

Install Django REST framework
  `pip install djangorestframework`
  `pip install markdown `      # Markdown support for the browsable API.
  `pip install django-filter`  # Filtering support

Hide secret key
  create a new file such as secrets.py, and then in the cut-paste the `SECRET_KEY` into it
  Update the key in the settings
    from secrets import key
    ...
    SECRET_KEY = key

Add 'rest_framework' to your `INSTALLED_APPS` in the `settings.py` file
  INSTALLED_APPS = [
    ...
    'rest_framework',
  ]

For the advantageous browsable API, add to the core url file:
  urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
  ]

For serializers, fastest is to just use the meta:
  class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
      model = Reading
      fields = ('__all__')

For views, generic is best:
  class ReadingList(generics.ListCreateAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

  class ReadingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

This is followed up with the url scheme:
  urlpatterns = [
    ... ,
    path('readings/', ReadingList.as_view()),
    path('readings/<int:pk>/', ReadingDetail.as_view())
  ]


# Set up user login (WIP):
Add the default authentication credentials
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework.authentication.BasicAuthentication',
          'rest_framework.authentication.SessionAuthentication',
          'rest_framework.authentication.TokenAuthentication'
      ]
  }
-View handles the login triggered by the request to the url endpoint
-Trying to do this without coupling it to webpack


For parsing arbitrary information from the