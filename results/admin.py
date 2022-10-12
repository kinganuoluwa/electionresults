from django.contrib import admin
from .models import PollingUnit, Result, Ward


admin.site.register(PollingUnit)
admin.site.register(Result)
admin.site.register(Ward)
