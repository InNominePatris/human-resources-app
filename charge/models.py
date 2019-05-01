from django.db import models
from django.utils.translation import ugettext_lazy as _
from employee.models import Employee


class Charge(models.Model):
    description = models.CharField(max_length=20, verbose_name=_('Description'), unique=True)
    employee = models.ManyToManyField(Employee, verbose_name=_('Employee'))

    def __str__(self):
        return '{}'.format(self.description, self.employee)

    class Meta:
        verbose_name_plural = _('Charges')
        verbose_name = _('Charge')

