from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', max_length=20)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def clean(self):
        #import pdb; pdb.set_trace()
        cd = self.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        if user is None:
            raise forms.ValidationError('Usuario/Senha Inválidos')
        else:
            if not user.is_active:
                raise forms.ValidationError('Conta Desabilitada')
