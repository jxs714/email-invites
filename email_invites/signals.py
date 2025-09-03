
from django.dispatch import receiver
from django.urls import reverse

from pretalx.orga.signals import nav_event_settings


@receiver(nav_event_settings)
def email_invites_settings(sender, request, **kwargs):
    if not request.user.has_perm("event.update_event", request.event):
        return []
    return [
        {
            "label": "Email Invites",
            "url": reverse(
                "plugins:email_invites:settings",
                kwargs={"event": request.event.slug},
            ),
            "active": request.resolver_match.url_name
            == "plugins:email_invites:settings",
        }
    ]

