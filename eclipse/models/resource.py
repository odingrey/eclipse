from django.db import models
from .container import Container

class Resource(models.Model):
	weight = models.IntegerField()

class Stack(models.Model):
	resource = models.ForeignKey(Resource)
	container = models.ForeignKey(Container)
	quantity = models.IntegerField()
	weight = models.IntegerField()
