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