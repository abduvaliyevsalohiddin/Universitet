from django.contrib import admin

from .models import *


@admin.register(Ustoz)
class UstozAdmin(admin.ModelAdmin):
    list_display = ["id", "ism", "jins", "yosh", "daraja", "fan"]
    list_display_links = ["id", "ism"]
    search_fields = ["ism"]
    search_help_text = "Ism ustunlari bo'yicha qidiring"


admin.site.register(Yonalish)
admin.site.register(Fan)
# admin.site.register(Ustoz)
