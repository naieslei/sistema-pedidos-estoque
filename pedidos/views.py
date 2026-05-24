from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedido, ItemPedido
from estoque.models import Produto

@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-criado_em')
    return render(request, 'pedidos/lista.html', {'pedidos': pedidos})

@login_required
def novo_pedido(request):
    if request.method == 'POST':
        produto_id = request.POST['produto']
        quantidade = int(request.POST['quantidade'])
        produto = Produto.objects.get(id=produto_id)
        pedido = Pedido.objects.create(usuario=request.user)
        ItemPedido.objects.create(
            pedido=pedido,
            produto=produto,
            quantidade=quantidade,
            preco_unitario=produto.preco
        )
        produto.quantidade_estoque -= quantidade
        produto.save()
        return redirect('lista_pedidos')
    produtos = Produto.objects.all()
    return render(request, 'pedidos/form.html', {'produtos': produtos})