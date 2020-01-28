from django.db import models


# Create your models here.
class RecargaCoin(models.Model):
    mes = models.IntegerField()
    qtd_coin_mes = models.IntegerField(default=15)
    
    def __str__(self):
        return str(self.mes)