from django.urls import path
from django.views.generic import ListView
from djgeojson.views import GeoJSONLayerView
from .models import Things
from . import views

app_name = 'world'

urlpatterns = [
    path('add/', views.insert_thing, name="insert_thing"),
    path('map/', views.show_things, name="show_things"),
    path('',views.Home.as_view()),
    path('things_data/', views.things_dataset, name='the_things'),
    #path("api/", include("markers.api_urls")),
    #path('<slug:slug>/', views.thing_details, name="things")
    #path('data.geojson', GeoJSONLayerView.as_view(model=Things), name="data")
]
