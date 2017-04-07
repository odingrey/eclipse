from django.contrib.auth import authenticate, login
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from eclipse.models.ship import Ship
from eclipse.models.station import Station

import json

HTML_CODES = {
	'ACCEPTED' : '202',
	'UNAUTHORIZED' : '401',
	'FORBIDDEN' : '403',
	'ERROR' : '500'
}


@login_required
@require_http_methods(['GET'])
def get_player(request):
	if not request.method == 'GET':
		return HttpResponse(HTML_CODES['FORBIDDEN'])
	user = request.user.player
	data = serializers.serialize('json', [user])
	# Remove array wrapper
	struct = json.loads(data)
	data = json.dumps(struct[0])
	return HttpResponse(data, content_type='application/json')


@login_required
@require_http_methods(['GET'])
def get_ships(request):
	if not request.method == 'GET':
		return HttpResponse(HTML_CODES['FORBIDDEN'])
	ships = Ship.objects.filter(owner=request.user.player).all()
	print ships
	data = serializers.serialize('json', ships)
	print data
	# Remove array wrapper
	struct = json.loads(data)
	data = json.dumps(struct)
	return HttpResponse(data, content_type='application/json')


@login_required
@require_http_methods(['POST'])
def move_ship(request):
	if not request.method == 'POST':
		return HttpResponse(HTML_CODES['FORBIDDEN'])

	station = get_object_or_404(Station, pk=request.POST['location'])
	location = station.location
	ship = request.user.player.current_ship
	ship.move(location)
	return HttpResponse(HTML_CODES['ACCEPTED'])

################################  
@login_required
def addTest(request):
	try:
		newShip = ships.create_test(request.user)
		return HttpResponse(HTML_CODES['ACCEPTED'])
	except e:
		return HttpResponse(HTML_CODES['ERROR'])
###############################