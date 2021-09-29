from django.contrib.gis.db.models import PointField
from django.contrib.gis.db import models
from django.contrib.gis import forms

class Things(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1000)
    #picture = models.ImageField()
    geom = models.PointField()
    @property
    def lat_lng(self):
        return list(getattr(self.geom, 'coords', [])[::-1])


    def __unicode__(self):
        return self.title

class Blog(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=200)

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    headline = models.CharField(max_length=255)
    point = PointField()
    @property
    def lat_lng(self):
        return list(getattr(self.point, 'coords', [])[::-1])
