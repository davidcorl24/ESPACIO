from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('nuevoEspacioestudio/', views.nuevoEspacioestudio),
    path('listadoEspacios/',views.listadoEspacioestudio),
    path('guardarEspacio/', views.guardarEspacio),
    path('eliminarEspacioestudio/<id>/',views.eliminarEspacioestudio),
    path('editarEspacio/<id>/', views.editarEspacio, name='editarEspacio'),
    path('actualizarEspacio/<int:id>/', views.actualizar_espacio, name='actualizarEspacio'),
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    path('nuevaReserva/', views.nuevaReserva),
    path('listadoReservas/',views.listadoReservas),
    path('guardarReserva/', views.guardarReserva),
    path('eliminarReserva/<id>/',views.eliminarReserva),
    path('editarReserva/<id>/', views.editarReserva, name='editarReserva'),
    path('actualizarReserva/<int:id>/', views.actualizar_reserva, name='actualizarReserva'),
    path('exportarReportePDF/', views.exportar_reservas_pdf, name='exportar_reservas_pdf'),
    ]