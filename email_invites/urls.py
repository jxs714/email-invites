from django.urls import path

from . import views

app_name = "email_invites"

urlpatterns = [
    path(
        "event/<str:event>/send-invitations/",
        views.InvitationSendView.as_view(),
        name="send_invitations",
    ),
]
