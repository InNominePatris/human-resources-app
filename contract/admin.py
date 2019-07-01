from django.contrib import admin
from .models import Beneficiary, Contract


class BenficiaryAdmin(admin.ModelAdmin):
    filter_horizontal = ('beneficiary',)

    list_display = ('employee', 'type', 'initial_date', 'final_date')


admin.site.register(Beneficiary)
admin.site.register(Contract, BenficiaryAdmin)
