from django.shortcuts import render

from eclipse.models.station import Station

from django.contrib.auth.decorators import login_required



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
