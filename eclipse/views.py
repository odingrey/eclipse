from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse

from eclipse.models.location import Location
from eclipse.models.station import Station

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

HTML_CODES = {
	'ACCEPTED' : '202',
	'UNAUTHORIZED' : '401',
	'FORBIDDEN' : '403',
	'ERROR' : '500'
}



# API Calls
def loginUser(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']

			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse(HTML_CODES['ACCEPTED'])
				else:
					return HttpResponse(HTML_CODES['FORBIDDEN'])
			else:
				return HttpResponse(HTML_CODES['UNAUTHORIZED'])
		else:
			return render(request, 'login.html')

@login_required
@require_http_methods(['POST'])
def move_ship(request):
	if not request.method == 'POST':
		return HttpResponse(HTML_CODES['FORBIDDEN'])

	station = get_object_or_404(Station, pk=request.POST['location'])
	location = station.location
	print location
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
		print e
		return HttpResponse(HTML_CODES['ERROR'])
###############################


#Django Rendering
	
@login_required
def main(request):
	response = {'username': request.user.player.name}
	return render(request, 'main.html', response)

def password_reset(request):
	return render(request,'password_reset.html')

@login_required
def move(request):
	context = dict()
	context['stations'] = Station.objects.all()
	return render(request, 'move.html', context)
