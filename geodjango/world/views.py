import json
from django.db.models import Value
from django.db.models.functions import Replace
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from django.http import HttpResponse
from django.core.serializers import serialize
from django.urls import path
from django.shortcuts import render
from .models import Things, PanoImg
from . import forms

my_location = Point(46.870782, -96.788118,srid=4326)

class Home(generic.ListView):
    model = PanoImg
    context_object_name = 'panos'
    template_name = 'world/things_list.html'

def things_dataset(request):

    thing = serialize('geojson', Things.objects.all())
    return HttpResponse(thing, content_type='json')

def pic_dataset(request):
    pic = serialize('geojson', PanoImg.objects.all() )
    return HttpResponse(pic, content_type='json')

def insert_thing(request):
    if request.method == 'POST':
        form = forms.ThingForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return render(request, 'world/addthing.html', {'form':form})
    else:
        form = forms.ThingForm()
    return render(request, 'world/addthing.html', {'form':form})

def show_things(request):
    return render(request, 'world/showthings.html')

def thing_details(request, slug):
    thing = Things.objects.get(slug=slug)
    return render(request, 'world/thingdetails.html', { 'thing':thing })
