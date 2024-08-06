from rest_framework import serializers
from .models import ElectronicItem, ReportModel


class ElectrItemSerializer(serializers.Serializer):
    item = serializers.CharField()
    related_home = serializers.IntegerField()



class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportModel
        fields = ['home', 'report_type', 'report_description', 'report_file']


class DeleteReportSerializer(serializers.Serializer):
    report = serializers.IntegerField()
