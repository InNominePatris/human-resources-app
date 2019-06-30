from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords


class Employee(models.Model):
    IDENTITY_DNI = 'DNI'
    IDENTITY_PASSPORT = 'PASSPORT'
    IDENTITY_RESIDENCE = 'RESIDENCE'

    IDENTITY_CHOICES = (
        (IDENTITY_DNI, _('DNI')),
        (IDENTITY_PASSPORT, _('PASSPORT')),
        (IDENTITY_RESIDENCE, _('RESIDENCE'))
    )

    GENDER_FEMALE = 'f'
    GENDER_MALE = 'm'

    GENDER_CHOICES = (
        (GENDER_FEMALE, _('Female')),
        (GENDER_MALE, _('Male'))
    )

    STATUS_ALONE = 'a'
    STATUS_MARRIED = 'ma'
    STATUS_DIVORCED = 'd'

    STATUS_CHOICES = (
        (STATUS_ALONE, _('Alone')),
        (STATUS_MARRIED, _('Married')),
        (STATUS_DIVORCED, _('Divorced'))
    )
    first_name = models.CharField(max_length=20, verbose_name=_('First name'))
    last_name = models.CharField(max_length=20, verbose_name=_('Last name'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name=_('Gender'))
    identity = models.CharField(max_length=30, verbose_name=_('Identity'), unique=True)
    type = models.CharField(max_length=10, choices=IDENTITY_CHOICES, verbose_name=_('Type'))
    birthday = models.DateField(verbose_name=_('Birthday'))
    civil_status = models.CharField(max_length=2, choices=STATUS_CHOICES, verbose_name=_('Civil status'))
    address = models.CharField(max_length=50, verbose_name=_('Address'))
    phone = PhoneNumberField(verbose_name=_('Phone'))
    email = models.EmailField(max_length=70, null=False, verbose_name=_('Email'))
    nationality = models.CharField(max_length=20, verbose_name=_('Nationality'), blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name_plural = _('Employees')
        verbose_name = _('Employee')


class AcademicStudies(models.Model):
    PRIMARY_SCHOOL_CHOICE = 'Primary school'
    HIGH_SCHOOL_CHOICE = 'High school'
    UNIVERSITY_CHOICE = 'University'
    BACHELOR_DEGREE = 'Bachelor degree'
    MASTER_DEGREE = 'Master degree'
    DOCTOR_DEGREE = 'Doctor degree'
    POST_DOCTOR_DEGREE = 'Post doctor degree'
    PROFESSIONAL_SCHOOL = 'Professional school'
    NO_STUDY = 'No study'

    EDUCATIONAL_LEVEL_CHOICES = (
        (PRIMARY_SCHOOL_CHOICE, _('Primary')),
        (HIGH_SCHOOL_CHOICE, _('High school')),
        (UNIVERSITY_CHOICE, _('University')),
        (BACHELOR_DEGREE, _('Bachelor degree')),
        (MASTER_DEGREE, _('Master degree')),
        (DOCTOR_DEGREE, _('Doctor degree')),
        (POST_DOCTOR_DEGREE, _('Post doctor degree')),
        (PROFESSIONAL_SCHOOL, _('Professional school')),
        (NO_STUDY, _('No study'))
    )

    GRADE_BS = 'B.S'
    GRADE_BA = 'B.A'
    GRADE_MS = 'M.S'
    GRADE_MA = 'M.A'
    GRADE_PHD = 'Ph.D.'
    GRADE_MBA = 'MBA'
    GRADE_JD = 'JD'
    GRADE_MD = 'MD'

    GRADE_CHOICES = (
        (GRADE_BS, _('B.S')),
        (GRADE_BA, _('B.A')),
        (GRADE_MS, _('M.S')),
        (GRADE_MA, _('M.A')),
        (GRADE_PHD, _('Ph.D.')),
        (GRADE_MBA, _('MBA')),
        (GRADE_JD, _('JD')),
        (GRADE_MD, _('MD'))
    )

    employee = models.ForeignKey(
        Employee,
        verbose_name=_('Employee'), on_delete=models.CASCADE
    )
    study_type = models.CharField(max_length=20, choices=EDUCATIONAL_LEVEL_CHOICES, verbose_name=_('Study type'))
    grade = models.CharField(max_length=6, choices=GRADE_CHOICES, verbose_name=_('Grade'))
    description = models.CharField(max_length=200, verbose_name=_('Description'))
    from_date = models.DateField(null=False, verbose_name=_('From date'))
    to_date = models.DateField(null=True, verbose_name=_('To date'))
    institute = models.CharField(max_length=30, verbose_name=_('Institute'))

    def __str__(self):
        return '{}'.format(self.employee)
