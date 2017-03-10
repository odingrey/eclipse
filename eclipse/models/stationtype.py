from django.db import models

# Allows for natural key lookup
class StationTypeManager(models.Manager):
	def get_by_natural_key(self, name):
		return self.get(name=name)

class StationType(models.Model):
	objects = StationTypeManager()

	name = models.CharField(max_length=30, primary_key=True, unique=True)
	description = models.CharField(max_length=300, default="")

	def __str__(self):
		return self.name