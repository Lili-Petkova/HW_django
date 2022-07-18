from django.contrib import admin

from .models import Log


@admin.register(Log)
class GenreModelAdmin(admin.ModelAdmin):
    list_display = ["path", "method", "timestamp"]
