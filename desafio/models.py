from django.db import models


class Video(models.Model):
    titulo = models.CharField(max_length=80, blank=False, null=False)
    descricao = models.TextField(null=False, blank=False)
    url = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.titulo
    