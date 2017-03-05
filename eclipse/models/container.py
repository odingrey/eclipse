from django.db import models
from django.contrib.auth.models import User
from .ship import Ship
from .station import Station

class Container(models.Model):
	owner = models.ForeignKey(User)
	size = models.IntegerField()
	ship_location = models.ForeignKey(Ship, blank=True, null=True)
	station_location = models.ForeignKey(Station, blank=True, null=True)
