from .models import Employee
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .serializer import EmployeeSerializer
from .permissions import IsOwner
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


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


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_token(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'})
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'})
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})


@csrf_exempt
@api_view(["GET"])
def about_user(request):
    last_name = request.user.last_name
    first_name = request.user.first_name
    email = request.user.email
    date_joined = request.user.date_joined
    last_login = request.user.last_login
    data = {"Имя": first_name,
            "Фамилия": last_name,
            "Электронная почта": email,
            "Дата регистрации": date_joined,
            "Был в онлайне": last_login}
    return Response(data)
