from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_birth', 'photo')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput({'placeholder': 'Type your password'}))
    password2 = forms.CharField(label='Retype password', widget=forms.PasswordInput({'placeholder': 'Retype your password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']


class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput({'placeholder': 'Type your name'}))
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Type your password'}))
