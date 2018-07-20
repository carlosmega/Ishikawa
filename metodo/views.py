from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.views.generic import ListView

from .models import Hallazgo
from .models import Causa

from django.forms import inlineformset_factory

from .forms import HallazgoForm
from .forms import HallazgoCreateForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ListaHallazgos(LoginRequiredMixin, ListView):
    template_name = 'metodo/lista_hallazgos.html'
    model = Hallazgo
    

@login_required()
def crear_hallazgo(request):
    if request.method == 'POST':
        form = HallazgoForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('metodo:causas', pk=obj.pk)
    else:
        form = HallazgoForm(request.POST or None)

    context = {
        'form':form,
    }
    return render(request, 'metodo/causa_raiz.html', context)


@login_required()
def crear_causas(request, pk):
    obj = Hallazgo.objects.get(pk=pk)
    count_causas = Hallazgo.objects.get(pk=pk).causa_set.all().count()
    Causaformset = inlineformset_factory(Hallazgo, Causa, form=HallazgoCreateForm, extra=20 ,max_num=20)
    
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
        'count_causas': count_causas,
    }
    return render(request, 'metodo/causa.html', context)


@login_required()
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


@login_required()
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


def formulario(request, pk):
    obj = get_object_or_404(Hallazgo, pk=pk)
    #obj = Hallazgo.objects.get(pk=pk)
    form = HallazgoCreateForm

    if request.method == 'POST':
        f = form(request.POST or None, instance=obj)
        if f.is_valid():
            print(f)
            f.save()
            return redirect('metodo:formulario', pk=pk)
    else:
        f = form(instance=obj)

    context = {
        'form': form,
    }
    return render(request, 'metodo/formulario.html', context)



