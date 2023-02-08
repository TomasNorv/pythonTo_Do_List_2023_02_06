from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Uzduotis(models.Model):
    text = models.TextField(verbose_name='Užduoties pavadinimas', max_length=200, help_text='Įveskite užduoties pavadinimą(pvz. išplauti grindis)')
    user = models.ForeignKey(to=User, verbose_name='Vartotojas', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(verbose_name='laikas', auto_now_add=True)
    def __str__(self):
        return f"{self.text}"
    class Meta:
        verbose_name = "Užduotis"
        verbose_name_plural ='Užduotys'





