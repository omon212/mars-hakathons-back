from rest_framework import serializers
from .models import ElectronicItem, ReportModel


class ElectrItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicItem
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportModel
        fields = '__all__'


class DeleteReportSerializer(serializers.Serializer):
    report = serializers.IntegerField()
