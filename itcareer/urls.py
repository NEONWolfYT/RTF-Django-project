# Настройка URL-маршрутов Django:

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),          # Маршрут для админ-панели
    path('', include('core.urls')),           # Подключение URL-ов из приложения 'core' (корневой путь)
] 

# Добавление обработки медиа-файлов в режиме разработки:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
