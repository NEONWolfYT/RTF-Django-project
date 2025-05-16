# Импорт необходимых модулей
import os
from pathlib import Path  # Для работы с путями в файловой системе

# Базовый путь проекта (корневая директория)
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ для подписи данных. В реальных проектах должен храниться в .env!
SECRET_KEY = 'your-secret-key'  # Замените на уникальное значение в production⚠️

# Режим отладки. В продакшене должно быть False!
DEBUG = True  #  Отключает детализированные ошибки. Не использовать в production⚠️

# Разрешенные хосты. ['*'] разрешает все хосты (опасно для продакшена!)
ALLOWED_HOSTS = ['*']  # в production надо будет указать конкретные значения доменов⚠️

# Установленные приложения проекта
INSTALLED_APPS = [
    'django.contrib.admin',       # Админ-панель
    'django.contrib.auth',        # Система аутентификации
    'django.contrib.contenttypes',# Модели контента
    'django.contrib.sessions',    # Сессии
    'django.contrib.messages',    # Сообщения
    'django.contrib.staticfiles', # Статические файлы
    'core',                       # Пользовательское приложение
]

# Промежуточные слои (обрабатывают запросы и ответы)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',       # Безопасность
    'django.contrib.sessions.middleware.SessionMiddleware',# Управление сессиями
    'django.middleware.common.CommonMiddleware',           # Базовая обработка запросов
    'django.middleware.csrf.CsrfViewMiddleware',           # Защита от CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',# Аутентификация
    'django.contrib.messages.middleware.MessageMiddleware',# Работа с сообщениями
    'django.middleware.clickjacking.XFrameOptionsMiddleware',# Защита от clickjacking
]

# Корневой модуль URL-конфигурации
ROOT_URLCONF = 'itcareer.urls'

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Движок шаблонов
        'DIRS': [BASE_DIR / 'templates'],  # Директории для поиска шаблонов
        'APP_DIRS': True,  # Искать шаблоны в подпапках templates приложений
        'OPTIONS': {
            'context_processors': [  # Контекстные процессоры
                'django.template.context_processors.debug',    # Переменные для отладки
                'django.template.context_processors.request',  # Добавляет объект request
                'django.contrib.auth.context_processors.auth', # Данные аутентификации
                'django.contrib.messages.context_processors.messages', # Сообщения
            ],
        },
    },
]

# WSGI-приложение для развертывания
WSGI_APPLICATION = 'itcareer.wsgi.application'

# Настройки баз данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Используется SQLite
        'NAME': BASE_DIR / 'db.sqlite3',         # Путь к файлу БД
    }
}

# Валидаторы паролей (с пустым списком проверок нет)
AUTH_PASSWORD_VALIDATORS = []  #  В production добавить валидаторы⚠️

# Локализация
LANGUAGE_CODE = 'ru-ru'   # Язык интерфейса (русский)
TIME_ZONE = 'UTC'         # Часовой пояс (UTC)
USE_I18N = True           # Включение интернационализации
USE_TZ = True             # Использовать часовые пояса

# Настройки статических файлов (CSS, JS, изображения)
STATIC_URL = '/static/'   # URL-префикс для статики
STATICFILES_DIRS = [BASE_DIR / 'static']  # Директории со статическими файлами

# Настройки медиафайлов (загруженные пользователями)
MEDIA_URL = '/media/'     # URL-префикс для медиа
MEDIA_ROOT = BASE_DIR / 'media'  # Директория для хранения медиа

# Тип автоинкрементного поля по умолчанию
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'