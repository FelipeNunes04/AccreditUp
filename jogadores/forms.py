# -*- coding: utf-8 -*-

from django import forms
from .models import Jogador,BOOLEAN_CHOICE

class JogadorModelForm(forms.ModelForm):
	nome = forms.CharField(
		label = "Nome do Jogador",
		widget = forms.TextInput(
			attrs = {
				'placeholder': 'Nome do Jogador',
				'required': 'required',
				'class': 'form-control'
			}
		)
	)
	equipe = forms.CharField(
		label = "Equipe",
		widget = forms.TextInput(
			attrs = {
				'placeholder': 'Nome da Equipe',
				'required': 'required',
				'class': 'form-control'
			}
		)
	)
	presente = forms.ChoiceField(
		label = 'Presente', 
		choices=BOOLEAN_CHOICE,
	)
	quentinha = forms.ChoiceField(
		label = 'Quentinha', 
		choices=BOOLEAN_CHOICE,
	)

	class Meta:
		model = Jogador 
		fields = ('nome','equipe','presente','quentinha')