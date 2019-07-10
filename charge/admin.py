from django.contrib import admin
from .models import Charge, ChargeHistory, Department


class ChargeAdmin(admin.ModelAdmin):

    search_fields = ['name', 'status']


admin.site.register(Department)
admin.site.register(Charge, ChargeAdmin)
admin.site.register(ChargeHistory)

