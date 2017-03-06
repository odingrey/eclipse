from django.db import models

from .shiptype import ShipType

class ShipClass(models.Model):
	name = models.CharField(max_length=30, primary_key=True)
	ship_type = models.ForeignKey(
		ShipType,
		on_delete=models.CASCADE,
	)
	race = models.CharField(max_length=30)
	description = models.CharField(max_length=300, default="")
	power = models.FloatField()
	hull = models.FloatField()
	cargohold = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name