from django.utils.translation import gettext_lazy as _

class EmailInvitesPlugin:
    name = _("Email Invites")
    author = "JXS"
    description = _("Send mass email invitations using pretalx templates")
    version = "0.0.1"

    def ready(self):
        # Don't import anything here that might cause issues
        pass

    def get_urls(self):
        # Import only when needed to avoid circular imports
        try:
            from . import urls
            return urls.urlpatterns
        except ImportError:
            return []
