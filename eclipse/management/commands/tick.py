from django.core.management.base import BaseCommand

from eclipse.models.ship import Ship

import math

class Command(BaseCommand):
	def handle(self, *args, **options):
		ships = Ship.objects.all()
		for ship in ships:
			if ship.location is not ship.destination:
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
		x = abs(dx - lx)
		y = abs(dy - ly)
		z = abs(dz - lz)
		dist = math.sqrt((dx - lx) ** 2 + (dy - ly) ** 2 + (dz - lz) ** 2)
		
		traveltime = dist / ship.engine.speed

		# If traveltime is less than one, move straight to the point
		if traveltime < 1:
			ship.location.move(ship.destination)
			ship.destination.save()
		else:
			ship.location.x += lx / traveltime
			ship.location.y += ly / traveltime
			ship.location.z += lz / traveltime
			ship.location.save()
		ship.save()

	def travel_interstellar(self, ship):
		pass