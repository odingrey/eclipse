from django.db import models


from .container import ShipContainer
from .location import Location
from .spaceentity import SpaceEntity


class WeaponBay(models.Model):
	pass

class ShipManager(models.Manager):
	def create(self, owner, ship_class, station_location):
		ship = Ship(
			name = ship_class.name,
			owner = owner,
			ship_class = ship_class,
			docked_location = station_location,
			engine = ship_class.engine,
			weapon_bay = ship_class.weapon_bay,
			location = Location.objects.create(station_location.location),
			destination = Location.objects.create(station_location.location)
		)
	
		return ship
		# Create a container sized what the ship class wants, assign to ship
		container = ShipContainer.objects.generate(
			owner=owner,
			size=ship_class.cargosize,
			ship=ship
		)
		ship.save()
		container.save()
		return ship


class Ship(SpaceEntity):
	objects = ShipManager()

	name = models.CharField(max_length=100)
	destination = models.OneToOneField(
		'Location',
		on_delete=models.CASCADE,
		related_name='%(class)s_destination'
	)
	owner = models.ForeignKey(
		'Player',
		on_delete=models.CASCADE,
		blank=True,
		null=True
	)
	ship_class = models.ForeignKey(
		'ShipClass',
		on_delete=models.CASCADE,
	)
	engine = models.ForeignKey(
		'Engine',
		on_delete=models.DO_NOTHING,
		blank=True,
		null=True
	)
	weapon_bay = models.ForeignKey(
		'WeaponBay',
		on_delete=models.DO_NOTHING,
		blank=True,
		null=True
	)
	docked_location = models.ForeignKey(
		'Station',
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)

	def save(self, *args, **kwargs):
		# Set coords to docked location
		if self.docked_location:
			self.location = self.docked_location.location

		super(Ship, self).save(*args, **kwargs)

	def move(self, location):
		self.destination.move(location)
		self.save()


	def set_owner(self, owner):
		self.owner = owner
		self.save()


	def __unicode__(self):
		return str(self.owner) + ": " + self.ship_class.name