from django import forms
from .models import Contact
from .form_validation import validation_title,validation_bot,validator_empty
from django.core.exceptions import ValidationError
from django.contrib.messages import constants 
from django.shortcuts import redirect


class ContactUs(forms.ModelForm):
    title = forms.CharField(
    max_length=256 , 
    validators = [validation_title , validator_empty] )
    email = forms.EmailField( validators = [validation_title , validator_empty] )
    body = forms.CharField( validators = [validation_title , validator_empty] )
    name = forms.CharField(max_length=256, validators = [validation_title , validator_empty] )
    bot = forms.CharField(required = False,widget = forms.HiddenInput,validators = [validation_bot] )



    def __init__(self, *args, **kwargs):
        super(ContactUs, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
        "type":"text" ,
        "class":"form-control w-100" ,
        "value":"",
        "placeholder":"Username",
        })
        self.fields['body'].widget.attrs.update({
        "type":"text" ,
        "class":"form-control w-100" ,
        "value":"",
        "placeholder":"Username",
        })
        self.fields['email'].widget.attrs.update({
        "type":"text" ,
        "class":"form-control w-100" ,
        "value":"",
        "placeholder":"Username",
        })
        self.fields['title'].widget.attrs.update({
        "type":"text" ,
        "class":"form-control w-100" ,
        "value":"",
        "placeholder":"Username",
        })
    class Meta:
        model= Contact
        fields = ['title','email','body','name']