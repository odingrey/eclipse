from django.contrib.auth.models import User
from django.db import models

from .government import Government
from .npc import Npc
from .race import Race

class Player(models.Model):
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		blank=True,
		null=True
	)
	npc = models.ForeignKey(
		Npc,
		on_delete=models.CASCADE,
		blank=True,
		null=True
	)
	government = models.ForeignKey(
		Government,
		on_delete=models.CASCADE,
		blank=True,
		null=True
	)
	race = models.ForeignKey(Race, on_delete=models.CASCADE)
	location = models.ForeignKey(
		'Ship',
		blank=True,
		null=True,
		on_delete=models.DO_NOTHING
	)

	def __unicode__(self):
		if self.user:
			return "User: " + self.user.username
		if self.npc:
			return "NPC: " + self.npc.name
		if self.government:
			return "Government: " + self.government.name