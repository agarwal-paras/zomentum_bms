# django imports
from django.urls import path

from ticket.views import TicketCreateAPIView

urlpatterns = [
    path('create/',
        TicketCreateAPIView.as_view({"post": "ticket_create"}),
        name='ticket_create')
]
