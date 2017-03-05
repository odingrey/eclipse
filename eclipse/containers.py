from eclipse.models.container import Container

# Logic to make sure only one location is saved at a time.
def set_location(space_entity, location):
	if type(location) is Ship:
		space_entity.ship_location = location
		space_entity.station_location = null
	elif type(location) is Station:
		space_entity.station_location = location
		space_entity.ship_location = null
	space_entity.save()