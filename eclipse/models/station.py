from django.contrib.auth.models import User
from django.db import models

from .planet import Planet
from .player import Player
from .race import Race
from .stationclass import StationClass
from .spaceentity import SpaceEntity

class Station(SpaceEntity):
	name = models.CharField(max_length=100)
	# TODO: Maybe keep the station?  Make it claimable?
	owner = models.ForeignKey(Player, blank=True, null=True, on_delete=models.CASCADE)
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