from django import forms


class LoginForm(forms.Form):
    nome = forms.CharField(widget=forms.TextInput({'placeholder': 'Digite o seu nome'}))
    senha = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Digite a sua senha'}))
