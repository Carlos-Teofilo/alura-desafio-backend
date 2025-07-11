from django.db import models

from desafio.validators import is_valid_cor

class Categoria(models.Model):
    titulo = models.CharField(max_length=100, blank=False, default='livre')
    cor = models.CharField(
        max_length=7,
        blank=False,
        null=False,
        validators=[is_valid_cor],
        default='#2EC27E'
        )

    def __str__(self):
        return self.titulo


class Video(models.Model):
    titulo = models.CharField(max_length=80, blank=False, null=False)
    descricao = models.TextField(null=False, blank=False)
    url = models.TextField(null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.titulo
