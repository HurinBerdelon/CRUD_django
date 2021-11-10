from django.shortcuts import render, redirect

from . import models

def clientes(request):

    if request.method == 'POST':
        nome = request.POST.getlist('nome')
        email = request.POST.getlist('email')
        cpf = request.POST.getlist('cpf')
        birth = request.POST.getlist('birth')
        models.Cliente(name=nome[0], birth=birth[0], email = email[0], cpf = cpf[0]).save()

        return redirect('clientes')       

    list_of_clients = models.Cliente.objects.all()

    context = {'list_of_clients': list_of_clients}

    return render(request, 'dbase/clientes.html', context)

def client_by_id(request, id):
    client = models.Cliente.objects.get(id = id)

    if request.method == 'POST':
        client.delete()

        return redirect('clientes')

    context = {'client': client}

    return render(request, 'dbase/client_id.html', context)

def editar(request, id):
    client = models.Cliente.objects.get(id = id)

    if request.method == 'POST':
        nome = request.POST.getlist('nome')
        email = request.POST.getlist('email')
        cpf = request.POST.getlist('cpf')
        birth = request.POST.getlist('birth')

        client.name = nome[0]
        client.email = email[0]
        client.cpf = cpf[0]
        client.birth = birth[0]

        client.save()

        return redirect('clientes')

    context = {'client': client}

    return render(request, 'dbase/editar.html', context)