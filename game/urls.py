from django.urls import path
from .views import *

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="index"),
    path('projeto', PaginaProjetoView.as_view(), name="projeto"),
    path('contao', PaginaContatoView.as_view(), name="contato"),
    path('curriculo', PaginaCurriculoView.as_view(), name="curriculo"),
    path('sobre', PaginaSobreView.as_view(), name="sobre"),

]
