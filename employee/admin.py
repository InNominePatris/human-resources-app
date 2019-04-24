from django.contrib import admin
from .models import Employee
from django.contrib.auth.models import User, Group


admin.site.register(Employee)
admin.site.unregister(User)
admin.site.unregister(Group)
