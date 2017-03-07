from django.db import models

class ShipPart(models.Model):
	part_number = models.CharField(
		max_length=100,
		primary_key=True,
		unique=True
	)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	power_req = models.FloatField(default=0.0)
	size_class = models.ForeignKey(
		'SizeClass',
		on_delete=models.CASCADE,
	)

	def __unicode__(self):
		return self.name

	class Meta:
		abstract = True


class Engine(ShipPart):
	speed = models.FloatField(default=0.0)
	jump_distance = models.FloatField(default=0.0)


class Weapon(ShipPart):
	ammo = models.ForeignKey(
		'WeaponBay',
		on_delete=models.CASCADE
	)

	# These are the defaults, the ammo will modify all these fields
	accuracy = models.FloatField(default=0.0)
	min_range = models.FloatField(default=0.0)
	max_range = models.FloatField(default=0.0)
	power_req = models.FloatField(default=0.0)
	shield_damage = models.FloatField(default=0.0)
	hull_damage = models.FloatField(default=0.0)

	class Meta:
		abstract = True

class Laser(Weapon):
	ammo = models.ForeignKey(
		'Crystal',
		on_delete=models.CASCADE
	)

class Plasma(Weapon):
	ammo = models.ForeignKey(
		'Gas',
		on_delete=models.CASCADE
	)

class Kinetic(Weapon):
	ammo = models.ForeignKey(
		'Projectile',
		on_delete=models.CASCADE
	)

class Missile(Weapon):
	ammo = models.ForeignKey(
		'Rocket',
		on_delete=models.CASCADE
	)