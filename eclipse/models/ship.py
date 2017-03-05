from django.contrib.auth.models import User
from django.db import models

from .spaceentity import SpaceEntity

class Ship(SpaceEntity):
	owner = models.ForeignKey(User)
	ship_class = models.CharField(max_length=30)
	max_hp = models.FloatField()
	current_hp = models.FloatField()
	max_powergrid = models.FloatField()
	current_powergrid = models.FloatField()
