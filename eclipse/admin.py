from django.contrib import admin
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

admin.site.register(Crystal)
admin.site.register(Gas)
admin.site.register(Projectile)
admin.site.register(Rocket)
admin.site.register(Engine)
admin.site.register(Laser)
admin.site.register(Location)
admin.site.register(Plasma)
admin.site.register(Kinetic)
admin.site.register(Missile)
admin.site.register(ShipContainer)
admin.site.register(StationContainer)
admin.site.register(Planet)
admin.site.register(Player)
admin.site.register(Race)
admin.site.register(Resource)
admin.site.register(Ship)
admin.site.register(ShipClass)
admin.site.register(ShipType)
admin.site.register(SizeClass)
admin.site.register(SolarSystem)
admin.site.register(Station)
admin.site.register(StationClass)
admin.site.register(StationType)



class PlayerInline(admin.StackedInline):
	model = Player

class CustomUser(admin.ModelAdmin):
	inlines = [PlayerInline]

class CustomNpc(admin.ModelAdmin):
	inlines = [PlayerInline]

class CustomGovernment(admin.ModelAdmin):
	inlines = [PlayerInline]


admin.site.unregister(User)
admin.site.register(User, CustomUser)
admin.site.register(Npc, CustomNpc)
admin.site.register(Government, CustomGovernment)
