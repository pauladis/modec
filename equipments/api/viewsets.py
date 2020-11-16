from rest_framework.viewsets import ModelViewSet
from equipments.models import Equipment
from .serializers import EquipmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse

class EquipmentViewSet(ModelViewSet):
    serializer_class = EquipmentSerializer

    def get_queryset(self):
        return Equipment.objects.all()

    def list(self, request, *args, **kwargs):  #GET
        return super(EquipmentViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        vessel = request.query_params.get('vessel', None)
        if vessel:
            request.data['vessel'] = vessel
        return super(EquipmentViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):   #DELETE
        return super(EquipmentViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):  #GET/id
        return super(EquipmentViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):  #PUT
        return super(EquipmentViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):  #PATCH
        return super(EquipmentViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['patch'], detail=False)
    def deactivateEquipment(self, request):
        for i in request.data.get("code"):
            Equipment.objects.filter(code=i).update(status=False)
        return HttpResponse("Os equipamentos foram desativados")

    @action(methods=['patch'], detail=False)
    def activateEquipment(self, request):
        for i in request.data.get("code"):
            Equipment.objects.filter(code=i).update(status=True)
        return HttpResponse("Os equipamentos foram ativados")
