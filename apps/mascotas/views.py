import django
from django.views.generic.edit import DeleteView, UpdateView
from apps.mascotas.models import Mascota
from django.forms.formsets import ManagementForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView

from apps.mascotas.form import MascotaForm
from apps.mascotas.models import Mascota
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'mascota/index.html')


def mascotata_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = MascotaForm()
    
    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas':mascota}
    return render(request, 'mascota/mascota_list.html', contexto)

def mascota_edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect(mascota_list)
    return render(request, 'mascota/mascota_form.html', {'form':form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect(mascota_list)
    return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list_clase.html'

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('listar')

class MascotaUpdate(UpdateView):
    model =  Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('listar')

class MascotaDelet(DeleteView):
    model = Mascota
    template_name = 'mascota/mascota_delete_clase.html'
    success_url = reverse_lazy('listar')