from django.db import models
from employee.models import Employee
from django.utils.translation import ugettext_lazy as _


class VacationRequest(models.Model):
    REQUEST_ACTIVE = 'Active'
    REQUEST_INACTIVE = 'Inactive'

    REQUEST_STATUS = (
        (REQUEST_ACTIVE, _('Active')),
        (REQUEST_INACTIVE, _('Inactive'))
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_('Employee'))
    date = models.DateTimeField(verbose_name=_('Date'))
    detail = models.CharField(max_length=300, verbose_name=_('Detail'))
    status = models.CharField(max_length=10, choices=REQUEST_STATUS, verbose_name=_('Status'))

    def __str__(self):
        return '{} {}'.format(self.employee, self.date)

    class Meta:
        verbose_name_plural = _('Solicitudes de vacaciones')
        verbose_name = _('Solicitud de vacaciones')

