from django.utils.translation import gettext_lazy as _

try:
    from pretalx.plugin import Plugin
except ImportError:
    # Fallback for when pretalx is not available (during build)
    class Plugin:
        pass

class EmailInvitesPlugin(Plugin):
    name = _("Email Invites")
    author = "JXS"
    description = _("Send mass email invitations using pretalx templates")
    version = "0.0.1"

    def ready(self):
        # Don't import anything here that might cause circular imports
        pass

    def get_urls(self):
        try:
            from . import urls
            return urls.urlpatterns
        except ImportError:
            return []
