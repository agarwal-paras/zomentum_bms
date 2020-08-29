# django imports
from django.urls import path
from ticket.views import GetTicketAPIView 
from ticket.views import TicketCreateAPIView, TicketDeleteAPIView
from ticket.views import TicketExpireAPIView, TicketUpdateAPIView

urlpatterns = [
    path('create/',
        TicketCreateAPIView.as_view({"post": "ticket_create"})),
    path('update/',
        TicketUpdateAPIView.as_view({"post": "ticket_update"})),
    path('delete/',
        TicketDeleteAPIView.as_view({"put": "ticket_delete"})),
    path('expire/',
        TicketExpireAPIView.as_view({"post": "ticket_expire"})),
    path('get/<ticket_id>',
    	GetTicketAPIView.as_view({"get": "get_ticket"})),
    path('get/',
    	GetTicketAPIView.as_view({"get": "view_ticket"}))
]
