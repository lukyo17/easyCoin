from django import forms
from django.forms import ModelForm, Select
from feedback.models import Feedback, Carteira
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import Sum

class DateInput(forms.DateTimeInput):
    input_type = 'date'


class RelatorioForm(forms.Form):
    date_init = forms.DateTimeField(widget=DateInput(), label="Data Inicial ")
    date_end = forms.DateTimeField(widget=DateInput(), label="Data Final ")
    user_sel = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="TODOS", required=False, label="Usuario ")

    def get_rel(self):
        date_init = self.cleaned_data['date_init']
        #setar hora e minuto fixo
        date  = self.cleaned_data['date_end']
        date_end = date.replace(hour=23,minute=59)

        if self.cleaned_data['user_sel'] == None:
            date_in = Feedback.objects.select_related('destino').filter(data_pub__range =[date_init,date_end]).values('destino__pessoa__first_name','destino__pessoa__last_name').annotate(qtd_rec=Sum('qtd_coin'))
        else:
            user = Carteira.objects.select_related('pessoa').get(pessoa=self.cleaned_data['user_sel'])
            date_in = Feedback.objects.select_related('destino').filter(destino=user,data_pub__range =[date_init,date_end]).values('destino__pessoa__first_name','destino__pessoa__last_name').annotate(qtd_rec=Sum('qtd_coin'))  
        return date_in


