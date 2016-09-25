from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from espectadores.models import Espectador
from espectadores.forms import EspectadorModelForm

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class Home(LoginRequiredMixin, TemplateView):
	template_name = u'index.html'


class EspectadorFormView(LoginRequiredMixin, FormView):
	template_name = u'espectador/cadastrar.html'
	form_class = EspectadorModelForm
	success_url = reverse_lazy('cadastrar-espectador')

	def form_valid(self,form):
		espectador = form.save(commit = False)
		espectador.save()
		messages.success(self.request, u"Espectador cadastrado com sucesso!")
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self,form):
		messages.error(self.request, u"Por favor, preencha corretamente os campos")
		return self.render_to_response(self.get_context_data(form = form))

class EspectadorListView(LoginRequiredMixin, ListView):
	template_name = u'espectador/listar.html'

	def get_queryset(self):
		espectador = Espectador.objects.all().order_by('nome')
		return espectador

class EspectadorUpdateView(LoginRequiredMixin, UpdateView):
	template_name = u'espectador/editar.html'
	model = Espectador
	form_class = EspectadorModelForm
	success_url = reverse_lazy('listar-espectador')

	def form_valid(self,form):
		espectador = form.save(commit = False)
		espectador.save()
		messages.success(self.request, u"Espectador atualizado com sucesso!")
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self,form):
		messages.error(self.request, u"Por favor, preencha corretamente os campos")
		return self.render_to_response(self.get_context_data(form = form))

class EspectadorDeleteView(DeleteView):
	template_name = "espectador/deletar.html"
	model = Espectador
	success_url = reverse_lazy('listar-espectador')
	success_message = "Espectador deletado com sucesso!"

	def delete(self,request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(EspectadorDeleteView, self).delete(request, *args, **kwargs)