from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from jogadores.models import Jogador
from espectadores.models import Espectador


@login_required
def total_credenciados(request):
	todos_jogadores = Jogador.objects.all()
	jogadores_presentes = Jogador.objects.filter(presente = 'Sim')
	jogadores_quentinha = Jogador.objects.filter(quentinha = 'Sim')
	todos_espectadores = Espectador.objects.all()
	espectadores_quentinha = Espectador.objects.filter(quentinha = 'Sim')

	num_jogadores = todos_jogadores.count()
	num_jogadores_presentes = jogadores_presentes.count()
	num_jogadores_quentinha = jogadores_quentinha.count()
	num_espectadores_quentinha = espectadores_quentinha.count()
	num_espectadores = todos_espectadores.count()
	num_total_participantes = num_jogadores + num_espectadores
	num_total_participantes_presentes = num_jogadores_presentes + num_espectadores
	num_total_quentinhas = num_jogadores_quentinha + num_espectadores_quentinha

	return render(request, 'credenciados/count.html', {"num_jogadores" : num_jogadores,
	 "num_jogadores_presentes": num_jogadores_presentes, "num_espectadores":num_espectadores,
	 "num_total_participantes":num_total_participantes, "num_total_participantes_presentes": num_total_participantes_presentes,
	 "num_jogadores_quentinha":num_jogadores_quentinha, "num_espectadores_quentinha":num_espectadores_quentinha,
	 "num_total_quentinhas":num_total_quentinhas
	 })
