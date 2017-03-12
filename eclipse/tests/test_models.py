from django.test import TestCase
from django.contrib.auth.models import User

from eclipse.models.ammo import Crystal, Gas, Projectile, Rocket
from eclipse.models.container import ShipContainer, StationContainer
from eclipse.models.government import Government
from eclipse.models.location import Location
from eclipse.models.npc import Npc
from eclipse.models.planet import Planet
from eclipse.models.player import Player
from eclipse.models.race import Race
from eclipse.models.resource import Stack, Resource
from eclipse.models.ship import Ship, WeaponBay
from eclipse.models.shipclass import ShipClass
from eclipse.models.shippart import *
from eclipse.models.shiptype import ShipType
from eclipse.models.sizeclass import SizeClass
from eclipse.models.solarsystem import SolarSystem
from eclipse.models.spaceentity import SpaceEntity
from eclipse.models.station import Station
from eclipse.models.stationclass import StationClass
from eclipse.models.stationtype import StationType

#class ShipTestCase



class LocationTestCase(TestCase):

	def setUp(self):
		sol = SolarSystem.objects.create(name="Sol")
		Location(
			x=0,
			y=0,
			z=0,
			solar_system=sol
		).save()
		Location(
			x=100,
			y=100,
			z=100,
			solar_system=sol
		).save()

	def testCreate(self):
		location = Location.objects.get(pk=1)
		newLocation = Location.objects.create(location)
		# Make sure they aren't the same object
		self.assertIsNot(location, newLocation)

	def testMove(self):
		location = Location.objects.get(pk=1)
		location2 = Location.objects.get(pk=2)
		location.move(location2)

		self.assertIsNot(location, location2)
		self.assertEqual(location.x, location2.x)
		self.assertEqual(location.y, location2.y)
		self.assertEqual(location.z, location2.z)
		self.assertEqual(location.solar_system, location2.solar_system)


class ShipTestCase(TestCase):
	fixtures = ['eclipse_data']		

	def testCreate(self):
		pod = ShipClass.objects.get(pk="Lifepod")
		location = Station.objects.get(pk=1)
		new_ship = Ship.objects.create(
			owner=None,
			ship_class=pod,
			station_location=location
			)
		new_ship.save()

		self.assertEqual(new_ship.location.x, new_ship.destination.x)
		self.assertEqual(new_ship.location.y, new_ship.destination.y)
		self.assertEqual(new_ship.location.z, new_ship.destination.z)
		self.assertEqual(new_ship.location.solar_system, new_ship.destination.solar_system)

