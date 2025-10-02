from django.urls import path

from image_processing_project.views.helloView import helloWorld

urlpatterns = [
    path('hello/', helloWorld, name='helloWorld'),
]