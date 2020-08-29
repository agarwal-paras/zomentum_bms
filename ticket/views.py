from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from ticket.serializers import TicketCreateRequestSerializer
from ticket.models import Ticket

class TicketCreateAPIView(ViewSet):
    """
    Ticket Create API to craete tickets for a user for different timings.
    """

    def ticket_create(self, request):
        """
        Ticket create API
        Args:
            user_name: User name
            user_contact: User contact
            timings: [Timings of tickets]
        """

        response = {
            'success': False,
            'message': '',
            'error_messagers': '',
            'data': []
        }

        status_code = status.HTTP_400_BAD_REQUEST

        try:
            validation_serializer = TicketCreateRequestSerializer(data=request.data)
            validation_serializer.is_valid(raise_exception=True)
            data = validation_serializer.data
            user_name = data.get('user_name')
            user_contact = data.get('user_contact')

            for timing in data.get('timings'):
                ticket = Ticket(
                    ticket_time=timing,
                    user_name=user_name,
                    user_contact=user_contact)
                ticket.save()

            response.update(success=True)
            response.update(message="Tickets created successfully")
        except ValidationError as e:
            response.update(error_message=e.detail)
        else:
            status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
