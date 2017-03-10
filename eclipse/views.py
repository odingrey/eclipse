from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib import auth
from django.contrib.auth.decorators import login_required


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
					return HttpResponse('202') #Accepted
				else:
					return HttpResponse('403') #Forbidden (IE, account is banned)
			else:
				return HttpResponse('401') #Unauthorized (IE, bad username and password)
		else:
			return render(request, 'login.html')

@login_required
def move_ship(request):
	ship = request.user.player.current_ship
	ship.move_ship(request.location)
	ship.save()
	return HttpResponse('202')

################################  
@login_required
def addTest(request):
	try:
		newShip = ships.create_test(request.user)
		return HttpResponse('202')
	except e:
		print e
		return HttpResponse('500')
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
	return render(request, 'move.html')
