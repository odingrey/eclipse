from eclipse.models.ship import Ship
from containers import Container


def make_ship(ship_class):
	ship = Ship(
		owner = user, 
		ship_name = "",
		ship_class = ship_class,
		max_hp = 100.00,
		current_hp = 100.00,
		max_powergrid = 100.00,
		current_powergrid = 100.00
	)
	container = Container.make_container()
	container.set_location(ship)

def change_owner()