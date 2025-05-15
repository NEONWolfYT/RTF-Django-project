# Файл маршрутов (URLs) приложения core:

from django.urls import path
from . import views  # Импорт views из текущего приложения

urlpatterns = [
    path('', views.index, name='index'),  # Корневой URL приложения → функция index из views.py
]
