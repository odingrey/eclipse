from django.contrib import admin

from eclipse.models.container import Container
from eclipse.models.resource import Stack, Resource
from eclipse.models.ship import Ship

admin.site.register(Ship)
admin.site.register(Container)
admin.site.register(Stack)
admin.site.register(Resource)