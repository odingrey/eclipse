from django.db import models

# Allows for natural key lookup
class ShipTypeManager(models.Manager):
	def get_by_natural_key(self, name):
		return self.get(name=name)

class ShipType(models.Model):
	objects = ShipTypeManager()

	name = models.CharField(max_length=30, primary_key=True, unique=True)
	description = models.CharField(max_length=300, default="")
	size_class = models.ForeignKey(
		'SizeClass',
		on_delete=models.DO_NOTHING,
		blank=True,
		null=True
	)

	def __str__(self):
		return self.name