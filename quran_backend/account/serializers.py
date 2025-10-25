from rest_framework import serializers
from django.contrib.auth import authenticate

class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        if not user.is_staff:
            raise serializers.ValidationError("Only admin/staff can login here.")
        data['user'] = user
        return data
