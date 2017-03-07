from django.db import models

class ShipClassManager(models.Manager):
	def get_by_natural_key(self, name):
		return self.get(name=name)

class ShipClass(models.Model):
	objects = ShipClassManager()
	name = models.CharField(max_length=30, primary_key=True, unique=True)
	ship_type = models.ForeignKey(
		'ShipType',
		on_delete=models.DO_NOTHING,
	)
	race = models.ForeignKey(
		'Race',
		blank=True,
		null=True,
		on_delete=models.CASCADE
	)
	description = models.CharField(max_length=300, default="")
	power = models.FloatField()
	hull = models.FloatField()
	cargosize = models.FloatField()
	engine = models.ForeignKey(
		'Engine',
		on_delete=models.DO_NOTHING,
	)
	weapon_bay = models.ForeignKey(
		'WeaponBay',
		on_delete=models.DO_NOTHING,
		blank=True,
		null=True
	)

	def __unicode__(self):
		return self.name