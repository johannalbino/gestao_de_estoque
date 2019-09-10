from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

# Create your models here.

class Produtos(models.Model):
    codigo_produto = models.IntegerField(_('Código'))
    nome_produto = models.CharField(_('Produto'), max_length=100)
    quantidade = models.DecimalField(_('Quantidade'), max_digits=20, decimal_places=3)
    validade = models.DateField(_('Validade'), auto_now_add=False)

    def __str__(self):
        return str(self.codigo_produto) + ' ' + self.nome_produto