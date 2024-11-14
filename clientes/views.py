from django.shortcuts import render, redirect
from .models import Cliente
from .commands import ProcessaUsuarios
from django.http import JsonResponse
from django.core import serializers
import json

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


def atualiza_cliente(request):
    if request.method == 'GET':
        pass
        
    elif request.method == 'POST':
        # validar se o id do cliente existe
        id_cliente = request.POST.get('id_cliente')
        cliente_bd = Cliente.objects.filter(id=id_cliente)
        
        # muito com o serializers, não o conhecia -> transforma uma model em um json
        cliente_json = json.loads(serializers.serialize('json', cliente_bd))
        cliente_selecionado = cliente_json[0]['fields']
        
        return JsonResponse(cliente_selecionado)