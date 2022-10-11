from django.contrib import admin
from .models import Agent, PollingBooth, Result, Ward


admin.site.register(Agent)
admin.site.register(PollingBooth)
admin.site.register(Result)
admin.site.register(Ward)
