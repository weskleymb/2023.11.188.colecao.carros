from django.db import models

# cria um modelo de carro
class Carro(models.Model):

    # define os atributos do modelo
    nome = models.CharField(
        max_length=100, 
        null=False,
        blank=False
    )
    
    marca = models.CharField(
        max_length=100, 
        null=False,
        blank=False
    )
    
    cor = models.CharField(
        max_length=100, 
        null=False,
        blank=False
    )
    
    ano_fabricacao = models.IntegerField(
        null=False,
        blank=False
    )
    
    ano_entrada = models.IntegerField(
        null=False,
        blank=False
    )

    # define como o objeto será exibido
    def __str__(self):
        return self.nome
