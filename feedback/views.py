from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from feedback.models import Feedback, Carteira


# Create your views here.
@login_required
def get_feedback(request):
    if request.method == 'POST':
        envioFeedback = FeedbackForm(request.POST, remetente=request.user)
        if envioFeedback.is_valid():
            cd = envioFeedback.save()
            return HttpResponseRedirect('/')

    else:
        envioFeedback = FeedbackForm(remetente=request.user)

    dados = Carteira.objects.get(pessoa=request.user)
    feedForm = Feedback.objects.all().order_by('-data_pub')[:10]
    context_feed = {
        'form': envioFeedback,
        'feeds': feedForm,
        'dados': dados,
    }
    return render(request, 'feedback/index.html', context_feed)
