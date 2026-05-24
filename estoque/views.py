from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria

@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/lista.html', {'produtos': produtos})

@login_required
def novo_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        preco = request.POST['preco']
        quantidade = request.POST['quantidade']
        categoria_id = request.POST['categoria']
        categoria = Categoria.objects.get(id=categoria_id)
        Produto.objects.create(nome=nome, preco=preco, quantidade_estoque=quantidade, categoria=categoria)
        return redirect('lista_produtos')
    categorias = Categoria.objects.all()
    return render(request, 'estoque/form.html', {'categorias': categorias})