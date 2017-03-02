from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib import auth
from django.contrib.auth.decorators import login_required

from forms.register import UserRegistrationForm
from forms.user import UserProfile


@login_required(login_url='/login/')
def index(request):
		return render(request, 'index.html')

@login_required(login_url='/login/')
def main(request):
	if user.is_authenticated():
		return render(request, 'main.html')
	return HttpResponseRedirect('/login')


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


def register(request):
		#TODO(mike): Redirect failed registration into correct window instead of new one
		registered = False
		if request.method == 'POST':
			user_form = UserRegistrationForm(data=request.POST)	 #Fills form with POST data
			profile_form = UserProfile(data=request.POST)
			if user_form.is_valid() and profile_form.is_valid():
				user = user_form.save()
				user.save()						#saves new user
				profile = profile_form.save(commit=False)
				profile.user = user
				profile.save()					# saves new user profile
				registered = True
			else:
				print(user_form.errors, profile_form.errors)	 #Will output to apache's error.log

		else:
			user_form = UserRegistrationForm() #creates forms to pass to the front end for filling out
			profile_form = UserProfile()

		return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

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
