from django.db import models


class ContainerManager(models.Manager):
	def generate_ship_container(owner, size, ship):
		return ShipContainer(
			owner=owner,
			size=size,
			ship=ship
		)

	def generate_station_container(owner, station):
		return StationContainer(
			owner=owner,
			station=station
		)

	def set_owner(self, owner):
		self.owner = owner
		self.save()

	def make_station_container(owner, station):
		self.generate_station_container(owner, station).save()

	def make_ship_container(owner, size, ship):
		self.generate_ship_container(owner, size, ship).save()


class Container(models.Model):
	owner = models.ForeignKey(
		'Player',
		on_delete=models.CASCADE
	)

	class Meta:
		abstract = True

	def __unicode__(self):
		return str(self.pk) + ": " + str(self.owner)		

class ShipContainer(Container):
	objects = ContainerManager()

	# Only one container per ship, is used in Ship object
	size = models.IntegerField()
	ship = models.ForeignKey(
		'Ship',
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)


class StationContainer(Container):
	# Many to one relationship to stations
	station = models.ForeignKey(
		'Station',
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)
