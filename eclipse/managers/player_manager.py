from eclipse.models.npc import Npc
from eclipse.models.player import Player

players = Player.objects

def generate_player(npc, user, government):
	if not npc and not user and not government:
		raise AttributeError('Requires either NPC or User')
	# Counts trues, if it's more than 1, more than 1 field was set...
	if sum([1 for x in (npc, user, government,) if x]) > 1:
		raise AttributeError('Requires either NPC or User, not both')

	if npc:
		return Player(npc=npc)
	elif user:
		return Player(user=user)
	elif government:
		return Player(government=government)
	return

def generate_npc(name, race):
	npc = Npc(name=name, race=race)
	player = generate_player(npc)
	return player

def generate_government(name, race, government):
	gov = Government(name=name, race=race)
	player = generate_player(government)
	return player