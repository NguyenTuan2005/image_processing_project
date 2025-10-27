from django.urls import path

from generate import views

urlpatterns = [
    path("", views.create_image , name="create_image"),
]