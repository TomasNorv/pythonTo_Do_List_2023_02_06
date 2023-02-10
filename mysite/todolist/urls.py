from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("uzduotys/", views.uzduotys, name= "sukurtos_užduotys"),
    path('useruzduotys/', views.UserUzduotisListView.as_view(), name = 'user_užduotys'),
    path('useruzduotys/created', views.UserUzduotisCreateView.as_view(), name = 'user_užduotį_sukurti'),
    path('useruzduotys/<int:pk>/update', views.UserUzduotisUpdateView.as_view(), name='user_užduotį_redaguoti'),
    path('useruzduotys/<int:pk>/delete', views.UserUzduotisDeleteView.as_view(), name='user_užduotį_ištrinti'),

]