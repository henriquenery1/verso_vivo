from django.db import models
from django.utils import timezone

class Content(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    body = models.TextField(verbose_name='Conteúdo')
    publication_date = models.DateTimeField(default=timezone.now, verbose_name='Data de Publicação')

    def formatted_date(self):
        return self.publication_date.strftime('%d/%m/%Y')