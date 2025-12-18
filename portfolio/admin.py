from django.contrib import admin
from .models import Projeto, ImagemProjeto

# Register your models here.
   
class ProjetoImagemInline(admin.TabularInline):
    model = ImagemProjeto
    extra = 1   
    
@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao', 'link')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo', 'tecnologias')
    list_filter = ('data_criacao',)
    inlines = [ProjetoImagemInline]