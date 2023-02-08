from django.shortcuts import render
from .models import Uzduotis
# Create your views here.
def index(request):
    num_Uzduotis = Uzduotis.objects.all().count()

    cotext={
        'num_Uzduotis': num_Uzduotis,
    }
    return render(request,'index.html', context=cotext)


