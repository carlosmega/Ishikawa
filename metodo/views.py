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
            #obj = Hallazgo.objects.get(pk=pk)
            obj = form.save(commit=False)
            #obj.pk = request.id
            obj.save()
            return redirect('metodo:causas', pk=obj.pk)
    else:
        form = HallazgoForm(request.POST or None)

    context = {
        'form':form,
    }
    return render(request, 'metodo/causa_raiz.html', context)

def crear_causas(request, pk):
    obj = Hallazgo.objects.get(pk=pk)
    Causaformset = inlineformset_factory(Hallazgo, Causa, fields=('hallazgo', 'causa'), extra=20)
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


def amef(request, pk):
    #rpn = Hallazgo.objects.get(pk=pk).causa_set.all()
    obj = Hallazgo.objects.get(pk=pk)
    formsetCausa = inlineformset_factory(Hallazgo, Causa, fields=('hallazgo', 'causa', 'sev', 'det', 'occ', 'rpn'), extra=0)
    if request.method == 'POST':
        formset = formsetCausa(request.POST, instance=obj)
        if formset.is_valid():
            formset.save()
            return redirect('metodo:amef', pk=pk)
    else:
        formset = formsetCausa(instance=obj)

    context = {
        'obj': obj,
        'formset': formset,
        #'rpn': rpn,

    }
    return render(request, 'metodo/amef.html', context)


def kaizen(request, pk):
    obj = Hallazgo.objects.get(pk=pk)

    Causaformset = inlineformset_factory(Hallazgo, Causa, fields=('hallazgo', 'causa', 'rpn', 'solucion', 'responsable', 'fecha_cierre', 'comentarios'), extra=0)
    if request.method == 'POST':
        formset = Causaformset(request.POST, instance=obj, queryset=Causa.objects.filter(rpn__gt=3))
        if formset.is_valid():
            formset.save()
            return redirect('metodo:kaizen', pk=pk)
    else:
        formset = Causaformset(instance=obj, queryset=Causa.objects.filter(rpn__gt=3))

    context = {
        'formset': formset,
    }
    
    return render(request, 'metodo/kaizen.html', context)


