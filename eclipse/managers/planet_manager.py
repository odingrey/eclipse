from eclipse.models.planet import Planet


def set_owner(planet, owner=null, race=null):
	if not race and not owner:
		raise AttributeError('Requires either an owner or race')
	if race and owner:
		raise AttributeError('Requires either an owner or race, not both')
	if race:
		planet.race = race
	elif owner:
		planet.owner = owner
	planet.save()
