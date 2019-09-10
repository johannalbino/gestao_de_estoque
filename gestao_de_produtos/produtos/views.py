from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtos
from .forms import produtosForm
# Create your views here.


def index(request):
    template_name = 'index.html'
    context = {}
    context['produtos'] = Produtos.objects.all()

    return render(request, template_name, context)


def novo(request):
    template_name = 'novo.html'
    form = produtosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {"formProduto": form})

def editar(request, id):
    template_name = 'novo.html'
    produto = get_object_or_404(Produtos, pk=id)
    form = produtosForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, template_name, {"formProduto": form})

def excluir(request, id):
    produto = get_object_or_404(Produtos, pk=id)
    produto.delete()

    return render(request, 'index.html')