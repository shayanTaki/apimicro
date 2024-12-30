from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import RegistrationRequest
from django.contrib.auth.hashers import make_password


#برای تهیه توکن
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # token['username'] = user.username
        return token
#برای اضافه کردن یوزر
class RegistrationRequestSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(write_only=True)
    admin_username = serializers.CharField(write_only=True)
    admin_password = serializers.CharField(write_only=True)

    class Meta:
        model = RegistrationRequest
        fields = ['admin_username', 'admin_password', 'new_username', 'new_password']


#احراز اینکه ادمین هست یا ن
    def validate(self, data):
        admin_username = data.get('admin_username')
        admin_password = data.get('admin_password')
        new_username = data.get('new_username')

        admin_user = authenticate(username=admin_username, password=admin_password)
        if not admin_user or not admin_user.is_staff:
            raise serializers.ValidationError("Invalid admin credentials.")

        if User.objects.filter(username=new_username).exists():
            raise serializers.ValidationError("Username already exists.")

        return data
#ساخت نهایی که در صورت درست بودن سمت ویو ذخیره میشود آپجکت ساخته شده
    def create(self, validated_data):
        admin_user = User.objects.get(username=validated_data['admin_username'])
        new_user = User.objects.create_user(username=validated_data['new_username'], password=validated_data['new_password'])
        registration_request = RegistrationRequest.objects.create(
            admin_user=admin_user,
            new_username=validated_data['new_username'],
            new_password=make_password(validated_data['new_password'])
        )
        return registration_request