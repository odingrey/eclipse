from django.contrib.auth.models import User
from django.db import models

from .spaceentity import SpaceEntity
from .container import StationContainer

class Station(SpaceEntity):
	name = models.CharField(max_length=100)
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
	hull = models.FloatField()
	power = models.FloatField()

	def save(self, *args, **kwargs):
		# Set coords to planetary location
		if self.planet_location:
			self.x = self.planet_location.x
			self.y = self.planet_location.y
			self.z = self.planet_location.z

		self.hull = self.station_class.hull
		self.power = self.station_class.power

		super(Station, self).save(*args, **kwargs)

		# Generation a container the first time.
		if StationContainer.objects.filter(station=self).count() == 0:
			StationContainer.objects.create(
				owner=self.owner, 
				station=self
			)
		

	def __unicode__(self):
		return str(self.owner) + ": " + self.name