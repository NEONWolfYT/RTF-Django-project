
from django.shortcuts import render
from .models import Section

def index(request):
    section = Section.objects.filter(title__icontains='Главная').first()
    return render(request, 'analytics/page.html', {'section': section, 'page': 'Главная'})

def statistics(request):
    section = Section.objects.filter(title__icontains='Статистика').first()
    return render(request, 'analytics/page.html', {'section': section, 'page': 'Общая статистика'})

def demand(request):
    section = Section.objects.filter(title__icontains='Востребованность').first()
    return render(request, 'analytics/page.html', {'section': section, 'page': 'Востребованность'})

def geo(request):
    section = Section.objects.filter(title__icontains='География').first()
    return render(request, 'analytics/page.html', {'section': section, 'page': 'География'})

def skills(request):
    section = Section.objects.filter(title__icontains='Навыки').first()
    return render(request, 'analytics/page.html', {'section': section, 'page': 'Навыки'})

def vacancies(request):
    # Пока заглушка
    return render(request, 'analytics/vacancies.html')
