# -*- coding: utf-8 -*-

from django import forms
from .models import Espectador,BOOLEAN_CHOICE

class EspectadorModelForm(forms.ModelForm):
	nome = forms.CharField(
		label = "Nome do Espectador",
		widget = forms.TextInput(
			attrs = {
				'placeholder': 'Nome do Espectador',
				'required': 'required',
				'class': 'form-control'
			}
		)
	)
	quentinha = forms.ChoiceField(
		label = 'Quentinha', 
		choices = BOOLEAN_CHOICE,
	)

	class Meta:
		model = Espectador 
		fields = ('nome','quentinha')