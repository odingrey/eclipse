from django.db import models

from .player import Player
from .ship import Ship
from .station import Station


class Container(models.Model):
	owner = models.ForeignKey(Player, on_delete=models.CASCADE)
	size = models.IntegerField()
	ship_location = models.ForeignKey(
		Ship,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)
	station_location = models.ForeignKey(
		Station,
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)
