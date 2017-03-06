from eclipse.models.station import Station

def generate_station(solar_system, x, y, z, station_class):
	return Station(
		x = x,
		y = y,
		z = z,
		planet = null,
		station_class = station_class,
		hull = station_class.hull,
		power = station_class.power,
	)

def change_owner(station, owner=null, race=null):
	if not race and not owner:
		raise AttributeError('Requires either an owner or race')
	if race and owner:
		raise AttributeError('Requires either an owner or race, not both')
	if race:
		station.race = race
	elif owner:
		station.owner = owner


def move_to_planet(station, planet):
	station.x = planet.x
	station.y = planet.y
	station.z = planet.z
	station.planet = planet;
	return station

def set_to_planet(station, planet):
	station = move_to_planet(station, planet)
	station.save()


def generate_station_on_planet(owner=null, race=null, station_class, planet):
	station = generate_station(owner, 0, 0, 0, station_class)
	set_to_planet(station, planet)
	change_owner(station, owner, race)
	return station
