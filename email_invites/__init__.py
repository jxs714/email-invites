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
        # Import here to avoid circular imports during plugin discovery
        try:
            from . import views  # noqa
        except ImportError as e:
            # Log the error but don't crash the plugin loading
            print(f"Error importing views: {e}")

    def get_urls(self):
        try:
            from . import urls
            return urls.urlpatterns
        except ImportError as e:
            print(f"Error importing urls: {e}")
            return []
