__version__ = "0.0.1"

from django.urls import path
from django.utils.translation import gettext_lazy as _

class EmailInvitesPlugin:
    name = _("Email Invites")
    author = "JXS"
    description = _("Send mass email invitations using pretalx templates")
    version = "0.0.1"

    def ready(self):
        # This method is called when the plugin is loaded
        pass

    def get_urls(self):
        # This registers the URLs for the plugin
        from . import views
        return [
            path(
                "send-invitations/",
                views.InvitationSendView.as_view(),
                name="send_invitations",
            ),
        ]

    # CRITICAL: This method adds the plugin to the admin menu
    def register_orga_urls(self, urlpatterns):
        from . import views
        urlpatterns.append(
            path(
                "send-invitations/",
                views.InvitationSendView.as_view(),
                name="send_invitations",
            ),
        )

