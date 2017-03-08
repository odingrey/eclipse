from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from eclipse.management import ship_manager

from .government import Government
from .npc import Npc
from .race import Race
from .shipclass import ShipClass
from .station import Station

class Player(models.Model):
	name = models.CharField(max_length=100)
	race = models.OneToOneField(
		'Race',
		blank=True,
		null=True,
		on_delete=models.CASCADE
	)	
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		blank=True,
		null=True
	)
	npc = models.OneToOneField(
		Npc,
		on_delete=models.CASCADE,
		blank=True,
		null=True
	)
	government = models.OneToOneField(
		Government,
		on_delete=models.CASCADE,
		blank=True,
		null=True
	)
	location = models.ForeignKey(
		'Ship',
		blank=True,
		null=True,
		on_delete=models.DO_NOTHING
	)


	# Generate a player whenever a user registers
	@receiver(post_save, sender=User)
	def create_user_player(sender, instance, created, **kwargs):
		if created:
			# Make a pod, put the user in it
			pod = ShipClass.objects.get(pk="Lifepod")
			location = Station.objects.get(pk=1)
			# TODO: Don't hardcode race, let the player choose
			#race = Race.objects.get(pk="Human")
			#race_gov = race.player.
			#homeworld = Planet.objects.get(pk=)
			new_ship = ship_manager.generate_ship(
				None,
				pod,
				location
				)
			new_ship.save()

			# Save user
			new_player = Player.objects.create(
				name=sender.username,
				user=instance,
				location=new_ship
			)
			ship_manager.set_owner(new_ship, new_player)

	# Save the player info whenever a user object is saved
	@receiver(post_save, sender=User)
	def save_user_player(sender, instance, **kwargs):
		instance.player.save()


	# Generate a player whenever a user registers
	@receiver(post_save, sender=Npc)
	def create_npc_player(sender, instance, created, **kwargs):
		if created:
			Player.objects.create(npc=instance)

	# Save the player info whenever a user object is saved
	@receiver(post_save, sender=Npc)
	def save_npc_player(sender, instance, **kwargs):
		instance.player.save()


	# Generate a player whenever a user registers
	@receiver(post_save, sender=Government)
	def create_government_player(sender, instance, created, **kwargs):
		if created:
			Player.objects.create(government=instance)

	# Save the player info whenever a user object is saved
	@receiver(post_save, sender=Government)
	def save_government_player(sender, instance, **kwargs):
		instance.player.save()


	# Logic to check saving
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
		
		super(Player, self).save(*args, **kwargs)

	def __unicode__(self):
		if self.user:
			return "User: " + self.name
		if self.npc:
			return "NPC: " + self.name
		if self.government:
			return "Government: " + self.name