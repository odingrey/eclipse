from eclipse.models.ship import Ship
from eclipse.models.shipclass import ShipClass
import container_manager


ship_classes = ShipClass.objects

def generate_ship(owner, ship_class, location):
	ship = Ship(
		owner = owner,
		ship_class = ship_class,
		docked_location = location
	)
	return ship

def set_owner(ship, owner):
	ship.owner = owner
	#TODO: This
	#container_manager.set_owner(ship.container_set, owner)
	ship.save()

def make_ship(owner, ship_class, location):
	generate_ship(owner, ship_class, location).save()