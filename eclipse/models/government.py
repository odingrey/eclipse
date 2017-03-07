from django.db import models

class GovernmentManager(models.Manager):
	def get_by_natural_key(self, name):
		return self.get(name=name)

class Government(models.Model):
	objects = GovernmentManager()
	name = models.CharField(max_length=100, primary_key=True, unique=True)
	race = models.ForeignKey(
		'Race',
		blank=True,
		null=True,
		on_delete=models.CASCADE
	)
	description = models.CharField(max_length=300, default="")

	def __unicode__(self):
		return self.name