from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from .serializers import *
from .models import *


class CreateElectronic(APIView):
    @swagger_auto_schema(request_body=ElectrItemSerializer)
    def post(self, request):
        item = request.data.get('item')
        related_home = request.data.get('related_home')
        home = HomeModel.objects.get(id=related_home)
        if home:
            ElectronicItem.objects.create(item=item, related_home=home)
            return Response({"message": "Electronic Added"})
        else:
            return Response({"error": "Home Not Found"})


class ReportCreate(APIView):
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(request_body=ReportSerializer)
    def post(self, request):
        serializer = ReportSerializer(data=request.data)
        home = request.data.get('home')
        if serializer.is_valid():
            homes = HomeModel.objects.get(id=home)
            if home:
                ReportModel.objects.create(home=homes, report_type=serializer.validated_data['report_type'],
                                           report_description=serializer.validated_data['report_description'],
                                           report_file=serializer.validated_data['report_file'])
                return Response({'message': 'Report created successfully'}, status=200)
            else:
                return Response({'message': 'Home not found'}, status=404)
        else:
            return Response({'message': 'Invalid data'}, status=500)


class ReportDelete(APIView):
    @swagger_auto_schema(request_body=DeleteReportSerializer)
    def delete(self, request):
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


class ElectronicsGetView(APIView):
    def get(self, request, id):
        items = ElectronicItem.objects.filter(related_home=id)
        serializer = ElectrItemSerializer(items, many=True)
        if not serializer.data:
            return Response({'message': 'No electronic items found'}, status=404)
        return Response(serializer.data)
