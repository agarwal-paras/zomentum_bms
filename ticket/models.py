
from django.db import models
from enum import Enum

class Ticket(models.Model):
    
    ticket_id = models.AutoField(primary_key = True)
    ticket_time = models.DateTimeField('date published')
    user_name = models.CharField(max_length = 20)
    user_contact = models.CharField(max_length = 10)
    
    class Ticket_validate(Enum):
    	Valid = 'VALID'
    	Invalid = 'INVALID'

    ticket_status = models.CharField(max_length = 7, choices = {('Valid', 'VALID'), ('Invalid', 'INVALID')}, default = 'Valid')
