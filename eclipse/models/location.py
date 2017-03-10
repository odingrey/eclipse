from django.db import models


class LocationManager(models.Manager):
	def create(self, location):
		# Unassign the pk, so it forces Django to assign a new one.
		location.pk = None
		location.save()
		return location


class Location(models.Model):
	objects = LocationManager()

	solar_system = models.ForeignKey(
		'SolarSystem',
		on_delete=models.CASCADE
	)
	x = models.FloatField(default=0.0)
	y = models.FloatField(default=0.0)
	z = models.FloatField(default=0.0)


	def move(self, location):
		self.x = location.x
		self.y = location.y
		self.z = location.z
		self.solar_system = location.solar_system
		self.save()

	def __unicode__(self):
		return str(self.solar_system) + " x: " + str(self.x) + " y: " + str(self.y) + " z: " + str(self.z)