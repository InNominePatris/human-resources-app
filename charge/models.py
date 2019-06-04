from django.db import models
from django.utils.translation import ugettext_lazy as _
from employee.models import Employee


class Department(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('Name'))
    description = models.CharField(max_length=100, verbose_name=_('Description'), null=False)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = _('Departments')
        verbose_name = _('Department')


class Charge(models.Model):
    STATUS_ACTIVE = 'Active',
    STATUS_INACTIVE = 'Inactive'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, _('Active')),
        (STATUS_INACTIVE, _('Inactive')),
    )

    name = models.CharField(max_length=20, verbose_name=_('Name'))
    description = models.CharField(max_length=20, verbose_name=_('Description'), unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name=_('Status'))
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE, verbose_name=_('Department'))

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name_plural = _('Charges')
        verbose_name = _('Charge')


class ChargeHistory(models.Model):
    STATUS_ACTIVE = 'Active',
    STATUS_INACTIVE = 'Inactive'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, _('Active')),
        (STATUS_INACTIVE, _('Inactive')),
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE, verbose_name=_('Employee'))
    charge = models.ForeignKey(
        Charge,
        on_delete=models.CASCADE, verbose_name=_('Charge'))
    initial_date = models.DateField(verbose_name=_('Initial date'))
    final_date = models.DateField(verbose_name=_('Final date'))
    motive_movement = models.CharField(max_length=300, verbose_name=_('Motive of movement'))
    authorized_for = models.CharField(max_length=20, verbose_name=_('Authorized for'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name=_('Status'))

    def __str__(self):
        return '{}'.format(self.employee.first_name)

    class Meta:
        verbose_name_plural = _('Charges history')
        verbose_name = _('Charge history')



