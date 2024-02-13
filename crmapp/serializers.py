from rest_framework import serializers
from .models import CRMLed
from .master import MASSlm

class CRMLEDSerializer(serializers.ModelSerializer):
    """CRMLED Serializer"""

    class Meta:
        model = CRMLed
        # fields = __all__

class MASSLMSerializer(serializers.ModelSerializer):
    """MASSLM Serializer"""

    class Meta:
        model = MASSlm
        # fields = __all__