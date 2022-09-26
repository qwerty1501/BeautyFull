from django.contrib import admin

from .models import Master, Services, Request


admin.site.register(Master)
admin.site.register(Services)
admin.site.register(Request)
