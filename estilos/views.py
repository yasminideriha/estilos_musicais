from django.shortcuts import render, redirect, get_object_or_404
from estilos.models import Estilos

def listar_estilos(request):
    estilos = Estilos.objects.all()
    return render(request, 'listarestilo.html', {'estilos': estilos})

def cadastrar_estilos(request):
   if request.method == 'POST':
      nome = request.POST['nome']
      sigla = request.POST['sigla']
      Estilos.objects.create(nome=nome, sigla=sigla)
      return redirect('listar_estilos')
   return render(request, 'formestilo.html')

def editar_estilos(request, id):
    estilos = get_object_or_404(Estilos, id=id)
    if request.method == "POST":
        estilos.nome = request.POST['nome']
        estilos.sigla = request.POST['sigla']
        estilos.save()
        return redirect('listar_estilos')
    return render(request, 'formestilo.html', {'estilo': estilos})

def excluir_estilos(request, id):
    estilos = get_object_or_404(Estilos, id=id)
    if request.method == "POST":
        estilos.delete()
        return redirect('listar_estilos')
    return render(request, 'confirmar_exclusaoestilo.html', {'estilo': estilos})
