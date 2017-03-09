from django.db import models


from .container import Container
from .spaceentity import SpaceEntity


class WeaponBay(models.Model):
	pass

class ShipManager(models.Manager):
	def generate_ship(self, owner, ship_class, location):
		ship = Ship(
			owner = owner,
			ship_class = ship_class,
			docked_location = location,
			engine = ship_class.engine,
			weapon_bay = ship_class.weapon_bay,
			location = Location.generate_location(location),
			destination = Location.generate_location(location),
		)
		# Create a container sized what the ship class wants, assign to ship
		Container.generate_ship_container(
			owner=owner,
			size=ship_class.cargosize,
			ship=ship
		)
		return ship

	def set_owner(self, owner):
		self.owner = owner
		self.save()

	def make_ship(self, owner, ship_class, location):
		return self.generate_ship(owner, ship_class, location).save()

class Ship(SpaceEntity):
	objects = ShipManager()

	name = models.CharField(max_length=100)
	destination = models.OneToOneField(
		'Location',
		blank=True,
		null=True,
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

		self.size_class = self.ship_class.ship_type.size_class
		self.hull = self.ship_class.hull
		self.power = self.ship_class.power

		super(Ship, self).save(*args, **kwargs)


	def __unicode__(self):
		return str(self.owner) + ": " + self.ship_class.name