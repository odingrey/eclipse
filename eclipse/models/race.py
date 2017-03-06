from django.db import models

# Allows for natural key lookup
class RaceManager(models.Manager):
	def get_by_natural_key(self, name):
		return self.get(name=name)


class Race(models.Model):
	objects = RaceManager()
	name = models.CharField(max_length=30, primary_key=True, unique=True)
	description = models.CharField(max_length=300)

	def __unicode__(self):
		return self.name