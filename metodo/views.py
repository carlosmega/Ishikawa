from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.views.generic import ListView

from .models import Hallazgo
from .models import Causa

from django.forms import inlineformset_factory

from .forms import HallazgoForm
from .forms import HallazgoCreateForm
from .forms import EdithCausa

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
    procesos = Causa.objects.filter(hallazgo__pk=pk).filter(agrupador__agrupador='Procesos')
    herramientas = Causa.objects.filter(hallazgo__pk=pk).filter(agrupador__agrupador='Herramientas')
    manodeobra = Causa.objects.filter(hallazgo__pk=pk).filter(agrupador__agrupador='Mano de Obra')
    externos = Causa.objects.filter(hallazgo__pk=pk).filter(agrupador__agrupador='Externos')
    objeto = Hallazgo.objects.get(pk=pk)
    count_causas = Hallazgo.objects.get(pk=pk).causa_set.all().count()
    objeto_causas = Causa.objects.all()
    objslug = Causa.objects.filter(hallazgo__pk=pk)
    form = HallazgoCreateForm

    if request.method == 'POST':
        form = HallazgoCreateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = HallazgoCreateForm()

    context = {
        'procesos': procesos,
        'herramientas': herramientas,
        'manodeobra': manodeobra,
        'externos': externos,
        'objeto': objeto,
        'count_causas': count_causas,
        'objeto_causas': objeto_causas,
        'form': form,
        'objslug': objslug,
    }
    return render(request, 'metodo/causa.html', context)

def editar_causas(request, pk, slug):
    obj_slug = Causa.objects.get(slug=slug)
    obj_hallazgo = Causa.objects.filter(hallazgo__pk=pk)

    data = {
        'hallazgo': obj_hallazgo,
        'causa': obj_slug,
    }

    if request.method == 'POST':
        form = EdithCausa(request.POST, data)
        if form.is_valid():
            obj_slug.causa = form.cleaned_data['causa']
            obj_slug.save()
            return redirect('metodo:causas', pk=pk)
    else:
        form = EdithCausa(data)

    context = {
        'form': form,
    }
    return render(request, 'metodo/editar_causas.html', context)


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



