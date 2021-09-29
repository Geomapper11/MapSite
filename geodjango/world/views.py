from django.urls import path
from django.shortcuts import render
from django.views.generic import ListView
from .models import Things
from . import forms

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
