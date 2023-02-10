from django.shortcuts import render, reverse
from .models import Uzduotis
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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

class UserUzduotisCreateView(LoginRequiredMixin, CreateView):
    model = Uzduotis
    fields = ['text']
    template_name = 'user_uzduotys_form.html'

    def get_success_url(self):
        return reverse('user_užduotys')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class UserUzduotisUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Uzduotis
    fields = ['text']
    template_name = 'user_uzduotys_form.html'

    def get_success_url(self):
        return reverse('user_užduotys')
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def test_func(self):
        uzduotis = self.get_object()
        return self.request.user == uzduotis.user

class UserUzduotisDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Uzduotis
    fields = ['text']
    template_name = 'user_uzduotys_delete.html'
    context_object_name = 'uzduotis'

    def get_success_url(self):
        return reverse('user_užduotys')

    def test_func(self):
        uzduotis = self.get_object()
        return self.request.user == uzduotis.user