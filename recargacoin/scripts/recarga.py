from recargacoin.models import RecargaCoin
from feedback.models import Carteira
from datetime import datetime


def run():
	datenow = datetime.now()
	recarga_coin = RecargaCoin.objects.filter(mes=datenow.month).first().qtd_coin_mes

	Carteira.objects.all().update(qtd_coin=recarga_coin)
	Carteira.objects.all().update(qtd_coin_recebido=0)
