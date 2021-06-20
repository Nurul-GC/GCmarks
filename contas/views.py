from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from contas.forms import LoginForm


# Create your views here.
def inicio(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            usuario = authenticate(request, username=cd['nome'], password=cd['senha'])
            if usuario is not None:
                if usuario.is_active:
                    login(request, usuario)
                    return HttpResponse('Usuario autenticado!')
                else:
                    return HttpResponse('Conta desativada!')
            else:
                return HttpResponse('Inicio de sessao invalido!')
    else:
        form = LoginForm()
    return render(request, 'inicio.html', {'form': form})
