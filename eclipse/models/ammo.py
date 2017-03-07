from django.db import models

from .resource import Resource

class Ammo(Resource):
	accuracy_mod = models.FloatField(default=0.0)
	min_range_mod = models.FloatField(default=0.0)
	max_range_mod = models.FloatField(default=0.0)
	power_req_mod = models.FloatField(default=0.0)
	shield_damage_mod = models.FloatField(default=0.0)
	hull_damage_mod = models.FloatField(default=0.0)

	class Meta:
		abstract = True

class Projectile(Ammo):
	pass

class Gas(Ammo):
	pass

class Rocket(Ammo):
	pass

class Crystal(Ammo):
	pass