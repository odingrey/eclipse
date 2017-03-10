from django.db import models

class SpaceEntity(models.Model):
	location = models.OneToOneField(
		'Location',
		on_delete=models.CASCADE,
		related_name='%(class)s_location'
	)
	class Meta:
		abstract = True
