from django.db import models

from .race import Race

class Npc(models.Model):
	name = models.CharField(max_length=100)
	race = models.ForeignKey(Race, blank=True, null=True, on_delete=models.CASCADE)

	def __unicode__(self):
		return str(self.pk) + ": " + self.name