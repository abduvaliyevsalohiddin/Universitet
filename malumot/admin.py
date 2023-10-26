from django.contrib import admin

from .models import *


@admin.register(Ustoz)
class UstozAdmin(admin.ModelAdmin):
    list_display = ["id", "ism", "jins", "yosh", "daraja", "fan"]
    list_display_links = ["id", "ism"]
    search_fields = ["ism"]
    search_help_text = "Ism ustunlari bo'yicha qidiring"

@admin.register(Yonalish)
class YonalishAdmin(admin.ModelAdmin):
    list_display = ["id", "nom", "aktiv"]
    list_display_links = ["id", "nom"]
    search_fields = ["nom"]
    search_help_text = "Nom ustunlari bo'yicha qidiring"
    list_filter = ["aktiv"]


# admin.site.register(Yonalish)
admin.site.register(Fan)
# admin.site.register(Ustoz)
