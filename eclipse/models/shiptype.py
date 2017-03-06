from django.db import models

# Allows for natural key lookup
class ShipTypeManager(models.Manager):
	def get_by_natural_key(self, name):
		return self.get(name=name)

class ShipType(models.Model):
	objects = ShipTypeManager()

	name = models.CharField(max_length=30, primary_key=True, unique=True)
	description = models.CharField(max_length=300, default="")

	def __unicode__(self):
		return self.name