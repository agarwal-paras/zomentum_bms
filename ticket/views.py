from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from ticket.serializers import TicketCreateRequestSerializer
from ticket.serializers import TicketUpdateRequestSerializer
from ticket.serializers import TicketDeleteRequestSerializer
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
                if(Ticket.objects.filter(ticket_time=timing).count() < 20):
                    ticket = Ticket(
                        ticket_time=timing,
                        user_name=user_name,
                        user_contact=user_contact)
                    ticket.save()
                else:
                    raise ValidationError("There are already 20 tickets for timing " + timing)

            response.update(success=True)
            response.update(message="Tickets created successfully")
        except ValidationError as e:
            response.update(error_message=e.detail)
        else:
            status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


class TicketUpdateAPIView(ViewSet):
    """
    Ticket update API to update the timing of a ticket.
    """

    def ticket_update(self, request):
        """
        Ticket Timing Update API
        Args:
            ticket_id: Ticket Id to update.
            timing: New timing for the ticket.
        """
        response = {
            'success': False,
            'message': '',
            'error_messagers': '',
            'data': []
        }

        status_code = status.HTTP_400_BAD_REQUEST

        try:
            validation_serializer = TicketUpdateRequestSerializer(data=request.data)
            validation_serializer.is_valid(raise_exception=True)
            data = validation_serializer.data
            ticket_id = data.get('ticket_id')
            timing = data.get('timing')

            ticket = Ticket.objects.get(ticket_id=ticket_id)
            ticket.ticket_time = timing
            ticket.save()

            response.update(success=True)
            response.update(message="Ticket updated successfully")
        except ValidationError as e:
            response.update(error_message=e.detail)
        except Ticket.DoesNotExist as e:
            response.update(error_message="Ticket does not exist.")
        else:
            status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


class TicketDeleteAPIView(ViewSet):
    """
    Ticket delete API to delete a ticket.
    """

    def ticket_delete(self, request):
        """
        Ticket Timing Delete API
        Args:
            ticket_id: Ticket Id to delete.
        """
        response = {
            'success': False,
            'message': '',
            'error_messages': '',
            'data': []
        }

        status_code = status.HTTP_400_BAD_REQUEST

        try:
            validation_serializer = TicketDeleteRequestSerializer(data=request.data)
            validation_serializer.is_valid(raise_exception=True)
            data = validation_serializer.data
            ticket_id = data.get('ticket_id')

            ticket = Ticket.objects.get(ticket_id=ticket_id)
            ticket.delete()

            response.update(success=True)
            response.update(message="Ticket deleted successfully")
        except ValidationError as e:
            response.update(error_message=e.detail)
        except Ticket.DoesNotExist as e:
            response.update(error_message="Ticket does not exist.")
        else:
            status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
