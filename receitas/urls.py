from django.urls import path
from receitas.views import index, receita

urlpatterns = [
    path('', index, name='index'),
    path('receita/<int:receita_id>', receita, name='receita')
    
]