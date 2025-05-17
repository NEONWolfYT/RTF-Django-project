
from django.db import models

class Section(models.Model):
    title = models.CharField(max_length=200)
    html_content = models.TextField(verbose_name='HTML-таблица или описание')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='График (PNG)')

    def __str__(self):
        return self.title
