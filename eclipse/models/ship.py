from django.db import models

from eclipse.management import container_manager

from .spaceentity import SpaceEntity


class WeaponBay(models.Model):
	pass

class Ship(SpaceEntity):
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

		# If first save
		if not self.pk:
			# Set initial values from the ship class
			self.owner = self.owner
			self.engine = self.ship_class.engine
			self.weapon_bay = self.ship_class.weapon_bay
			self.destination = None

			# Create a container sized what the ship class wants, assign to ship
			container_manager.generate_ship_container(
				owner=self.owner,
				size=self.ship_class.cargosize,
				ship=self
			)

		super(Ship, self).save(*args, **kwargs)


	def __unicode__(self):
		return str(self.owner) + ": " + self.ship_class.name