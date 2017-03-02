from django.conf.urls import include, url
from django.conf.urls.static import static
from eclipse import views
from eclipse import settings

from django.contrib import admin
from django.contrib import auth
admin.autodiscover()


urlpatterns = [
        url(r'^$', views.index),
	url(r'^main/$', views.main),
        url(r'^admin/', admin.site.urls),
        url(r'^login/$', views.loginUser),
        url(r'^logout/$', auth.logout, {'next_page': '/'}),
        url(r'^register/$', views.register),
	url(r'^settings/$', views.settings),
	]
#) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
