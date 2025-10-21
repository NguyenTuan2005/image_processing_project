from django.urls import path
from image_processing_project.views.imageView import image_generator

urlpatterns = [
    path("generate/", image_generator, name="image_generator"),
]