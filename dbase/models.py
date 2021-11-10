from django.db import models

# Create your models here.

class Cliente(models.Model):
    name = models.CharField(max_length=60)
    cpf= models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    birth = models.DateField()

    def __str__(self):
        return self.name

