from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meme/', views.create_meme, name='create_meme'),
]
