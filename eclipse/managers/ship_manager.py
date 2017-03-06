from eclipse.models.ship import Ship
from eclipse.models.shipclass import ShipClass
import container_manager


ship_classes = ShipClass.objects

def generate_ship(owner, ship_class):
	ship = Ship(
		owner = owner,
		ship_name = ship_class.class_name,
		ship_class = ship_class,
		hull = ship_class.base_hp,
		power = ship_class.power
	)
	container = container_manager.generate_container(owner, ship_class.cargo_size)
	container.set_location(ship)

def set_owner(ship, owner):
	ship.owner = new_owner
	container_manager.set_owner(ship.container_set, owner)
	ship.save()

def make_ship(owner, ship_class, x, y, z, solar_system):
	ship = generate_ship(ship_class)
	ship.x = x
	ship.y = y
	ship.z = z
	ship.solar_system = solar_system
	ship.save()