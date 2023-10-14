from django.urls import path

from carros.views import index, form, delete

urlpatterns = [
    path('', index, name='index'),
    path('cadastro', form, name='form'),
    path('remover/<int:id>', delete, name='delete'),
]
