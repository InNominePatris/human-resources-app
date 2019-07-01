from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BenefitsConfig(AppConfig):
    name = 'benefits'

    verbose_name = _('Beneficios')
