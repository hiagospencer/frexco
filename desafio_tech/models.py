from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=20)
    senha = models.CharField(max_length=10, blank=True, null=True)
    data_nascimento = models.DateField(error_messages={'invalid': 'Formato inválido. Dia/Mês/Ano'})

    def __str__(self):
        return self.nome

        