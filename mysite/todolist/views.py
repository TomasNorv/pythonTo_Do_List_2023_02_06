from django.shortcuts import render
from .models import Uzduotis
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
# Create your views here.
def index(request):
    num_Uzduotis = Uzduotis.objects.all().count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    cotext={
        'num_Uzduotis': num_Uzduotis,
        'num_visits': num_visits,
    }
    return render(request,'index.html', context=cotext)
def uzduotys(request):
    uzduotys= Uzduotis.objects.all
    context = {
        'uzduotys': uzduotys
    }
    return render(request, 'uzduotys.html', context=context)


class UserUzduotisListView(LoginRequiredMixin, ListView):
    model = Uzduotis
    template_name = 'user_uzduotys.html'
    context_object_name = 'uzduotys'


    def get_queryset(self):
        return Uzduotis.objects.filter(user=self.request.user)


