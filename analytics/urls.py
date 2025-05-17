
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('statistics/', views.statistics, name='statistics'),
    path('demand/', views.demand, name='demand'),
    path('geo/', views.geo, name='geo'),
    path('skills/', views.skills, name='skills'),
    path('vacancies/', views.vacancies, name='vacancies'),
]
