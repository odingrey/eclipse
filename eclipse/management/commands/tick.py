from django.core.management.base import BaseCommand

from eclipse.ship import Ship

import math

class Command(BaseCommand):
	def handle(self, *args, **options):
		ships = Ship.objects.all()
		for ship in ships:
			if ship.destination:
				speed = ship.engine.speed
				x = abs(ship.location.x - ship.destination.x)
				y = abs(ship.location.y - ship.destination.y)
				z = abs(ship.location.z - ship.destination.z)
				traveldistance = abs(x + y + z)
				
				traveltime = math.floor(traveldistance / speed)

				# If it's less than a tick, it goes straight there
				traveltime = 1 if traveltime == 0

				ship.location.x = ship.location.x - int(x / traveltime)
				ship.location.y = ship.location.y - int(y / traveltime)
				ship.location.z = ship.location.y - int(z / traveltime)
