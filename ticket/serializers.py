from rest_framework import fields
from rest_framework import serializers
from ticket.models import Ticket

class TicketCreateRequestSerializer(serializers.Serializer):
    """
    Serializer for the Ticket Create API
    """
    user_name = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    user_contact = serializers.CharField(required=True, allow_blank=False, allow_null=False,
        max_length=10, min_length=10)
    timings = serializers.ListField(child=serializers.DateTimeField(),
        allow_empty=False, min_length=1)


class TicketUpdateRequestSerializer(serializers.Serializer):
    """
    Serializer for the Ticket Update API
    """
    ticket_id = serializers.IntegerField(required=True, allow_null=False)
    timing = serializers.DateTimeField(required=True, allow_null=False)


class TicketDeleteRequestSerializer(serializers.Serializer):
    """
    Serializer for the Ticket Delete API
    """
    ticket_id = serializers.IntegerField(required=True, allow_null=False)


class GetTicketResponseSerializer(serializers.ModelSerializer):
    """
    Serializer to the Get Ticket Response 
    """
    class Meta:
        model = Ticket
        fields = ['ticket_id', 'user_name', 'user_contact', 'ticket_time']


class TicketViewRequestSerializer(serializers.Serializer):
    """
    Serializer for the Get A ticket For a particular Time
    """
    ticket_time = serializers.DateTimeField(required=True, allow_null=False)
