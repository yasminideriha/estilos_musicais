from django.shortcuts import render, redirect, get_object_or_404
from cantores.models import Cantores
from cantores.forms import CantoresForm

def listar_cantores(request):
    cantores = Cantores.objects.all()
    return render(request, 'listarcantores.html', {'cantor': cantores})

def cadastrar_cantores(request):
  if request.method == 'POST':
        form = CantoresForm(request.POST)
        if form.is_valid():
            form.save()
        nome = request.POST ['nome']
        tipo = request.POST ['tipo']
        Cantores.objects.create(nome=nome, tipo=tipo)

        return redirect('listar_cantores')
  else:
        form = CantoresForm()
        return render(request, 'formcantores.html', {'form': form})
  
def editar_cantor(request, id):
    cantor = get_object_or_404(Cantores, id=id)
    if request.method == "POST":
        form = CantoresForm (request.POST, instance=cantor)
        if form.is_valid():
            form.save()
            return redirect('listar_cantores')
    else:
        form = CantoresForm(instance=cantor)
    return render(request, 'formcantor.html',{'form': form})   

def excluir_cantor(request, id):
    cantor = get_object_or_404 (Cantores, id=id)
    if request.method == "POST":
        cantor.delete()
        return redirect('listar_cantores')
    return render(request, 'confirmar_ex_cantor.html', {'cantor': cantor})