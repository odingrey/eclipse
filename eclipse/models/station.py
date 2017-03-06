from django.contrib.auth.models import User
from django.db import models

from .stationclass import StationClass
from .spaceentity import SpaceEntity
from .planet import Planet
from .race import Race

class Station(SpaceEntity):
	name = models.CharField(max_length=100)
	# Either an entire race owns it, or a User
	race = models.ForeignKey(Race, blank=True, null=True)
	owner = models.ForeignKey(User, blank=True, null=True)
	# Optional planet location
	planet_location = models.ForeignKey(
		Planet,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)
	station_class = models.ForeignKey(StationClass)
	hull = models.FloatField()
	power = models.FloatField()

	def __unicode__(self):
		return str(self.pk) + ": " + self.name