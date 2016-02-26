
from django.apps import AppConfig

default_app_config = 'leonardo_auth_kerberos.Config'


LEONARDO_APPS = ['leonardo_auth_kerberos', 'django_auth_kerberos']

LEONARDO_ORDERING = -6
LEONARDO_AUTH_BACKENDS = ['django_auth_kerberos.backends.KrbBackend']


class Config(AppConfig):
    name = 'leonardo_auth_kerberos'
    verbose_name = "leonardo-auth-kerberos"
