from django.contrib.auth.models import User
from django.db import models

from .spaceentity import SpaceEntity
from .race import Race

# Allows for natural key lookup
class PlanetManager(models.Manager):
	def get_by_natural_key(self, name):
		return self.get(name=name)

class Planet(SpaceEntity):
	objects = PlanetManager()
	name = models.CharField(max_length=100, primary_key=True, unique=True)
	# Either an entire race owns it, or a User
	race = models.ForeignKey(Race, blank=True, null=True)
	owner = models.ForeignKey(User, blank=True, null=True)

	def __unicode__(self):
		return self.name