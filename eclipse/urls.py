from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from eclipse import api
from eclipse import views
from eclipse import settings

from django.contrib import admin
from django.contrib import auth
from django.contrib.auth.views import login, logout
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
admin.autodiscover()


urlpatterns = [
	# Django default stuff
  url(r'^admin/', admin.site.urls),
  url(r'^login/$', login, name='login'),
  url(r'^logout/$', logout),
	url(r'^register/', CreateView.as_view(
		template_name='registration/register.html',
		form_class=UserCreationForm,
		success_url='/'
	)),
	url(r'^pasword_reset/$', views.password_reset, name='password_reset'),
	#url(r'^settings/$', views.settings),
	url(r'^welcome/$', TemplateView.as_view(
		template_name='welcome.html'
	)),
	url('^accounts/', include('django.contrib.auth.urls')),   # Remove this bit after a while, useful for now




	# Templates
	url(r'^$', views.main),
	url(r'^move/$', views.move),




	# API Calls
	#url(r'^buy_ship/$', views.addTest),
	url(r'^move_ship/$', api.move_ship),
]
