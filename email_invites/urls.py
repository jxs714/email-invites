
from django.urls import re_path

from pretalx.event.models.event import SLUG_REGEX

from .views import EmailInvitesSettingsView

urlpatterns = [
    re_path(
        rf"^orga/event/(?P<event>{SLUG_REGEX})/settings/p/email_invites/$",
        EmailInvitesSettingsView.as_view(),
        name="settings",
    ),
]
