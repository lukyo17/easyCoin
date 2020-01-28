from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def get_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            login(request, user)

            return HttpResponseRedirect(reverse('feedback:get_feedback'))

    else:
        form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'login/index.html', context)

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:get_login'))
