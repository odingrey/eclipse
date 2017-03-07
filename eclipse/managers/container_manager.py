from eclipse.models.container import ShipContainer, StationContainer

def generate_ship_container(owner, size, ship):
	return ShipContainer(
		owner=owner,
		size=size,
		ship=ship
	)

def generate_station_container(owner, station):
	return StationContainer(
		owner=owner,
		station=station
	)

def set_owner(containers, owner):
	for contain in containers:
		container.owner = owner
		container.save()

def make_station_container(owner, station):
	generate_station_container(owner, station).save()

def make_ship_container(owner, size, ship):
	generate_ship_container(owner, size, ship).save()