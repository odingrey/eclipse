from eclipse.models.ship import Ship
from eclipse.models.shipclass import ShipClass
import container_manager


ship_classes = ShipClass.objects

def generate_ship(owner, ship_class, x, y, z, location):
	ship = Ship(
		owner = owner,
		name = ship_class.name,
		ship_class = ship_class,
		size_class = ship_class.ship_type.size_class,
		hull = ship_class.hull,
		power = ship_class.power,
		engine = ship_class.engine,
		weapon_bay = ship_class.weapon_bay,
		x = x,
		y = y,
		z = z,
		docked_location = location
	)
	return ship

def set_owner(ship, owner):
	ship.owner = owner
	#TODO: This
	#container_manager.set_owner(ship.container_set, owner)
	ship.save()

def make_ship(owner, ship_class, x, y, z, location):
	generate_ship(owner, ship_class, x, y, z, location).save()