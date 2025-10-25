from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Surah
from .serializers import SurahSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# ===========================================================
# SURAH MANAGEMENT VIEW
# ===========================================================
class SurahAPIView(APIView):
    """
    => GET all surahs or search by name
    => GET surah by ID
    => POST surah
    => PATCH surah by ID
    => DELETE surah by ID
    """

    # ---------------- GET ALL / SEARCH ----------------
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'search',
                openapi.IN_QUERY,
                description="Search by Arabic, Malayalam, or English surah name",
                type=openapi.TYPE_STRING,
                required=False
            )
        ],
        responses={200: SurahSerializer(many=True)},
        operation_summary="Get all Surahs or search by name",
        tags=["Surah"]
    )
    def get(self, request):
        search = request.GET.get('search')
        if search:
            surahs = Surah.objects.filter(
                surah_name_arabic__icontains=search
            ) | Surah.objects.filter(
                surah_name_malayalam__icontains=search
            ) | Surah.objects.filter(
                surah_name_english__icontains=search
            )
        else:
            surahs = Surah.objects.all()

        serializer = SurahSerializer(surahs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ---------------- POST ----------------
    @swagger_auto_schema(
        request_body=SurahSerializer,
        responses={201: SurahSerializer()},
        operation_summary="Create a new Surah",
        tags=["Surah"]
    )
    def post(self, request):
        serializer = SurahSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ===========================================================
# SURAH DETAIL VIEW (GET by ID / PATCH / DELETE)
# ===========================================================
class SurahDetailAPIView(APIView):

    # ---------------- GET BY ID ----------------
    @swagger_auto_schema(
        responses={200: SurahSerializer()},
        operation_summary="Get a Surah by ID",
        tags=["Surah"]
    )
    def get(self, request, surah_id):
        surah = get_object_or_404(Surah, id=surah_id)
        serializer = SurahSerializer(surah)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ---------------- PATCH ----------------
    @swagger_auto_schema(
        request_body=SurahSerializer,
        responses={200: SurahSerializer()},
        operation_summary="Update a Surah partially",
        tags=["Surah"]
    )
    def patch(self, request, surah_id):
        surah = get_object_or_404(Surah, id=surah_id)
        serializer = SurahSerializer(surah, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ---------------- DELETE ----------------
    @swagger_auto_schema(
        responses={204: "Surah deleted successfully"},
        operation_summary="Delete a Surah by ID",
        tags=["Surah"]
    )
    def delete(self, request, surah_id):
        surah = get_object_or_404(Surah, id=surah_id)
        surah.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    # ---------------- DELETE ----------------
    @swagger_auto_schema(
        responses={204: "Surah deleted successfully"},
        operation_summary="Delete a Surah by ID",
        operation_description="Permanently delete a Surah by its ID",
        tags=["Surah"]
    )
    def delete(self, request, surah_id):
        surah = get_object_or_404(Surah, id=surah_id)
        surah.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Ayat, Surah
from .serializers import AyatSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# ===========================================================
# AYAT MANAGEMENT VIEW
# ===========================================================

class AyatAPIView(APIView):
    """
    GET all ayats or filter by surah_id
    POST new ayat
    """

    # ---------------- GET ALL / FILTER BY SURAH ----------------
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'surah_id',
                openapi.IN_QUERY,
                description="Filter ayats by Surah ID",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: AyatSerializer(many=True)},
        operation_summary="Get all Ayats or filter by Surah ID",
        tags=["Ayat"]
    )
    def get(self, request):
        surah_id = request.GET.get('surah_id')
        if surah_id:
            ayats = Ayat.objects.filter(surah_id=surah_id)
        else:
            ayats = Ayat.objects.all()
        serializer = AyatSerializer(ayats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ---------------- POST ----------------
    @swagger_auto_schema(
        request_body=AyatSerializer,
        responses={201: AyatSerializer()},
        operation_summary="Create a new Ayat",
        tags=["Ayat"]
    )
    def post(self, request):
        serializer = AyatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ===========================================================
# AYAT DETAIL VIEW (GET by ID / PATCH / DELETE)
# ===========================================================

class AyatDetailAPIView(APIView):
    """
    GET, PATCH, DELETE Ayat by ID
    """

    # ---------------- GET BY ID ----------------
    @swagger_auto_schema(
        responses={200: AyatSerializer()},
        operation_summary="Get Ayat by ID",
        tags=["Ayat"]
    )
    def get(self, request, ayat_id):
        ayat = get_object_or_404(Ayat, id=ayat_id)
        serializer = AyatSerializer(ayat)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ---------------- PATCH ----------------
    @swagger_auto_schema(
        request_body=AyatSerializer,
        responses={200: AyatSerializer()},
        operation_summary="Update Ayat partially",
        tags=["Ayat"]
    )
    def patch(self, request, ayat_id):
        ayat = get_object_or_404(Ayat, id=ayat_id)
        serializer = AyatSerializer(ayat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ---------------- DELETE ----------------
    @swagger_auto_schema(
        responses={204: "Ayat deleted successfully"},
        operation_summary="Delete Ayat by ID",
        operation_description="Permanently delete an Ayat by its ID",
        tags=["Ayat"]
    )
    def delete(self, request, ayat_id):
        ayat = get_object_or_404(Ayat, id=ayat_id)
        ayat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
