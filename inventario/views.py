from django.shortcuts import render
from .forms import FormElementoEnUso, FormElementoPrestado, FormElemento, FormAlertas
from django.views.generic import TemplateView
from .models import Elementos
# Create your views here.
def form_ElementoEnUso(request):
    if request.method == 'POST':
        form = FormElementoEnUso(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormElementoEnUso()
    
    return render(request, 'EnUso.html', {'form': form})
########################
def form_ElementoPrestado(request):
    if request.method == 'POST':
        form = FormElementoPrestado(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormElementoPrestado()
    
    return render(request, 'prestado.html', {'form': form})
#############################
def form_Elemento(request):
    if request.method == 'POST':
        form = FormElemento(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormElemento()
    
    return render(request, 'elemento.html', {'form': form})
######################
def form_Alertas(request):
    if request.method == 'POST':
        form = FormAlertas(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormAlertas()
    
    return render(request, 'alertas.html', {'form': form})

#####################

class InventarioPageView(TemplateView):
    template_name = "inventario.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        # Obtén los datos del inventario
        if query:
            # Realiza la búsqueda por nombre
            inventario = Elementos.objects.filter(Nombre__icontains=query).values('Nombre', 'Marca', 'Tipo', 'Observaciones', 'Estado', 'Cantidad', 'Ubicación')
        else:
            inventario = Elementos.objects.values('Nombre', 'Marca', 'Tipo', 'Observaciones', 'Estado', 'Cantidad', 'Ubicación')

        context['inventario'] = inventario
        return context