from django.contrib import admin

# Register your models here.
from .models import Surah,Ayat,Fraction_ayat


admin.site.register(Surah)
admin.site.register(Ayat)
admin.site.register(Fraction_ayat)