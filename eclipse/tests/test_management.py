from django.core.management import call_command
from django.test import TestCase

from eclipse.models.location import Location
from eclipse.models.ship import Ship
from eclipse.models.shipclass import ShipClass
from eclipse.models.solarsystem import SolarSystem
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

	def testMoveCorrectlyOutwards(self):
		sol = SolarSystem.objects.get(pk='Sol')
		location2 = Location(x=200,y=200,z=200,solar_system=sol)
		ship = Ship.objects.get(pk=1)
		ship.location.x=100
		ship.location.y=100
		ship.location.z=100
		ship.location.save()
		ship.save()
		ship.move(location2)

		expected = {
			'x': 128.8675134594813,
			'y': 128.8675134594813,
			'z': 128.8675134594813,
		}

		call_command('tick')
		# Grab ship from DB again
		ship = Ship.objects.get(pk=1)

		self.assertEqual(ship.location.x, expected['x'])
		self.assertEqual(ship.location.y, expected['y'])
		self.assertEqual(ship.location.z, expected['z'])

	def testMoveCorrectlyInwards(self):
		sol = SolarSystem.objects.get(pk='Sol')
		location2 = Location(x=100,y=100,z=100,solar_system=sol)
		ship = Ship.objects.get(pk=1)
		ship.location.x=200
		ship.location.y=200
		ship.location.z=200
		ship.location.save()
		ship.save()
		ship.move(location2)

		expected = {
			'x': 171.1324865405187,
			'y': 171.1324865405187,
			'z': 171.1324865405187,
		}

		call_command('tick')
		# Grab ship from DB again
		ship = Ship.objects.get(pk=1)

		self.assertEqual(ship.location.x, expected['x'])
		self.assertEqual(ship.location.y, expected['y'])
		self.assertEqual(ship.location.z, expected['z'])