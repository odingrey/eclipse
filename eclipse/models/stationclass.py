from django.db import models

class StationClassManager(models.Manager):
	def get_by_natural_key(self, name):
		return self.get(name=name)

class StationClass(models.Model):
	objects = StationClassManager()
	name = models.CharField(max_length=30, primary_key=True, unique=True)
	station_type = models.ForeignKey(
		'StationType',
		on_delete=models.CASCADE,
	)
	race = models.ForeignKey(
		'Race',
		on_delete=models.CASCADE)
	description = models.CharField(max_length=300, default="")
	power = models.FloatField()
	hull = models.FloatField()

	def __unicode__(self):
		return self.name
