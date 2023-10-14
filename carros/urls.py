from django.urls import path

from carros.views import index, form, delete, edit, nao_encontrado

urlpatterns = [
    path('', index, name='index'),
    path('nao_encontrado', nao_encontrado, name='nao_encontrado'),
    path('cadastro', form, name='form'),
    path('remover/<int:id>', delete, name='delete'),
    path('editar/<int:id>', edit, name='edit'),
]
