class EmailInvitesPlugin:
    def __init__(self):
        from django.utils.translation import gettext_lazy as _
        self.name = _("Email Invites")
        self.author = "JXS"
        self.description = _("Send mass email invitations using pretalx templates")
        self.version = "0.0.1"

    def ready(self):
        pass

    def get_urls(self):
        try:
            from . import urls
            return urls.urlpatterns
        except ImportError:
            return []

    # ADD THIS METHOD FOR THE MENU ITEM
    def get_orga_urls(self):
        from django.urls import path
        from . import views
        
        return [
            path(
                "send-invitations/",
                views.InvitationSendView.as_view(),
                name="send_invitations",
            ),
        ]
