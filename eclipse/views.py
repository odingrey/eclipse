from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from managers.ship_manager import ShipManager


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
	return render(request, 'main.html')

def password_reset(request):
	return render(request,'password_reset.html')

@login_required
def settings(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			profile_form = UserProfile(data=request.POST, instance=request.user)
			if profile_form.is_valid():
				profile_form.save()
			return HttpResponseRedirect('/')
		else:
			profile_form = UserProfile();
			return render(request, 'settings.html', {'profile_form': profile_form})
	return HttpResponse(status = 401) # Not Authenticated


