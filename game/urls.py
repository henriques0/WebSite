from django.urls import path
from .views import *

urlpatterns = [
    path('', PaginaInicialView.as_view(), name="index"),
    path('sobre', PaginaSobreView.as_view(), name="sobre"),
    path('contao', PaginaContatoView.as_view(), name="contato"),

]
