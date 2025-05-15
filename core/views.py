# Обработчик главной страницы приложения:

from django.shortcuts import render

def index(request):
    # Рендерит шаблон base.html и возвращает его как HTTP-ответ
    return render(request, 'base.html') 
