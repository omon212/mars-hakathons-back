from rest_framework.serializers import ModelSerializer, Serializer
from .models import ElectronicItem, ReportModel


class ElectrItemSerializer(ModelSerializer):
    class Meta:
        model = ElectronicItem
        fields = '__all__'


class ReportSerializer(Serializer):
    class Meta:
        model = ReportModel
        fields = '__all__'
