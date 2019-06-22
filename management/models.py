from django.db import models
from django.utils.translation import ugettext_lazy as _
from employee.models import Employee


class Training(models.Model):
    EVENT_PENDING = 'Pending'
    EVENT_ACTIVE = 'Active'
    EVENT_INACTIVE = 'Inactive'
    EVENT_COMPLETED = 'Completed'

    EVENT_STATUS_CHOICES = (
        (EVENT_PENDING, _('Pending')),
        (EVENT_ACTIVE, _('Active')),
        (EVENT_INACTIVE, _('Inactive')),
        (EVENT_COMPLETED, _('Completed'))
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
    training_program = models.CharField(max_length=30, verbose_name=_('Training program'))
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


class TrainingDetail(models.Model):
    title = models.CharField(max_length=20)
