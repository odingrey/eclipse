from django.db import models

class Npc(models.Model):

	def __str__(self):
		return str(self.pk) + ": " + self.name