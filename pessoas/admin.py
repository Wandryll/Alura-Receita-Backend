from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ("nome", "email",)
    list_display_links = ("nome", "email",)
    list_per_page = 2
    search_fields = ("nome",)

admin.site.register(Pessoa, ListandoPessoas)

