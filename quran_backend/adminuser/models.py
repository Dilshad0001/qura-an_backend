from django.db import models

# Create your models here.


class Surah(models.Model):
    surah_number=models.IntegerField()
    surah_name_arabic=models.CharField(max_length=200)
    surah_name_malayalam=models.CharField(max_length=200,null=True,blank=True)
    surah_name_english=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.surah_name_english



class Ayat(models.Model):
    surah=models.ForeignKey(Surah,on_delete=models.CASCADE)
    ayat_number=models.IntegerField()
    ayat_text=models.TextField(blank=True,null=True)
    meaning_text=models.TextField(blank=True,null=True)
    word_meaning=models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.surah.surah_name_english}-{self.ayat_number} ayat=>{self.ayat_text[:10]}'


class Fraction_ayat(models.Model):
    ayat=models.ForeignKey(Ayat,on_delete=models.CASCADE)
    ayat_fraction_number=models.IntegerField()    
    ayat_fraction_text=models.TextField(blank=True,null=True)
    ayat_fraction_meaning=models.TextField(blank=True,null=True)
    ayat_fraction_tafseer=models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.ayat.ayat_number} ayat of {self.ayat.surah.surah_name_english}=>{self.ayat_fraction_number}- {self.ayat_fraction_text[:10]}'
