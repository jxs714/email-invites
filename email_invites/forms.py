
from i18nfield.forms import I18nModelForm

from .models import EmailInvitesSettings


class EmailInvitesSettingsForm(I18nModelForm):

    def __init__(self, *args, event=None, **kwargs):
        self.instance, _ = EmailInvitesSettings.objects.get_or_create(event=event)
        super().__init__(*args, **kwargs, instance=self.instance, locales=event.locales)

    class Meta:
        model = EmailInvitesSettings
        fields = ("some_setting", )
        widgets = {}

