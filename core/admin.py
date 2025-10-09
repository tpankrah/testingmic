from django.contrib import admin
from .models import CheckType, Tenant, Monitor, Check, Oncall

# Register your models here.
admin.site.register(CheckType)
admin.site.register(Tenant)
admin.site.register(Monitor)
admin.site.register(Check)
admin.site.register(Oncall)