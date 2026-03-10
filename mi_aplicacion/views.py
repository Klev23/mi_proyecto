from django.shortcuts import render 
from django.views import View
from django.shortcuts import redirect
from .models import Escuela, Maestro, Alumno
from mi_aplicacion.forms import EscuelaForm, MaestroForm
from django.urls import reverse

class Home(View):
    def get(self, request):
        cdx={
            "TITULO": "Mi Aplicación",
            "SUBTITULO": "Bienvenido a mi aplicación Django",
        }
        return render(request, "mi_aplicacion/home/home.html", cdx)
    
class Escuelas(View):
    def get(self, request):
        Escuelas = Escuela.objects.all()
        cdx={
            "TITULO": "Escuelas",
            "SUBTITULO": "Lista de Escuelas",
            "ESCUELAS": Escuelas,
        }
        return render(request, "mi_aplicacion/escuela/escuelas.html", cdx)

class EscuelaAlta(View):
    def get(self, request):
        form = EscuelaForm()
        cdx={
            "TITULO": "Escuela",
            "SUBTITULO": "Alta de Escuela",
            "form": form,
        }
        return render(request, "mi_aplicacion/escuela/CRUD.html", cdx)
    
    def post(self, request):
        escuela = EscuelaForm(request.POST, request.FILES)
        if escuela.is_valid():
            escuela.save()
            return redirect("escuelas")
        return redirect("home")    

class EscuelaEditar(View):
    def get(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuela)
        cdx={
            "TITULO": "Escuela",
            "SUBTITULO": "Editar Escuela",
            "form": form,
        }
        return render(request, "mi_aplicacion/escuela/CRUD.html", cdx)
    
    def post(self, request, id):
        escuela = Escuela.objects.get(id=id)
        form = EscuelaForm(request.POST, request.FILES, instance=escuela)
        if form.is_valid():
            form.save()
            return redirect("escuelas")
        return redirect("home")
    

class EscuelaEliminar(View):
    def get(self, request, id):
        escuela = Escuela.objects.filter(id=id).first()
        cdx={
            "TITULO": "Escuela",
            "SUBTITULO": "Eliminar Escuela",
            "escuela": escuela,
        }
        return render(request, "mi_aplicacion/escuela/CRUD.html", cdx)
    
    def post(self, request, id):
        escuela = Escuela.objects.get(id=id)
        escuela.delete()
        return redirect("escuelas")

class Maestros(View):
    def get(self, request):
        Maestros = Maestro.objects.all()
        cdx={
            "TITULO": "Maestros",
            "SUBTITULO": "Lista de Maestros",
            "MAESTROS": Maestros,
        }
        return render(request, "mi_aplicacion/maestro/maestros.html", cdx)
    
class MaestroAlta(View):
    def get(self, request):
        form = MaestroForm()
        cdx={
            "TITULO": "Maestro",
            "SUBTITULO": "Alta de Maestro",
            "form": form,
        }
        return render(request, "mi_aplicacion/escuela/CRUD.html", cdx)
    
    def post(self, request):
        maestro = MaestroForm(request.POST, request.FILES)
        if maestro.is_valid():
            maestro.save()
            return redirect("maestros")
        return redirect("home")

class MaestroEditar(View):
    def get(self, request, id):
        maestro = Maestro.objects.filter(id=id).first()
        form = MaestroForm(instance=maestro)
        cdx={
            "TITULO": "Maestro",
            "SUBTITULO": "Editar Maestro",
            "form": form,
        }
        return render(request, "mi_aplicacion/escuela/CRUD.html", cdx)
    
    def post(self, request, id):
        maestro = Maestro.objects.get(id=id)
        form = MaestroForm(request.POST, request.FILES, instance=maestro)
        if form.is_valid():
            form.save()
            return redirect("maestros")
        return redirect("home")

class MaestroEliminar(View):
    def get(self, request, id):
        maestro = Maestro.objects.filter(id=id).first()
        cdx={
            "TITULO": "Maestro",
            "SUBTITULO": "Eliminar Maestro",
            "maestro": maestro,
        }
        return render(request, "mi_aplicacion/escuela/CRUD.html", cdx)
    
    def post(self, request, id):
        maestro = Maestro.objects.get(id=id)
        maestro.delete()
        return redirect("maestros")
