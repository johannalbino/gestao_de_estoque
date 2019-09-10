from django.forms import ModelForm
from .models import Produtos


class produtosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['codigo_produto', 'nome_produto', 'quantidade', 'validade']