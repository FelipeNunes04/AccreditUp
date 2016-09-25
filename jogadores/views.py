from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from jogadores.models import Jogador
from jogadores.forms import JogadorModelForm
from espectadores.views import LoginRequiredMixin

class JogadorFormView(LoginRequiredMixin, FormView):
	template_name = u'jogador/cadastrar.html'
	form_class = JogadorModelForm
	success_url = reverse_lazy('cadastrar-jogador')

	def form_valid(self,form):
		jogador = form.save(commit = False)
		jogador.save()
		messages.success(self.request, u"Jogador cadastrado com sucesso!")
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self,form):
		messages.error(self.request, u"Por favor, preencha corretamente os campos")
		return self.render_to_response(self.get_context_data(form = form))

class JogadorListView(LoginRequiredMixin, ListView):
	template_name = u'jogador/listar.html'

	def get_queryset(self):
		jogador = Jogador.objects.all().order_by('equipe')
		return jogador

class JogadorUpdateView(LoginRequiredMixin, UpdateView):
	template_name = u'jogador/editar.html'
	model = Jogador
	form_class = JogadorModelForm
	success_url = reverse_lazy('listar-jogador')

	def form_valid(self,form):
		jogador = form.save(commit = False)
		jogador.save()
		messages.success(self.request, u"Jogador atualizado com sucesso!")
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self,form):
		messages.error(self.request, u"Por favor, preencha corretamente os campos")
		return self.render_to_response(self.get_context_data(form = form))

class JogadorDeleteView(DeleteView):
	template_name = "jogador/deletar.html"
	model = Jogador
	success_url = reverse_lazy('listar-jogador')
	success_message = "Jogador deletado com sucesso!"

	def delete(self,request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(JogadorDeleteView, self).delete(request, *args, **kwargs)

