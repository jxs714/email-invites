# NO IMPORTS AT THE TOP LEVEL

class EmailInvitesPlugin:
    def __init__(self):
        from django.utils.translation import gettext_lazy as _
        self.name = _("Email Invites")
        self.author = "JXS"
        self.description = _("Send mass email invitations using pretalx templates")
        self.version = "0.0.1"

    def ready(self):
        # Empty - no imports here
        pass

    def get_urls(self):
        # Import only when absolutely needed
        try:
            from . import urls
            return urls.urlpatterns
        except ImportError:
            return []
