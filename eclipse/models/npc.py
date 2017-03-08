from django.db import models

class Npc(models.Model):

	def __unicode__(self):
		return str(self.pk) + ": " + self.name