from django.core.management import call_command
from django.test import TestCase

from eclipse.models.location import Location
from eclipse.models.ship import Ship
from eclipse.models.shipclass import ShipClass
from eclipse.models.station import Station

class MoveTest(TestCase):
	fixtures = ['eclipse_data']
	
	def setUp(self):
		pod = ShipClass.objects.get(pk="Lifepod")
		location = Station.objects.get(pk=1)
		new_ship = Ship.objects.create(
			owner=None,
			ship_class=pod,
			station_location=location
			)
		new_ship.save()

	def testMove(self):
		location2 = Station.objects.get(pk=3).location
		ship = Ship.objects.get(pk=1)
		original_loc = Location.objects.create(ship.location)
		ship.move(location2)
		call_command('tick')
		# Grab ship from DB again
		ship = Ship.objects.get(pk=1)

		self.assertIsNot(ship.location, original_loc)
		self.assertNotEqual(ship.location.x, original_loc.x)
		self.assertNotEqual(ship.location.y, original_loc.y)
		self.assertNotEqual(ship.location.z, original_loc.z)
		self.assertEqual(ship.location.solar_system, original_loc.solar_system)
