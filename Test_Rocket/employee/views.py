from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .serializer import EmployeeSerializer
from .permissions import IsOwner

# Create your views here.

class EmployeeAPIView(APIView):
    permission_classes = [permissions.IsAdminUser, IsOwner]

    def get(self, request):
        objects = Employee.objects.all()
        serializer = EmployeeSerializer(objects, many=True)
        return Response(serializer.data)


class GetLevelAPIView(APIView):
    permission_classes = [permissions.IsAdminUser, IsOwner]

    def get(self, request, level):
        objects = Employee.objects.filter(level=level)
        serializer = EmployeeSerializer(objects, many=True)
        return Response(serializer.data)