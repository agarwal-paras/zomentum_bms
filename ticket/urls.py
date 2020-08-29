# django imports
from django.urls import path

from ticket.views import TicketCreateAPIView, TicketUpdateAPIView

urlpatterns = [
    path('create/',
        TicketCreateAPIView.as_view({"post": "ticket_create"})),
    path('update/',
        TicketUpdateAPIView.as_view({"post": "ticket_update"}))
]
