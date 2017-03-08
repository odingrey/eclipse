from django.db import models

class Location(models.Model):
	solar_system = models.ForeignKey(
		'SolarSystem',
		on_delete=models.CASCADE
	)
	x = models.FloatField(default=0.0)
	y = models.FloatField(default=0.0)
	z = models.FloatField(default=0.0)


	def __unicode__(self):
		return str(self.solar_system) + " x: " + str(self.x) + " y: " + str(self.y) + " z: " + str(self.z)