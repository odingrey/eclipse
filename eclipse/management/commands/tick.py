from django.core.management.base import BaseCommand

from eclipse.models.ship import Ship

import math

class Command(BaseCommand):
	def handle(self, *args, **options):
		ships = Ship.objects.all()
		for ship in ships:
			if not ship.location.isEqualTo(ship.destination):
				if ship.location.solar_system == ship.destination.solar_system:
					self.travel_local(ship)
				else:
					self.travel_interstellar(ship)



	def travel_local(self, ship):
		lx = ship.location.x
		ly = ship.location.y
		lz = ship.location.z
		dx = ship.destination.x
		dy = ship.destination.y
		dz = ship.destination.z
		x = dx - lx
		y = dy - ly
		z = dz - lz
		dist = math.sqrt(x ** 2 + y ** 2 + z ** 2)
		
		traveltime = dist / ship.engine.speed

		# If traveltime is less than one, move straight to the point
		if traveltime < 1:
			ship.location.move(ship.destination)
			ship.location.save()
		else:
			ship.location.x += x / traveltime
			ship.location.y += y / traveltime
			ship.location.z += z / traveltime
			ship.location.save()
		ship.save()

	def travel_interstellar(self, ship):
		pass