from django.contrib import admin

from eclipse.models.container import Container
from eclipse.models.government import Government
from eclipse.models.npc import Npc
from eclipse.models.planet import Planet
from eclipse.models.player import Player
from eclipse.models.race import Race
from eclipse.models.resource import Stack, Resource
from eclipse.models.ship import Ship
from eclipse.models.shipclass import ShipClass
from eclipse.models.shiptype import ShipType
from eclipse.models.solarsystem import SolarSystem
from eclipse.models.spaceentity import SpaceEntity
from eclipse.models.station import Station
from eclipse.models.stationclass import StationClass
from eclipse.models.stationtype import StationType

admin.site.register(Container)
admin.site.register(Government)
admin.site.register(Npc)
admin.site.register(Planet)
admin.site.register(Player)
admin.site.register(Race)
admin.site.register(Resource)
admin.site.register(Ship)
admin.site.register(ShipClass)
admin.site.register(ShipType)
admin.site.register(SolarSystem)
admin.site.register(Station)
admin.site.register(StationClass)
admin.site.register(StationType)