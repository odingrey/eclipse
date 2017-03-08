from django.db import models

class SpaceEntity(models.Model):
	location = models.OneToOneField(
		'Location',
		on_delete=models.CASCADE
	)
	class Meta:
		abstract = True
