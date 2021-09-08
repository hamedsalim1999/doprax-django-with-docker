from django.core.exceptions import ValidationError
from django.contrib.messages import constants 

def validation_title(value):
    if len(value) <= 5:
        raise ValidationError('your lenth is soo short')
def validation_bot(value):
    if len(value) != 0:
        raise ValidationError('i think you are bot if not plese try again ') 
def validator_empty(value):
    if value == None:
        raise('this filed cant be empty')

