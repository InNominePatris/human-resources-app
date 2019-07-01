from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ContractConfig(AppConfig):
    name = 'contract'

    verbose_name = _('Contract')
