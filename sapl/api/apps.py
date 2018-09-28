from django import apps
from django.db.models.signals import post_save, post_delete
from django.dispatch.dispatcher import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

_time_refresh_models = {}


class AppConfig(apps.AppConfig):
    name = 'sapl.api'
    label = 'api'
    verbose_name = _('API Rest')


def _get_registration_key(model):
    return '%s:%s' % (model._meta.app_label, model._meta.model_name)


def time_refresh(model=None):
    def register(model):
        _time_refresh_models[_get_registration_key(model)] = timezone.now()
        return model

    if model is None:
        return register

    return register(model)


@receiver([post_save, post_delete])
def time_refresh_signal(sender, instance, **kwargs):
    refresh = _time_refresh_models.get(_get_registration_key(sender), None)

    if refresh:
        _time_refresh_models[refresh] = timezone.now()
