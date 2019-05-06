from django.db import models
from django.utils.translation import ugettext_lazy as _
from employee.models import Employee


class Charge(models.Model):
    description = models.CharField(max_length=20, verbose_name=_('Description'), unique=True)

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name_plural = _('Charges')
        verbose_name = _('Charge')

class History(models.Model):
    detail= models.CharField(max_length=20, verbose_name=_('Detail'))
    initial_date= models.DateField(verbose_name=_('Initial date'))
    final_date = models.DateField(verbose_name=_('Final date'))
    employee = models.ForeignKey(Employee, on_delete= models.CASCADE, verbose_name=_('Employee'))
    charge = models.ForeignKey(Charge, on_delete= models.CASCADE,verbose_name=_('charge'))
    

    def __str__(self):
        return '{} {} {} {} {}'.format(self.detail.initial_date.final_date.employee.charge)
    
    class Meta:
        verbose_name_plural= _('Histories')
        verbose_name= _('History')
    

