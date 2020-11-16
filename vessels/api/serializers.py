from rest_framework.serializers import ModelSerializer
from vessels.models import Vessel

class VesselSerializer(ModelSerializer):
    class Meta:
        model = Vessel
        fields = ('code', 'descricao')