from eclipse.models.ship import Ship

def create_test(user):
	return Ship.objects.create(
		owner = user, 
		ship_name = "",
		ship_class = 'Test',
		max_hp = 100.00,
		current_hp = 100.00,
		max_powergrid = 100.00,
		current_powergrid = 100.00
		)