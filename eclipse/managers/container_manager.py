from eclipse.models.container import Container

def generate_container(owner, size):
	return Container(
		owner=owner,
		size=size
	)

# Logic to make sure only one location is saved at a time.
def set_location(space_entity, location):
	#  Maybe use optionals here instead?
	if type(location) is Ship:
		space_entity.ship_location = location
		space_entity.station_location = null
	elif type(location) is Station:
		space_entity.station_location = location
		space_entity.ship_location = null
	space_entity.save()

def set_owner(containers, owner):
	for contain in containers:
		container.owner = owner
		container.save()