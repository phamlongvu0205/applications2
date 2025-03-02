# example/urls.py
from django.urls import path

from applications.views import index


urlpatterns = [
    path('', index),
]