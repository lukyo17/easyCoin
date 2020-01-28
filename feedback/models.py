from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class Carteira(models.Model):
    pessoa = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    qtd_coin = models.IntegerField(default=0)
    qtd_coin_recebido = models.IntegerField(default=0)

    def __str__(self):
        return self.pessoa.first_name


class Feedback(models.Model):
    remetente = models.ForeignKey(
        Carteira, related_name='feedback_remetente', on_delete=models.CASCADE)
    destino = models.ForeignKey(Carteira, related_name='feedback_destino',
                                on_delete=models.CASCADE, verbose_name="Destinatário :")
    msg = models.TextField(max_length=255, verbose_name="Mensagem :")
    qtd_coin = models.PositiveIntegerField(validators=[MinValueValidator(1)],
        default=0, verbose_name="Quantidade easyCoin")
    data_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.destino.pessoa.first_name