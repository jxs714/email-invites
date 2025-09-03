from django.utils.translation import gettext_lazy as _

try:
    from pretalx.plugin import Plugin
except ImportError:
    class Plugin:
        pass


class EmailInvitesPlugin(Plugin):
    name = _("Email Invites")
    author = "JXS"
    description = _("Send mass email invitations using pretalx templates")
    version = "0.0.1"

    def ready(self):
        from . import views  # noqa

    def get_urls(self):
        from . import urls
        return urls.urlpatterns
