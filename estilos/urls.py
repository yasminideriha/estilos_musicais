from django.urls import path
from cantores.views import listar_cantores, cadastrar_cantores, editar_cantor, excluir_cantor

urlpatterns = [
    path('', listar_cantores, name = 'listar_cantores'), 
    path('cantores/cadastrar/', cadastrar_cantores, name='cadastrar_cantores'), 
    path('cantores/editar/<int:id>/', editar_cantor, name='editar_cantores'), 
    path('cantores/excluir/<int:id>/', excluir_cantor, name='excluir_cantores')
]