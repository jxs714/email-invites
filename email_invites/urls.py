from django.urls import path
from . import views

app_name = "email_invites"

urlpatterns = [
    path("send-invitations/", views.InvitationSendView.as_view(), name="send_invitations"),
]
