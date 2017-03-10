from django.db import models

class Government(models.Model):
	homeworld = models.ForeignKey(
		'Planet',
		blank=True,
		null=True,
		on_delete=models.CASCADE
	)
	description = models.CharField(max_length=300, default="")

	def __str__(self):
		return self.player.name