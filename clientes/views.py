from django.shortcuts import render, redirect
from .models import Cliente
from .commands import ProcessaUsuarios


def clientes(request):
    if request.method == 'GET':
        clientes_bd = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes_bd})
    
    elif request.method == 'POST':
        processa_post = ProcessaUsuarios(request)
        if processa_post.valida_dados():
            processa_post.salva_cliente()
            processa_post.salva_carro()
            return redirect('clientes')
        else:
            return render(request, 'clientes.html', {'erro': processa_post.erro_msg})
    
    else:
        return render(request, 'clientes.html')
