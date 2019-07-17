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

    def __str__(self):
        return '{}'.format(self.employee)


