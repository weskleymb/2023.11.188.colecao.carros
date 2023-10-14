from django.shortcuts import render, redirect

from carros.models import Carro
from carros.forms import CarroForms

# criar rota para a página inicial
def index(request):
    # criar uma lista de carros
    carros = Carro.objects.all().order_by('-id')
    # criar um dicionário para passar para o template
    return render(request, 'carros/index.html', {'carros': carros})

# criar rota para o formulário de cadastro
def form(request):
    # iniciar o formulário
    form = CarroForms()

    # verificar se o formulário foi enviado
    if request.method == 'POST':
        # preencher o formulário com os dados enviados
        form = CarroForms(request.POST)
        # verificar se os dados são válidos
        if form.is_valid():
            # salvar os dados no banco de dados
            form.save()
            # redirecionar para a página inicial
            return redirect('index')

    # renderizar o template do formulário
    return render(request, 'carros/form.html', {'form': form})

# criar rota para excluir um carro
def delete(request, id):
    # buscar o carro no banco de dados
    carro = Carro.objects.get(id=id)
    # verificar se o carro existe
    if not carro:
        # redirecionar para a página nao encontrado
        return redirect('nao_encontrado')
    # excluir o carro do banco de dados
    carro.delete()
    # redirecionar para a página inicial
    return redirect('index')
