from django.db import models


BOOLEAN_CHOICE = (
	('Não','Não'),
	('Sim','Sim'),
)
class Jogador(models.Model):
	nome = models.CharField(max_length = 100)
	equipe = models.CharField(max_length = 50)
	presente = models.CharField(max_length = 3, choices=BOOLEAN_CHOICE)
	quentinha = models.CharField(max_length = 3, choices=BOOLEAN_CHOICE)

		
