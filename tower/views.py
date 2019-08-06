from django.views.generic import ListView

from rest_framework import viewsets, status, mixins
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from .models import Nuc, Person, DetectedInformation
from .serializers import DetectedInformationSerializer

class NucList(ListView):
    model = Nuc
    context_object_name = 'object_list'

class PersonList(ListView):
    model = Person
    context_object_name = 'object_list'

class PlaceList(ListView):
    model = Nuc
    context_object_name = 'object_list'
    template_name = 'tower/place_list.html'

class DetectedInformationViewset(viewsets.ModelViewSet):
    queryset = DetectedInformation.objects.all()
    serializer_class = DetectedInformationSerializer