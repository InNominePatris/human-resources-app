from django.contrib import admin
from .models import Training


class TrainingAdmin(admin.ModelAdmin):

    list_display = ('title', 'event_status', 'type')


admin.site.register(Training, TrainingAdmin)
