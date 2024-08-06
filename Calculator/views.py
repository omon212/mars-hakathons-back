from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from .models import *


class CreateElectronic(APIView):
    @swagger_auto_schema(request_body=ElectrItemSerializer)
    def post(self, request):
        item = request.data.get('item')
        related_home = request.data.get('related_home')

        try:
            home = HomeModel.objects.get(id=related_home)
            ElectronicItem.objects.create(item=item, related_home=home)

            # home_items_list = ElectronicItem.objects.filter(related_home=home)
            # list_items = []
            # for i in home_items_list:
            #     list_items.append(i.item)
            # home_per_hour = 0
            # home_1_day = 0
            #
            #
            # for i in list_items:
            #     home_per_hour += 1 * energy_consumption_per_hour[i]
            #     home_1_day += daily_usage_hours[i] * energy_consumption_per_hour[i]
            # home_30_days = home_1_day * 30
            # home_7_days = home_1_day * 7
            # home_1_year = home_1_day * 365

            return Response({'message': 'Electronic item added successfully'}, status=200)
        except:
            return Response({'message': 'Home not found'}, status=404)


class ReportCreate(APIView):
    @swagger_auto_schema(request_body=ReportSerializer)
    def post(self, request):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            home = HomeModel.objects.get(id=serializer.validated_data['report'])
            if home:
                ReportModel.objects.create(report=home, report_type=serializer.validated_data['report_type'],
                                           report_description=serializer.validated_data['report_description'],
                                           report_file=serializer.validated_data['report_file'])
                return Response({'message': 'Report created successfully'}, status=200)
            else:
                return Response({'message': 'Home not found'}, status=404)
        else:
            return Response({'message': 'Invalid data'}, status=500)


class ReportDelete(APIView):
    @swagger_auto_schema(request_body=DeleteReportSerializer)
    def post(self, request):
        serializer = DeleteReportSerializer(data=request.data)
        if serializer.is_valid():
            report = ReportModel.objects.get(id=serializer.validated_data['report'])
            if report:
                report.delete()
                return Response({'message': 'Report deleted successfully'}, status=200)
            else:
                return Response({'message': 'Report not found'}, status=404)
        else:
            return Response({'message': 'Invalid data'}, status=500)
