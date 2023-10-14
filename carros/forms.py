from django import forms

from carros.models import Carro

# cria um formulário de carro
class CarroForms(forms.ModelForm):

    # define os campos do formulário
    nome = forms.CharField(
        max_length=100, 
        required=True,
        label='Nome:'
    )
    
    marca = forms.CharField(
        max_length=100, 
        required=True,
        label='Marca:'
    )
    
    cor = forms.CharField(
        max_length=100, 
        required=True,
        label='Cor:'
    )
    
    ano_fabricacao = forms.IntegerField(
        required=True,
        label='Ano de Fabricação:'
    )
    
    ano_entrada = forms.IntegerField(
        required=True,
        label='Ano de Entrada:'
    )

    # define o modelo do formulário
    class Meta:
        model = Carro
        fields = ['nome', 'marca', 'cor', 'ano_fabricacao', 'ano_entrada']