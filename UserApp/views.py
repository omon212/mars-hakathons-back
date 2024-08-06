from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .serializers import *


class Register(APIView):
    @swagger_auto_schema(request_body=HomeSerializer)
    def post(self, request):
        serializer = HomeSerializer(data=request.data)
        if serializer.is_valid():
            home_id = random.randint(1000, 9999)
            serializer.validated_data['home_id'] = home_id
            serializer.save()
            response_data = serializer.data
            response_data['home_id'] = home_id
            response_data['id'] = serializer.instance.id
            return Response(response_data, 201)
        return Response(serializer.errors, 400)


class Login(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            home_id = serializer.validated_data['home_id']
            password = serializer.validated_data['password']
            try:
                home = HomeModel.objects.get(home_id=home_id)
                if home.password == password:
                    home_serializer = HomeDatasSRL(home)
                    return Response(home_serializer.data, status=200)
                else:
                    return Response({'msg': 'Invalid Password'}, status=404)
            except HomeModel.DoesNotExist:
                return Response({'msg': 'Home id Not Found'}, status=404)
        else:
            return Response(serializer.errors, status=500)

