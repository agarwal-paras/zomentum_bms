from datetime import datetime, timezone
from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from ticket.serializers import GetTicketResponseSerializer
from ticket.serializers import TicketCreateRequestSerializer
from ticket.serializers import TicketDeleteRequestSerializer
from ticket.serializers import TicketUpdateRequestSerializer
from ticket.serializers import TicketViewRequestSerializer
from ticket.models import Ticket

class TicketCreateAPIView(ViewSet):
    """
    Ticket Create API to create tickets for a user for different timings.
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
            'error_messages': '',
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


class GetTicketAPIView(ViewSet):
    """
    Get Ticket API to Get the information of a user for who booked the ticket of a particular ticket id.
    """

    def get_ticket(self, request, ticket_id):
        """
        Get Ticket API
        Args:
            ticket_id: Ticket ID 
        """

        response = {
            'success': False,
            'message': '',
            'error_messages': '',
            'data': []
        }

        status_code = status.HTTP_400_BAD_REQUEST

        try:
            ticket = Ticket.objects.get(ticket_id=ticket_id)            
            response_serializer = GetTicketResponseSerializer(ticket)
            response.update(data=response_serializer.data)
        except Ticket.DoesNotExist as e:
            response.update(error_message='Ticket Does Not Exist')
        except ValidationError as e:
            response.update(error_message=e.detail)
        else:
            status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
    
    def view_ticket(self, request):
        """    
        Get Ticket API
        Args:
            ticket_time: Ticket time of booking 
        
        """
        response = {
            'success': False,
            'message': '',
            'error_messages': '',
            'data': []
        }

        status_code = status.HTTP_400_BAD_REQUEST

        try:
            validation_serializer = TicketViewRequestSerializer(data=request.query_params)
            validation_serializer.is_valid(raise_exception=True)
            
            data = validation_serializer.data
            ticket_time = data.get('ticket_time')
            tickets = Ticket.objects.filter(ticket_time=ticket_time)            
            ticket_serializer = GetTicketResponseSerializer(tickets, many=True)
            response.update(data=ticket_serializer.data)
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


class TicketExpireAPIView(ViewSet):
    """
    Ticket expire API to expire a ticket if later than 8 hours.
    """

    def ticket_expire(self, request):
        """
        Ticket Timing Expire API
        Args:
            ticket_id: Ticket Id to expire.
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
            current_time = datetime.now(timezone.utc)
            difference = current_time - ticket.ticket_time

            if difference.seconds >= 0 * 60 * 60:
                ticket.ticket_status = 'Invalid'
                ticket.save()
            else:
                raise ValidationError("Ticket cannot be expired")

            response.update(success=True)
            response.update(message="Ticket expired successfully")
        except ValidationError as e:
            response.update(error_message=e.detail)
        except Ticket.DoesNotExist as e:
            response.update(error_message="Ticket does not exist.")
        else:
            status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
