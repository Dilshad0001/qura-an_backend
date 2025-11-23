from rest_framework import serializers
from .models import Surah,Ayat,Fraction_ayat


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
            "id",
            "surah",
            "ayat_number",
            "ayat_text",
            "meaning_text",
            "word_meaning"
        ]



    def to_representation(self, instance):
        data = super().to_representation(instance)

        # 👉 Add full surah details inside the ayat response
        data["surah_detail"] = {
            "id": instance.surah.id,
            "number": instance.surah.surah_number,
            "arabic": instance.surah.surah_name_arabic,
            "malayalam": instance.surah.surah_name_malayalam,
            "english": instance.surah.surah_name_english,
        }

        return data


class FractionAyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fraction_ayat
        fields = [
            "id",
            "ayat",
            "ayat_fraction_number",
            "ayat_fraction_text",
            "ayat_fraction_meaning",
            "ayat_fraction_tafseer"
        ]
