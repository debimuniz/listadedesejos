from django.db import models


class Usuario(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    login = models.CharField(
        unique=True,
        max_length=255,
        null=False,
        blank=False
    )

    senha = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    email = models.CharField(
        unique=True,
        max_length=255,
        null=False,
        blank=False
    )

    data_aniversario = models.DateField()

    def __str__(self):
        return self.nome