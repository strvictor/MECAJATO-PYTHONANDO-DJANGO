from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Carro


def clientes(request):
    if request.method == 'GET':
        return render(request, 'clientes.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')
        
        valida_cpf = Cliente.objects.filter(cpf=cpf)
        valida_email = Cliente.objects.filter(email=email)
        
        # falta rever essa lógica!
        if valida_cpf.exists() and valida_email.exists():
            return render(request, 'clientes.html', {'erro': 'e-mail ou cpf existentes'})
    
        cliente = Cliente(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            cpf=cpf)
        cliente.save()
        
        relaciona_carros = list(zip(carros, placas, anos))
        for nome_carro, placa, ano in relaciona_carros:
            carro = Carro(
                carro=nome_carro,
                placa=placa,
                ano=ano,
                cliente=cliente)
            carro.save()
        
        return redirect('clientes')
        
    else:
        return render(request, 'clientes.html')
        
        
