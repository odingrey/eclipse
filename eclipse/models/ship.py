from django.db import models
from django.contrib.auth.models import User

class Ship(models.Model):
	owner = models.ForeignKey(User)
	ship_name = models.CharField(max_length=100)
	ship_class = models.CharField(max_length=30)
	max_hp = models.FloatField()
	current_hp = models.FloatField()
	max_powergrid = models.FloatField()
	current_powergrid = models.FloatField()
