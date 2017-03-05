from eclipse.models.container import Container

def make_container(owner, size):
	return Container(owner, size)

# Logic to make sure only one location is saved at a time.
def set_location(space_entity, location):
	if type(location) is Ship:
		space_entity.ship_location = location
		space_entity.station_location = null
	elif type(location) is Station:
		space_entity.station_location = location
		space_entity.ship_location = null
	space_entity.save()

def set_owner(container, owner):
	container.owner = owner
	container.save()