from django.urls import path
from django.views.generic import ListView
from . import views

app_name = 'world'

urlpatterns = [
    path('map/', views.insert_thing, name="insert_thing"),
]
