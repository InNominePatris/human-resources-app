from django.contrib import admin
from .models import Employee, AcademicStudies


class EmployeeAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'email')
    search_fields = ['first_name']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(AcademicStudies)


