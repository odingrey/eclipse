from django.db import models

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
