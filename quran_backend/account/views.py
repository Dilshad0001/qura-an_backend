from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import AdminLoginSerializer,AdminRegisterSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi





class AdminLoginView(APIView):
    permission_classes=[]


    @swagger_auto_schema(
        request_body=AdminLoginSerializer,
        responses={
            200: openapi.Response(
                description="Admin login successful",
                examples={
                    "application/json": {
                        "message": "login successful",
                        "token": "b8b23f8c3df0...",
                        "user": {
                            "id": 1,
                            "username": "admin",
                            "email": "admin@example.com"
                        }
                    }
                }
            ),
            400: "Invalid credentials or non-admin user"
        },
        operation_description="Login endpoint for admin/staff users"
    )


    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'login successful',
                'token': token.key,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                }
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# =================================================
# ADMIN REGISTRATION VIEW
# ===================================================

class AdminRegisterView(APIView):
    permission_classes = []

    @swagger_auto_schema(
        request_body=AdminRegisterSerializer,
        responses={
            201: openapi.Response(
                description="Admin registration successful",
                examples={
                    "application/json": {
                        "message": "registration successful",
                        "token": "b8b23f8c3df0...",
                        "user": {
                            "id": 1,
                            "username": "admin",
                            "email": "admin@example.com"
                        }
                    }
                }
            ),
            400: "Invalid input or user already exists"
        },
        operation_description="Register a new admin/staff user"
    )
    def post(self, request):
        serializer = AdminRegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Create user
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                is_staff=True  # make it admin/staff user
            )
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'registration successful',
                'token': token.key,
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)