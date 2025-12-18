from django.urls import path
from .views import index, projeto_detalhes

urlpatterns = [
    path('', index, name='index'),
    path('projeto/<int:pk>/', projeto_detalhes, name='projeto_detalhes'),
]