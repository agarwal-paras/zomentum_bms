# django imports
from django.urls import path

from ticket.views import TicketCreateAPIView, TicketDeleteAPIView, TicketUpdateAPIView

urlpatterns = [
    path('create/',
        TicketCreateAPIView.as_view({"post": "ticket_create"})),
    path('update/',
        TicketUpdateAPIView.as_view({"post": "ticket_update"})),
    path('delete/',
        TicketDeleteAPIView.as_view({"put": "ticket_delete"}))
]
