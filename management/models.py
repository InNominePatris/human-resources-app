from django.db import models
from django.utils.translation import ugettext_lazy as _
from employee.models import Employee


class Training(models.Model):
    EVENT_ACTIVE = 'Active'
    EVENT_INACTIVE = 'Inactive'

    EVENT_STATUS_CHOICES = (
        (EVENT_ACTIVE, _('Active')),
        (EVENT_INACTIVE, _('Inactive')),
    )

    GAMING_TRAINING = 'Gaming'
    ONLINE_TRAINING = 'Online'
    ORIENTATION_TRAINING = 'Orientation'
    COACHING_TRAINING = 'Coaching'
    MVP_TRAINING = 'Mvp'
    WORKSHOP_TRAINING = 'Workshop',

    TRAINING_CHOICES = (
        (GAMING_TRAINING, _('Gaming')),
        (ONLINE_TRAINING, _('Online')),
        (ORIENTATION_TRAINING, _('Orientation')),
        (COACHING_TRAINING, _('Coaching')),
        (MVP_TRAINING, _('Mvp')),
        (WORKSHOP_TRAINING, _('Workshop'))
    )

    BEGINNER_LEVEL = 'Beginner'
    MEDIUM_LEVEL = 'Medium'
    EXPERT_LEVEL = 'Expert'

    EXPERTISE_CHOICES = (
        (BEGINNER_LEVEL, _('Beginner')),
        (MEDIUM_LEVEL, _('Medium')),
        (EXPERT_LEVEL, _('Expert')),
    )

    title = models.CharField(max_length=30, verbose_name=_('Title'))
    event_status = models.CharField(max_length=10, choices=EVENT_STATUS_CHOICES, verbose_name=_('Event status'))
    type = models.CharField(max_length=20, choices=TRAINING_CHOICES, verbose_name=_('Type'))
    level = models.CharField(max_length=20, choices=EXPERTISE_CHOICES, verbose_name=_('Level'))
    start_time = models.DateField(verbose_name=_('Start time'))
    end_time = models.DateField(verbose_name=_('End time'))
    enterprise = models.CharField(max_length=30, verbose_name=_('Enterprise'))

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name_plural = _('Trainings')
        verbose_name = _('Training')


class TrainingProgram(models.Model):
    PROGRAM_PENDING = 'Pending'
    PROGRAM_ACTIVE = 'Active'
    PROGRAM_INACTIVE = 'Inactive'
    PROGRAM_COMPLETED = 'Completed'

    PROGRAM_STATUS_CHOICES = (
        (PROGRAM_PENDING, _('Pending')),
        (PROGRAM_ACTIVE, _('Active')),
        (PROGRAM_INACTIVE, _('Inactive')),
        (PROGRAM_COMPLETED, _('Completed'))
    )

    name = models.CharField(max_length=70, verbose_name=_('Nombre de programa de entrenamiento'))
    training = models.ForeignKey(
        Training,
        on_delete=models.CASCADE, verbose_name=_('Training')
    )
    employee = models.ManyToManyField(
        Employee,
        verbose_name=_('Employee')
    )
    status = models.CharField(max_length=10, choices=PROGRAM_STATUS_CHOICES, verbose_name=_('Status'))
    start_time = models.DateField(verbose_name=_('Start time'))
    end_time = models.DateField(verbose_name=_('End time'))
    enterprise = models.CharField(max_length=30, verbose_name=_('Enterprise'))

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = _('Programas de entrenamiento')
        verbose_name = _('Programas de entrenamiento')
