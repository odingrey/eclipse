from django.contrib.auth.models import User
from django.db import models

from .container import StationContainer
from .location import Location
from .spaceentity import SpaceEntity



class ShipManager(models.Manager):
	def create(self, owner, station_class, location=None, name=None, planet_location=None):
		if not location and not planet_location:
			raise AttributeError('Must have either location or planet_location')

		if planet_location:
			location = Location.objects.create(planet_location.location)

		station = Station(
			name = name,
			owner = owner,
			station_class = station_class,
			location = location,
			planet_location = location
		)

		# Create a container sized what the ship class wants, assign to ship
		StationContainer.objects.create(
			owner=owner,
			station=station
		)
		return station.save()


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

	def save(self, *args, **kwargs):
		# This is here literally just so I can add stations in the admin console easier

		if self.planet_location:
			self.location = Location.objects.create(self.planet_location.location)
		super(Station, self).save(*args, **kwargs)


	def __str__(self):
		return str(self.owner) + ": " + self.name
