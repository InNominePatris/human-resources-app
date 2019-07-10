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
    date = models.DateField(verbose_name=_('Date'))
    detail = models.CharField(max_length=300, verbose_name=_('Detail'))
    status = models.CharField(max_length=10, choices=REQUEST_STATUS, verbose_name=_('Status'))

    def __str__(self):
        return '{} {}'.format(self.employee, self.date)

    class Meta:
        verbose_name_plural = _('Solicitudes de vacaciones')
        verbose_name = _('Solicitud de vacaciones')


class VacationPlan(models.Model):
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, _('Active')),
        (STATUS_INACTIVE, _('Inactive')),
    )

    employee = models.ManyToManyField(
        Employee,
        verbose_name=_('Employee')
    )
    initial_date = models.DateField(verbose_name=_('Initial date'))
    final_date = models.DateField(verbose_name=_('Final date'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name=_('Status'))
    description = models.CharField(max_length=300, verbose_name=_('Description'))

    def __str__(self):
        return '{} {}'.format(self.employee, self.status)

    class Meta:
        verbose_name_plural = _('Vacations plan')
        verbose_name = _('Vacation plan')


class HealthInsurance(models.Model):
    name = models.CharField(max_length=70, verbose_name=_('Name'))
    description = models.CharField(max_length=300, verbose_name=_('Descripción'))
    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = _('Heath insurances')
        verbose_name = _('Health insurance')


class HealthInsuranceApplication(models.Model):
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, _('Active')),
        (STATUS_INACTIVE, _('Inactive')),
    )

    INSURANCE_INISER = 'Iniser'
    INSURANCE_ASSA = 'Assa'
    INSURANCE_AMERICA = 'América'
    INSURANCE_INSS = 'Inss'

    INSURANCE_CHOICES = (
        (INSURANCE_INISER, _('Iniser')),
        (INSURANCE_ASSA, _('Assa')),
        (INSURANCE_AMERICA, _('America')),
        (INSURANCE_INSS, _('Inss'))
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE, verbose_name=_('Employee')
    )
    health_insurance = models.ForeignKey(HealthInsurance, on_delete=models.CASCADE, verbose_name=_('Seguro médicco'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name=_('Status'))
    provider = models.CharField(max_length=14, choices=INSURANCE_CHOICES, verbose_name=_('Provider'))
    offer_date = models.DateField(verbose_name=_('Offer date'))
    description = models.CharField(max_length=300, verbose_name=_('Description'))

    def __str__(self):
        return '{} {}'.format(self.employee, self.status)

    class Meta:
        verbose_name_plural = _('Insurances application')
        verbose_name = _('Insurance application')













