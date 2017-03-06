from django.db import models

from .solarsystem import SolarSystem

class SpaceEntity(models.Model):
	solarsystem = models.ForeignKey(SolarSystem)
	x = models.FloatField(default=0.0)
	y = models.FloatField(default=0.0)
	z = models.FloatField(default=0.0)

	class Meta:
		abstract = True
