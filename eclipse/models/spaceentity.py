from django.db import models

class SpaceEntity(models.Model):
	solar_system = models.ForeignKey(
		'SolarSystem',
		on_delete=models.CASCADE
	)
	x = models.FloatField(default=0.0)
	y = models.FloatField(default=0.0)
	z = models.FloatField(default=0.0)

	class Meta:
		abstract = True
