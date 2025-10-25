from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import AdminLoginSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi





class AdminLoginView(APIView):


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
