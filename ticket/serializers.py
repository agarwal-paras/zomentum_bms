from rest_framework import fields
from rest_framework import serializers

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
