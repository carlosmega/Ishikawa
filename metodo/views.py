from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import ListView

from .models import Hallazgo
from .models import Causa

from django.forms import inlineformset_factory

from .forms import HallazgoForm

# Create your views here.
class ListaHallazgos(ListView):
    template_name = 'metodo/lista_hallazgos.html'
    model = Hallazgo
    

def crear_hallazgo(request):
    if request.method == 'POST':
        form = HallazgoForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = HallazgoForm(request.POST or None)

    context = {
        'form':form,
    }
    return render(request, 'metodo/causa_raiz.html', context)

def crear_causas(request, pk):
    obj = Hallazgo.objects.get(pk=pk)
    Causaformset = inlineformset_factory(Hallazgo, Causa, fields=('hallazgo', 'causa'), extra=12)
    if request.method == 'POST':
        formset = Causaformset(request.POST, instance=obj)
        if formset.is_valid():
            formset.save()
            return redirect('metodo:causas', pk=pk)
    else:
        formset = Causaformset(instance=obj)

    context = {
        'obj': obj,
        'formset': formset,
    }
    return render(request, 'metodo/causa.html', context)

