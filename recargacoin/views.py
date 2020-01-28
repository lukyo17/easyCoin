from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from recargacoin.models import RecargaCoin
from feedback.models import Carteira
from log.models import LogRecarga
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required



# Create your views here.
@login_required
@staff_member_required
def run(request):
	
	datenow = datetime.now()
	recarga_coin = RecargaCoin.objects.filter(mes=datenow.month).first().qtd_coin_mes

	Carteira.objects.all().update(qtd_coin=recarga_coin)
	Carteira.objects.all().update(qtd_coin_recebido=0)
	qtd = recarga_coin
	date_exec = datenow
	msg = "Foi realizado uma recarga geral, na data programada {} com quantidade de {} coins!".format(date_exec,qtd)
	log = LogRecarga(pessoa=User.objects.get(username=request.user),evento=msg)
	log.save()

	return HttpResponseRedirect('/')
