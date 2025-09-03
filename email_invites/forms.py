from django import forms
from django.utils.translation import gettext_lazy as _
from pretalx.common.models import MailTemplate

class InvitationForm(forms.Form):
    template = forms.ModelChoiceField(
        queryset=MailTemplate.objects.none(),
        label=_("Email Template"),
        empty_label=None,
    )

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop("event")
        super().__init__(*args, **kwargs)
        self.fields["template"].queryset = MailTemplate.objects.filter(event=self.event)
