from django.db import models
from employee.models import Employee
from django.utils.translation import ugettext_lazy as _


class AttendanceRequest(models.Model):
    MARRIAGE_PERMISSION = 'Marriage'
    PARLOR_PERMISSION = 'Funeraral'
    JUDGE_PERMISSION = 'Judge'
    PERSONAL_ISSUES_PERMISSION = 'Personal'

    PERMISSION_STATUS = (
        (MARRIAGE_PERMISSION, _('Marriage')),
        (PARLOR_PERMISSION, _('Parlor')),
        (JUDGE_PERMISSION, _('Judge')),
        (PERSONAL_ISSUES_PERMISSION, _('Personal'))
    )

    ATTENDANCE_ACTIVE = 'Active'
    ATTENDANCE_INACTIVE = 'Inactive'

    ATTENDANCE_STATUS = (
        (ATTENDANCE_ACTIVE, _('Active')),
        (ATTENDANCE_INACTIVE, _('Inactive'))
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE, verbose_name=_('Employee')
    )

    type = models.CharField(max_length=10, choices=PERMISSION_STATUS, verbose_name=_('Type'))
    from_date = models.DateField(verbose_name=_('From date'))
    to_date = models.DateField(verbose_name=_('To date'))
    reason = models.CharField(max_length=20, verbose_name=_('Reason'))
    status = models.CharField(max_length=10, choices=ATTENDANCE_STATUS, verbose_name=_('Status'))

    def __str__(self):
        return '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = _('Attendances request')
        verbose_name = _('Attendance request')


class Assistance(models.Model):
    present_status = 'present'
    absent_status = 'Absent'
    half_day_status = 'Half day'

    ASSISTANCE_STATUS = (
        (present_status, _('Present')),
        (absent_status, _('Absent')),
        (half_day_status, _('Half day')),
    )

    employee = models.ManyToManyField(Employee, verbose_name=_('Employees'))
    date = models.DateTimeField(verbose_name=_('Date'))
    mark = models.CharField(max_length=30, choices=ASSISTANCE_STATUS, verbose_name=_('Mark'))
    description = models.CharField(max_length=300, blank=True, verbose_name=_('Description'))

    def __str__(self):
        return '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = _('Assitances')
        verbose_name = _('Assistance')


class ExtraHours(models.Model):
    PAID_TYPE = 'Paid'
    ASSIGNED_TYPE = 'Assigned'

    EXTRA_HOURS_TYPE = (
        (PAID_TYPE, _('Paid')),
        (ASSIGNED_TYPE, _('Assigned'))
    )

    quantity = models.IntegerField(verbose_name=_('Cantidad'))
    description = models.CharField(max_length=300, verbose_name=_('Description'))
    type = models.CharField(max_length=70, choices=EXTRA_HOURS_TYPE, verbose_name=_('Type'))
    checked_by = models.CharField(max_length=70, verbose_name=_('Checked by'))

    def __str__(self):
        return '{} {}'.format(self.quantity, self.type)

    class Meta:
        verbose_name_plural = _('Extras hours')
        verbose_name = _('Extra hours')


class ExtraHoursPlan(models.Model):

    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, _('Active')),
        (STATUS_INACTIVE, _('Inactive')),
    )

    employee = models.ManyToManyField(Employee, verbose_name=_('Employees'))
    initial_date = models.DateField(verbose_name=_('Initial date'))
    final_date = models.DateField(verbose_name=_('Final date'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name=_('Status'))
    reason = models.CharField(max_length=300, verbose_name=_('Reason'))

    def __str__(self):
        return '{} {}'.format(self.employee, self.status)

    class Meta:
        verbose_name_plural = _('Planes de horas extras')
        verbose_name = _('Plan de horas extras')

