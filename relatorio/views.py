from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RelatorioForm
from feedback.models import Feedback, Carteira


# Create your views here.
@login_required
def get_relatorio(request):
    if request.method == 'POST':
        relatorio = RelatorioForm(request.POST)
        if relatorio.is_valid():
            cd = relatorio.get_rel()
            context_rel={'users': cd, 'table': relatorio}
            return render(request, 'relatorio/index.html', context_rel)
    else:
        relatorio = RelatorioForm()

    context = {
        'table': relatorio,
    }
    return render(request, 'relatorio/index.html', context)
