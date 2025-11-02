from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password2 = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'password', 'password2']
        
    def validate_email(self, value):
        if User.objects.filter(email= value).exists():
            raise serializers.ValidationError('User with this email already exits!')
        return value
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Passwords do not matching!')
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['email', 'password']
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        if not email or not password:
            raise serializers.ValidationError('Both email and password required!')
        
        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError('Please input correct email and password!')
        
        attrs['user'] = user
        return attrs

class ProfileSerializer(serializers.ModelSerializer):
    model = User
    fields = ['id', 'firstname', 'lastname', 'email', 'role', 'phone_number', 'created_at', 'updated_at']
