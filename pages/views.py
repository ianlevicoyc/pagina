
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Usuario
from .forms import FormUsuario

class HomePageView(TemplateView):
    template_name = "home.html"

class LoginPageView(TemplateView):
    template_name = "login.html"

class FichaPageView(TemplateView):
    template_name = "ficha.html"

def form_register(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormUsuario()
    
    return render(request, 'register.html', {'form': form})



class VerUsuarioPageView(TemplateView):
    template_name = "verUsuarios.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        # Obtén los datos del inventario
        if query:
            # Realiza la búsqueda por nombre
            inventario = Usuario.objects.filter(Nombre__icontains=query).values('Nombre', 'Apellido', 'Grado', 'Correo')
        else:
            inventario = Usuario.objects.values('Nombre', 'Apellido', 'Grado', 'Correo')

        context['inventario'] = inventario
        return context





