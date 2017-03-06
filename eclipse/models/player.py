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

	def save(self, *args, **kwargs):
		# Error if more than one is set.
		if sum([1 for x in (self.npc, self.user, self.government,) if x]) > 1:
			raise AttributeError('Requires User, NPC or Government, not more than one')

		# Error if none are set.
		if sum([1 for x in (self.npc, self.user, self.government,) if x]) == 0:
			raise AttributeError('Requires User, NPC or Government')

		# Error if location is incorrect.
		if self.npc or self.user and not self.location:
			raise AttributeError('Requires location to be set if player is NPC or User')
		if self.government:
			self.location = None
		
		super(Player, self).save(*args, **kwargs)

	def __unicode__(self):
		if self.user:
			return "User: " + self.user.username
		if self.npc:
			return "NPC: " + self.npc.name
		if self.government:
			return "Government: " + self.government.name