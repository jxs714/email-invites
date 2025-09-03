from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView
from pretalx.common.mail import mail
from pretalx.common.models import MailTemplate
from pretalx.person.models import User
from .forms import InvitationForm


class InvitationSendView(FormView):
    template_name = "email_invites/send_invitations.html"
    form_class = InvitationForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["event"] = self.request.event
        return kwargs

    def form_valid(self, form):
        event = self.request.event
        template = form.cleaned_data["template"]
        users = User.objects.filter(
            submissions__event=event,
            submissions__state__in=["submitted", "accepted"],
        ).distinct()

        for user in users:
            context = {
                "event": event,
                "user": user,
                "submissions": user.submissions.filter(event=event),
            }
            mail(
                to=user.email,
                subject=template.subject,
                body=template.text,
                context=context,
                event=event,
            )

        messages.success(self.request, _("Invitations sent successfully!"))
        return redirect("plugins:email_invites:send_invitations")
