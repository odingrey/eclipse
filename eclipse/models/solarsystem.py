from django.db import models

class SolarSystemManager(models.Manager):
	def get_by_natural_key(self, name):
		return self.get(name=name)

class SolarSystem(models.Model):
	objects = SolarSystemManager()
	name = models.CharField(max_length=30, primary_key=True, unique=True)

	def __str__(self):
		return self.name