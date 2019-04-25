from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ChargeConfig(AppConfig):
    name = 'charge'

    verbose_name = _('Charge')

