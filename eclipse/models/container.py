from django.db import models


class ShipContainerManager(models.Manager):
	def generate(self, owner, size, ship):
		return ShipContainer(
			owner=owner,
			size=size,
			ship=ship
		)

	def create(self, owner, size, ship):
		container = ShipContainer(
			owner=owner,
			size=size,
			ship=ship
		)
		container.save()
		return container

class StationContainerManager(models.Manager):
	def create(self, owner, station):
		return StationContainer(
			owner=owner,
			station=station
		)


class Container(models.Model):	

	owner = models.ForeignKey(
		'Player',
		on_delete=models.CASCADE,
		blank=True,
		null=True
	)

	class Meta:
		abstract = True

	def set_owner(self, owner):
		self.owner = owner
		self.save()

	def __unicode__(self):
		return str(self.pk) + ": " + str(self.owner)		

class ShipContainer(Container):
	objects = ShipContainerManager()

	# Only one container per ship, is used in Ship object
	size = models.IntegerField()
	ship = models.ForeignKey(
		'Ship',
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)


class StationContainer(Container):
	objects = StationContainerManager()

	# Many to one relationship to stations
	station = models.ForeignKey(
		'Station',
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)
