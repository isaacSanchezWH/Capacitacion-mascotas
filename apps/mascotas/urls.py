from django.urls import path
from apps.mascotas.views import index, mascota_delete, mascota_edit, mascota_list,mascotata_view,MascotaList,MascotaCreate,MascotaUpdate,MascotaDelet

urlpatterns = [
    path('', index, name='index'),
    path('nuevo/', mascotata_view, name='nuevo'),
    path('clase/nuevo/', MascotaCreate.as_view(), name='nuevo_clase'),
    path('listar/', mascota_list, name='listar'),
    path('clase/listar/', MascotaList.as_view(), name='listar_clase'),
    path('actualizar/<int:id_mascota>', mascota_edit, name='editar'),
    path('clase/actualizar/<int:pk>', MascotaUpdate.as_view(), name='editar'),
    #path('eliminar/<int:id_mascota>', mascota_delete, name='eliminar'),
    path('clase/eliminar/<int:pk>', MascotaDelet.as_view(), name='eliminar'),
]
