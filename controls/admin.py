from django.contrib import admin
from .models import AttendanceRequest, Assistance, ExtraHours, ExtraHoursPlan


class AttendanceAdmin(admin.ModelAdmin):

    list_display = ('status', 'employee', 'from_date', 'to_date')
    search_fields = ['employee', 'status']


class AssistanceAdmin(admin.ModelAdmin):
    search_fields = ['employee']
    list_display = ('mark', 'date')


class ExtraHoursPlanAdmin(admin.ModelAdmin):
    filter_horizontal = ('employee',)


admin.site.register(AttendanceRequest, AttendanceAdmin),
admin.site.register(Assistance, AssistanceAdmin),
admin.site.register(ExtraHours),
admin.site.register(ExtraHoursPlan, ExtraHoursPlanAdmin)

