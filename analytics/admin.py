
from django.contrib import admin
from .models import Section

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
