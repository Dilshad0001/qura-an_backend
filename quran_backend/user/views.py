from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from adminuser.models import Surah,Fraction_ayat
from adminuser .serializers import SurahSerializer,AyatSerializer,FractionAyatSerializer
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
        tags=["user"]
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
    


# ===========================================================
# SURAH DETAIL VIEW (GET by ID )
# ===========================================================
class SurahDetailAPIView(APIView):

    # ---------------- GET BY ID ----------------
    @swagger_auto_schema(
        responses={200: SurahSerializer()},
        operation_summary="Get a Surah by ID",
        tags=["user"]
    )
    def get(self, request, surah_id):
        surah = get_object_or_404(Surah, id=surah_id)
        serializer = SurahSerializer(surah)
        return Response(serializer.data, status=status.HTTP_200_OK)   
    
     
    
from adminuser.models import Ayat

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
        tags=["user"]
    )
    def get(self, request):
        surah_id = request.GET.get('surah_id')
        if surah_id:
            ayats = Ayat.objects.filter(surah_id=surah_id)
        else:
            ayats = Ayat.objects.all()
        serializer = AyatSerializer(ayats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    

# from adminuser. serializers import AyatSerializer

# ===========================================================
# AYAT DETAIL VIEW (GET by ID / PATCH / DELETE)
# ===========================================================

# class AyatDetailAPIView(APIView):
#     """
#     GET, PATCH, DELETE Ayat by ID
#     """

#     # ---------------- GET BY ID ----------------
#     @swagger_auto_schema(
#         responses={200: AyatSerializer()},
#         operation_summary="Get Ayat by ID",
#         tags=["Ayat"]
#     )
#     def get(self, request, ayat_id):
#         ayat = get_object_or_404(Ayat, id=ayat_id)
#         serializer = AyatSerializer(ayat)
#         return Response(serializer.data, status=status.HTTP_200_OK)    





# ===========================================================
# FRACTION AYAT MANAGEMENT VIEW
# ===========================================================

class FractionAyatAPIView(APIView):
    """
    GET all fraction ayats or filter by ayat_id
    POST new fraction ayat
    """

    # ---------------- GET ALL / FILTER BY AYAT ----------------
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'ayat_id',
                openapi.IN_QUERY,
                description="Filter fraction ayats by Ayat ID",
                type=openapi.TYPE_INTEGER,
                required=False
            )
        ],
        responses={200: FractionAyatSerializer(many=True)},
        operation_summary="Get all Fraction Ayats or filter by Ayat ID",
        tags=["Fraction Ayat"]
    )
    def get(self, request):
        ayat_id = request.GET.get('ayat_id')
        if ayat_id:
            fractions = Fraction_ayat.objects.filter(ayat_id=ayat_id)
        else:
            fractions = Fraction_ayat.objects.all()
        serializer = FractionAyatSerializer(fractions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)