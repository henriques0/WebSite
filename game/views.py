from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

# Create your views here.
class PaginaInicialView(TemplateView):
	template_name = "index.html"

class PaginaProjetoView(TemplateView):
		template_name = "projeto.html"

class PaginaContatoView(TemplateView):
		template_name = "contato.html"

class PaginaCurriculoView(TemplateView):
		template_name = "curriculo.html"
