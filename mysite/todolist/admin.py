from django.contrib import admin
from .models import Uzduotis
# Register your models here.


class UzduotisAdmin(admin.ModelAdmin):
    list_display = ("text",'user', "created")


admin.site.register(Uzduotis,UzduotisAdmin)

