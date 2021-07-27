from django.urls import path
from apps.mascotas.views import index, mascota_delete, mascota_edit, mascota_list,mascotata_view,MascotaList,MascotaCreate,MascotaUpdate,MascotaDelet

urlpatterns = [
    
    #registrar
    path('nuevo/', mascotata_view, name='nuevo'),
    path('clase/nuevo/', MascotaCreate.as_view(), name='nuevo_clase'),

    #listar
    path('listar/', mascota_list, name='listar'),
    path('clase/listar/', MascotaList.as_view(), name='listar_clase'),

    #Editar
    path('actualizar/<int:id_mascota>', mascota_edit, name='editar'),
    path('clase/actualizar/<int:pk>', MascotaUpdate.as_view(), name='editar_clase'),

    #eliminar
    path('eliminar/<int:id_mascota>', mascota_delete, name='eliminar'),
    path('clase/eliminar/<int:pk>', MascotaDelet.as_view(), name='eliminar_clase'),
]
