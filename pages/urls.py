from django.contrib import admin
from django.urls import path, include

from inventario.views import InventarioPageView
from .views import HomePageView, LoginPageView, FichaPageView, VerUsuarioPageView
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name = "home"),
    path("login/", LoginPageView.as_view(), name = "login"),
    path("ficha/", FichaPageView.as_view(), name = "ficha"),
    path("register/", views.form_register, name = "register"),
    path("inventario/", InventarioPageView.as_view(), name = "inventario"),
    path("verUsuarios/", VerUsuarioPageView.as_view(), name = "verUsuarios"),
    path('admin/', admin.site.urls, name='custom_admin'),
    path("blog", include("blog.urls")),

]
