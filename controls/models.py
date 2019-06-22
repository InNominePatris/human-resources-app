from django.db import models
from employee.models import Employee
from django.utils.translation import ugettext_lazy as _


class AttendanceRequest(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE, verbose_name=_('Employee')
    )
    from_data = models.DateField(verbose_name=_('From data'))
    to_data = models.DateField(verbose_name=_('To data'))
    reason = models.CharField(max_length=20, verbose_name=_('Reason'))

    def __str__(self):
        return '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = _('Attendances request')
        verbose_name = _('Attendance request')