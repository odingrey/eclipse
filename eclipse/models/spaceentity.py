from django.db import models

class SpaceEntity(models.Model):
	name = models.CharField(max_length=100)
	x = models.FloatField(default=0.0)
	y = models.FloatField(default=0.0)
	z = models.FloatField(default=0.0)

	class Meta:
		abstract = True
