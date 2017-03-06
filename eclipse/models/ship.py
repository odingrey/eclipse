from django.contrib.auth.models import User
from django.db import models

from .spaceentity import SpaceEntity
from .shipclass import ShipClass

class Ship(SpaceEntity):
	name = models.CharField(max_length=100)
	owner = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		blank=True,
		null=True
	)
	race = models.CharField(max_length=30)
	description = models.CharField(max_length=300)
	ship_class = models.ForeignKey(
		ShipClass,
		on_delete=models.CASCADE,
	)
	hull = models.FloatField()
	powergrid = models.FloatField()
