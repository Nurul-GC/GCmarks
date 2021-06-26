from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from accounts.forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here
def index(request):
    return render(request, 'index.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'section': 'dashboard'})


def inicio(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            usuario = authenticate(request, username=cd['name'], password=cd['password'])
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
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html',
                  {'form': user_form})
