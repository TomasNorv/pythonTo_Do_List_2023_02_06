from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("uzduotys/", views.uzduotys, name= "sukurtos_užduotys"),
    path('useruzduotys/', views.UserUzduotisListView.as_view(), name = 'user_užduotys'),
]