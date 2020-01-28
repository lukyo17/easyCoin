from django import forms
from django.forms import ModelForm
from feedback.models import Feedback, Carteira

class FeedbackForm(ModelForm):

    class Meta:
        model = Feedback
        fields = ['destino', 'msg', 'qtd_coin']

    def save(self, commit=True):
        self.feedback = super(FeedbackForm, self).save(commit=False)
        destino = self.feedback.destino
        destino.qtd_coin_recebido =  destino.qtd_coin_recebido + self.feedback.qtd_coin
        destino.save()
        remet = Carteira.objects.get(pessoa=self.remetente)
        self.feedback.remetente = remet
        remet.qtd_coin = remet.qtd_coin - self.feedback.qtd_coin
        remet.save()
        if commit:
            self.feedback.save()
        return self.feedback

    def __init__(self, *args, **kwargs):
        self.remetente = kwargs.pop('remetente', None)
        if 'remetente' in kwargs:
            del kwargs['remetente']
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['destino'].queryset = Carteira.objects.exclude(pessoa=self.remetente).order_by('id')

    def clean_qtd_coin(self):
        self.remetente_val = Carteira.objects.filter(pessoa=self.remetente).first().qtd_coin
        if self.cleaned_data['qtd_coin'] > self.remetente_val:
            raise forms.ValidationError("Quantidade insuficiente de Coin!")
        return self.cleaned_data['qtd_coin']