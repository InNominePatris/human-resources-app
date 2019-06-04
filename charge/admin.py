from django.contrib import admin
from .models import Charge, ChargeHistory, Department


admin.site.register(Department)
admin.site.register(Charge)
admin.site.register(ChargeHistory)

