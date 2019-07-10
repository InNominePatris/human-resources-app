from django.contrib import admin
from .models import Training, TrainingProgram


class TrainingAdmin(admin.ModelAdmin):
    search_fields = ['title', 'envent_status', 'enterprise']
    list_display = ('title', 'event_status', 'type')


class TrainingProgramAdmin(admin.ModelAdmin):
    filter_horizontal = ('employee',)
    list_display = ('name', 'training', 'status')


admin.site.register(Training, TrainingAdmin)
admin.site.register(TrainingProgram, TrainingProgramAdmin)