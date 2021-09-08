from rest_framework import serializers
from ..models import Contact


class Contactserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields =  '__all__'
