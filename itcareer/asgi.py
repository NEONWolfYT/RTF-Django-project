import os
from django.core.asgi import get_asgi_application # Импорт функции для создания ASGI-приложения Django

# Установка переменной окружения DJANGO_SETTINGS_MODULE.
# Указывает Django, какой модуль настроек использовать (itcareer/settings.py).
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itcareer.settings')

# Создание ASGI-приложения.
# Переменная `application` используется ASGI-сервером для обработки входящих асинхронных запросов.
application = get_asgi_application()