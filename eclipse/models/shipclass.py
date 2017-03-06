from django.db import models

from .shiptype import ShipType

class ShipClassManager(models.Manager):
	def get_by_natural_key(self, name):
		return self.get(name=name)

class ShipClass(models.Model):
	objects = ShipClassManager()
	name = models.CharField(max_length=30, primary_key=True, unique=True)
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