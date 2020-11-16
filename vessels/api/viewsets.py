from rest_framework.viewsets import ModelViewSet
from vessels.models import Vessel
from equipments.models import Equipment
from .serializers import VesselSerializer
from rest_framework.decorators import action
from django.http import HttpResponse
from django.core import serializers

class VesselViewSet(ModelViewSet):
    serializer_class = VesselSerializer

    def get_queryset(self):
        return Vessel.objects.all()


    @action(methods=['get'], detail=True)
    def equipment(self, request, pk=None):
        data = Equipment.objects.filter(vessel=pk).filter(status=True)
        response = serializers.serialize("json", data, fields=('name', 'code', 'location', 'vessel'))
        return HttpResponse(response, content_type='application/json')