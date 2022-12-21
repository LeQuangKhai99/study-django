from django import views
from django.urls import path, include

from polls import views

urlpatterns = [
    path('polls', views.index, name="index"),
]