from django.db import models
from django.utils import timezone

class Content(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    body = models.TextField(verbose_name='Conteúdo do texto')
    author = models.CharField(max_length=100, verbose_name='Autor')
    publication_date = models.DateTimeField(default=timezone.now, verbose_name='Data de Publicação')

    def set_publication_date(self):
        self.publication_date = timezone.now()
        super().save()