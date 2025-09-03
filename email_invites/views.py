from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView
from pretalx.common.mail import mail
from pretalx.common.models import MailTemplate
from .forms import InvitationForm

class InvitationSendView(FormView):  # Make sure this matches exactly
    template_name = "email_invites/send_invitations.html"
    form_class = InvitationForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["event"] = self.request.event
        return kwargs

    def form_valid(self, form):
        event = self.request.event
        template = form.cleaned_data["template"]
        # Your email sending logic here
        messages.success(self.request, _("Invitations sent successfully!"))
        return redirect("plugins:email_invites:send_invitations")
