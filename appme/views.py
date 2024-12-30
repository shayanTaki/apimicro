from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView  # برای استفاده از سریالایزر توکن
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .serializers import CustomTokenObtainPairSerializer, RegistrationRequestSerializer
#احراز هویت و ارسال توکن
@api_view(['POST'])
def obtain_token_pair(request):
    serializer = CustomTokenObtainPairSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#ساخت یوزر توسط ادمین
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_registration_request(request):
    serializer = RegistrationRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)