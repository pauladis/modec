from rest_framework.serializers import ModelSerializer
from equipments.models import Equipment
from vessels.api.serializers import VesselSerializer

class EquipmentSerializer(ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('name', 'code', 'location','vessel')