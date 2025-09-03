from django.apps import AppConfig
from django.utils.translation import gettext_lazy

from . import __version__


class PluginApp(AppConfig):
    name = "email_invites"
    verbose_name = "Email Invites"

    class PretalxPluginMeta:
        name = gettext_lazy("Email Invites")
        author = "Fueled By X"
        description = gettext_lazy("Invite users by email")
        visible = True
        version = __version__
        category = "FEATURE"

    def ready(self):
        from . import signals  # NOQA
