from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from eclipse import views
from eclipse import settings

from django.contrib import admin
from django.contrib import auth
from django.contrib.auth.views import login, logout
admin.autodiscover()


urlpatterns = [
	url(r'^$', views.main),
        url(r'^admin/', admin.site.urls),
        url(r'^login/$', login),
        url(r'^logout/$', logout),
	url(r'^settings/$', views.settings),
	url(r'^navbar', TemplateView.as_view(template_name='static/navbar.html')),
	]
