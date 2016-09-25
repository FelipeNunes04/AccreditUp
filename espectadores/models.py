from django.db import models

BOOLEAN_CHOICE = (
		('Sim','Sim'),
		('Não','Não'),
)
class Espectador(models.Model):
	nome = models.CharField(max_length = 100)
	quentinha = models.CharField(max_length=3, choices=BOOLEAN_CHOICE)

