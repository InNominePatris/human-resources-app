from django.db import models
from employee.models import Employee
from django.utils.translation import ugettext_lazy as _


class Beneficiary(models.Model):
    GENDER_FEMALE = 'f'
    GENDER_MALE = 'm'

    GENDER_CHOICES = (
        (GENDER_FEMALE, _('Female')),
        (GENDER_MALE, _('Male'))
    )

    IDENTITY_DNI = 'DNI'
    IDENTITY_PASSPORT = 'PASSPORT'
    IDENTITY_RESIDENCE = 'RESIDENCE'

    IDENTITY_CHOICES = (
        (IDENTITY_DNI, _('DNI')),
        (IDENTITY_PASSPORT, _('PASSPORT')),
        (IDENTITY_RESIDENCE, _('RESIDENCE'))
    )

    first_name = models.CharField(max_length=20, verbose_name=_('First name'))
    last_name = models.CharField(max_length=20, verbose_name=_('Last name'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name=_('Gender'))
    identity = models.CharField(max_length=30, verbose_name=_('Identity'), unique=True)
    type = models.CharField(max_length=10, choices=IDENTITY_CHOICES, verbose_name=_('Type'))

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = _('Beneficiaries')
        verbose_name = _('Beneficiary')


class Contract(models.Model):
    DEFINED_CONTRACT = 'Defined'
    UNDEFINED_CONTRACT = 'Undefined'

    CONTRACT_TYPE = (
        (DEFINED_CONTRACT, _('Defined')),
        (UNDEFINED_CONTRACT, _('Undefined'))
    )

    type = models.CharField(max_length=10, choices=CONTRACT_TYPE, verbose_name=_('Type'))
    initial_date = models.DateField(null=False, verbose_name=_('Initial date'))
    final_date = models.DateField(null=True, verbose_name=_('Final date'))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name=_('Employee'))
    beneficiary = models.ManyToManyField(
        Beneficiary,
        verbose_name=_('Beneficiary')
    )

    def __str__(self):
        return '{}'.format(self.employee.first_name)

    class Meta:
        verbose_name_plural = _('Contracts')
        verbose_name = _('Contract')
