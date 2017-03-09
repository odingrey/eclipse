from django.contrib.auth.models import User
from django.db import models

from .spaceentity import SpaceEntity
from .container import StationContainer


class ShipManager(models.Manager):
	def create(self, owner, station_class, location, name=None, planet_location=None):
		station = Station(
			name = name,
			location = location,
			owner = owner,
			station_class = station_class,
		)

		# Set location
	
		# Create a container sized what the ship class wants, assign to ship
		StationContainer.objects.create(
			owner=owner,
			station=station
		)
		return station


class Station(SpaceEntity):
	objects = ShipManager()
	name = models.CharField(max_length=100, default="Station")
	# TODO: Maybe keep the station?  Make it claimable?
	owner = models.ForeignKey(
		'Player', 
		blank=True, 
		null=True, 
		on_delete=models.CASCADE
	)
	# Optional planet location
	planet_location = models.ForeignKey(
		'Planet',
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)
	station_class = models.ForeignKey(
		'StationClass',
		on_delete=models.CASCADE
	)

	def add_to_planet(self, planet):
		self.planet_location = planet


	def __unicode__(self):
		return str(self.owner) + ": " + self.name