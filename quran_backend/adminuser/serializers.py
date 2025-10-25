from rest_framework import serializers
from .models import Surah,Ayat


# ===========================================================
#   SURAH MODEL SERIALZER
# ===========================================================


class SurahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surah
        fields = [
            'id',
            'surah_number', 
            'surah_name_arabic', 
            'surah_name_malayalam', 
            'surah_name_english'
            ]


class AyatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ayat
        fields=[
            "surah",
            "ayat_number",
            "ayat_text",
            "meaning_text",
            "word_meaning"
        ]