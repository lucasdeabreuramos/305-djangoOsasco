from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_pombos(request):
    return render(request, 'pombos.html')

def mostrar_rolezinho(request):
     roles = ['balao', 'shopping', 'quermece', 'calçadao de Osasco', 'SESC', 'Risca faca']
     bairro= 'Rochdale'
     return render(request, 'rolezinho.html', {'roles':roles, 'bairro':bairro})
