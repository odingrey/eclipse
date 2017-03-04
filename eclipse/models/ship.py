from django.db import models

class Ship(models.Model):
	ship_name = models.CharField(max_length=30)
