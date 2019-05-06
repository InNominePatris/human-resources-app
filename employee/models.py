from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Employee(models.Model):
    GENDER_FEMALE = 'f'
    GENDER_MALE = 'm'

    GENDER_CHOICES = (
        (GENDER_FEMALE, _('Female')),
        (GENDER_MALE, _('Male'))
    )

    STATUS_ALONE = 'a'
    STATUS_ADJOINED = 'ad'
    STATUS_MARRIED = 'ma'
    STATUS_DIVORCED = 'd'

    STATUS_CHOICES = (
        (STATUS_ALONE, _('Alone')),
        (STATUS_ADJOINED, _('Adjoined')),
        (STATUS_MARRIED, _('Married')),
        (STATUS_DIVORCED, _('Divorced'))
    )

    first_name = models.CharField(max_length=20, verbose_name=_('First name'), unique=True)
    last_name = models.CharField(max_length=20, verbose_name=_('Last name'), unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name=_('Gender'))
    dni = models.CharField(max_length=10, verbose_name=_('Dni'), unique=True)
    birthday = models.DateField(verbose_name=_('Birthday'))
    civil_status = models.CharField(max_length=2, choices=STATUS_CHOICES, verbose_name=_('Civil status'))
    address = models.CharField(max_length=50, verbose_name=_('Address'))
    phone = PhoneNumberField(verbose_name=_('Phone'))
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = _('Employees')
        verbose_name = _('Employee')



