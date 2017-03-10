from django.db import models

# As in, Personal, Small, Medium, Capital, Super Capital
class SizeClass(models.Model):
	SHIP_SIZE_CHOICES = (
		('POD', 'Pod'),
		('P', 'Personal'),
		('S', 'Small'),
		('M', 'Medium'),
		('L', 'Large'),
		('C', 'Capital'),
		('SC', 'Super Capital'),

	)
	name = models.CharField(
		max_length=3,
		choices=SHIP_SIZE_CHOICES,
		default='POD',
		primary_key=True,
		unique=True,
	)

	def __str__(self):
		return self.name
	