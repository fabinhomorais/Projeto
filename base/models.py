from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Nome: {self.nome} - Email: {self.email}'

class Reserva(models.Model):
    nomeDoPet = models.CharField(max_length=50, verbose_name="Nome do PET")
    telefone = models.CharField(max_length=15)
    dia = models.DateField(verbose_name="Dia da Reserva")
    observacoes = models.TextField(verbose_name="Observações")