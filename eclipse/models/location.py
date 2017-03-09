from django.db import models


class LocationManager(models.Manager):
	def generate_location(self, location):
		# Copy given location
		location = Location(location)
		# Then unassign the pk, so it forces Django to assign a new one.
		location.pk = None

	def make_location(self, location):
		return self.generate_location(self, location).save()

class Location(models.Model):
	objects = LocationManager()

	solar_system = models.ForeignKey(
		'SolarSystem',
		on_delete=models.CASCADE
	)
	x = models.FloatField(default=0.0)
	y = models.FloatField(default=0.0)
	z = models.FloatField(default=0.0)


	def __unicode__(self):
		return str(self.solar_system) + " x: " + str(self.x) + " y: " + str(self.y) + " z: " + str(self.z)