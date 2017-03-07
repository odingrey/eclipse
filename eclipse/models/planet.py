from django.db import models

from .spaceentity import SpaceEntity

# Allows for natural key lookup
class PlanetManager(models.Manager):
	def get_by_natural_key(self, name):
		return self.get(name=name)

class Planet(SpaceEntity):
	objects = PlanetManager()
	name = models.CharField(max_length=100, primary_key=True, unique=True)
	# Either an entire race owns it, or a Player
	# TODO: Figure out what to do here?  Is the planet claimable?
	owner = models.ForeignKey(
		'Player', 
		blank=True, 
		null=True, 
		on_delete=models.DO_NOTHING
	)

	def __unicode__(self):
		return self.name