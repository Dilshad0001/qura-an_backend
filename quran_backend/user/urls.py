from django.urls import path
from .import views

urlpatterns = [
    # GET all / POST
    path('surah/', views.SurahAPIView.as_view(), name='user-surah-list'),

    # GET by ID / PATCH / DELETE
    path('surah/<int:surah_id>/', views.SurahDetailAPIView.as_view(), name='user-surah-detail'),

        # GET all / POST
    path('ayat/', views.AyatAPIView.as_view(), name='ayat-list'),

    # # GET by ID / PATCH / DELETE
    # path('ayat/<int:ayat_id>/', views.AyatDetailAPIView.as_view(), name='user-ayat-detail'),
    
    path('fraction-ayat/', views.FractionAyatAPIView.as_view(), name='user-fraction-ayat-list'),
    # path('fraction-ayat/<int:fraction_id>/', views.FractionAyatDetailAPIView.as_view(), name='user-fraction-ayat-detail'),

]
