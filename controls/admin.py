from django.contrib import admin
from .models import AttendanceRequest, Assistance


class AttendanceAdmin(admin.ModelAdmin):

    list_display = ('status', 'employee', 'from_date', 'to_date')
    search_fields = ['employee', 'status']


class AssistanceAdmin(admin.ModelAdmin):
    search_fields = ['employee']
    list_display = ('mark', 'date')


admin.site.register(AttendanceRequest, AttendanceAdmin),
admin.site.register(Assistance, AssistanceAdmin)
