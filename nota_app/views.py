from django.shortcuts import render, get_object_or_404, redirect
from .models import Nota
from .forms import NotaForm


def lista_notas(request):

    notas = Nota.objects.all()

    return render(request, 'nota_app/lista_notas.html', {'notas': notas} )

def crear_notas(request):

    if request.method == 'POST':

        form = NotaForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('lista_notas')
        
    else:

        form = NotaForm()

    return render(request, 'nota_app/form_nota.html', {'form': form} )

def editar_notas(request, pk):
    
    nota = get_object_or_404(Nota, pk=pk)

    if request.method == 'POST':

        form = NotaForm(request.POST, instance=nota)

        if form.is_valid():

            form.save()

            return redirect('lista_notas')
    else:

        form = NotaForm(instance=nota)

    return render(request, 'nota_app/editar_nota.html', {'form': form} )

def eliminar_notas(request, id):

    nota = get_object_or_404(Nota, id=id)

    nota.delete()

    return redirect('lista_notas')