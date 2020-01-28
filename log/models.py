from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LogRecarga(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    data_evento = models.DateTimeField(auto_now_add=True)
    evento = models.TextField()
    
    def __str__(self):
        return self.pessoa.first_name