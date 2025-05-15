import os
from django.core.wsgi import get_wsgi_application

# Указываем Django, какой файл настроек использовать (itcareer/settings.py)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itcareer.settings')

# Создаем WSGI-приложение для обработки HTTP-запросов
application = get_wsgi_application()