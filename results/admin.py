from django.contrib import admin
from .models import Agent, PollingUnit, Ward


admin.site.register(Agent)
admin.site.register(PollingUnit)
admin.site.register(Ward)
