from django.db import models

class Resource(models.Model):
	name = models.CharField(max_length=100)
	weight = models.IntegerField()

class Stack(models.Model):
	resource = models.ForeignKey(
		'Resource',
		on_delete=models.CASCADE
	)
	ship_container = models.ForeignKey(
		'ShipContainer',
		on_delete=models.CASCADE
	)
	station_container = models.ForeignKey(
		'StationContainer',
		on_delete=models.CASCADE
	)
	quantity = models.IntegerField()
	weight = models.IntegerField()

	def clean(self):
		# Check save logic
		
		if self.ship_container and self.station_container:
			raise AttributeError('Requires either ship_container or station_container, not both')
		if not self.ship_container and notself.station_container:
			raise AttributeError('Requires either ship_container or station_container')
