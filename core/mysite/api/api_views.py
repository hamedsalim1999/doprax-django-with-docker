
from rest_framework import viewsets
from .serializers import Contactserializers
from ..models import Contact


class ContactAPI_List(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = Contactserializers
