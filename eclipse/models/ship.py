from django.db import models

from eclipse.managers import container_manager

from .spaceentity import SpaceEntity


class WeaponBay(models.Model):
	pass

class Ship(SpaceEntity):
	name = models.CharField(max_length=100)
	size_class = models.ForeignKey(
		'SizeClass',
		on_delete=models.DO_NOTHING,
		blank=True,
		null=True
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
	hull = models.FloatField(default=0.1)
	power = models.FloatField(default=0.1)
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
			self.x = self.docked_location.x
			self.y = self.docked_location.y
			self.z = self.docked_location.z
			self.solar_system = self.docked_location.solar_system

		self.size_class = self.ship_class.ship_type.size_class
		self.hull = self.ship_class.hull
		self.power = self.ship_class.power

		# If first save
		if not self.pk:
			container_manager.generate_ship_container(
				owner=self.owner,
				size=self.ship_class.cargosize,
				ship=self
			)

		super(Ship, self).save(*args, **kwargs)


	def __unicode__(self):
		return str(self.owner) + ": " + self.name