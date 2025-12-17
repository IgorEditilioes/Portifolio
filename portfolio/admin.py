from django.contrib import admin
from .models import Projeto, ImagemProjeto

# Register your models here.
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao', 'link')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo', 'tecnologias')
    list_filter = ('data_criacao',)
    
@admin.register(ImagemProjeto)
class ImagemProjetoAdmin(admin.ModelAdmin):
    list_display = ('projeto', 'imagem')
    search_fields = ('projeto__titulo',)    