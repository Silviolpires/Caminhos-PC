from django.contrib import admin
from .models import Trilha

@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'distancia', 'duracao', 'nivel_dificuldade', 'data_criacao')
    list_filter = ('nivel_dificuldade', 'data_criacao')
    search_fields = ('nome', 'descricao')
    filter_horizontal = ('guias',)  # Interface mais amigável para o relacionamento ManyToMany
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'descricao', 'distancia', 'duracao', 'nivel_dificuldade')
        }),
        ('Guias', {
            'fields': ('guias',)
        }),
    )