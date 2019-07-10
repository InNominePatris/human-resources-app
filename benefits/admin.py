from django.contrib import admin
from .models import VacationRequest, VacationPlan, HealthInsurance, HealthInsuranceApplication


class RequestAdmin(admin.ModelAdmin):

    search_fields = ['status', 'employee']


class VacationPlanAdmin(admin.ModelAdmin):
    filter_horizontal = ('employee',)
    list_display = ('status', 'initial_date', 'final_date')


class HealthInsuranceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class HealthInsuranceApplicationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'status', 'provider')


admin.site.register(VacationRequest, RequestAdmin)
admin.site.register(VacationPlan, VacationPlanAdmin)
admin.site.register(HealthInsurance, HealthInsuranceAdmin)
admin.site.register(HealthInsuranceApplication, )
