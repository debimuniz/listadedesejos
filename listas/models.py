from django.db import models


class Lista(models.Model):
    nome = models.CharField(max_length=255)
    item1 = models.CharField(max_length=255)
    item2 = models.CharField(max_length=255)
    item3 = models.CharField(max_length=255)
    item4 = models.CharField(max_length=255)
    item5 = models.CharField(max_length=255)

    def __str__(self):
        return self.nome