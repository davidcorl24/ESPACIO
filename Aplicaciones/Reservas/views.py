from django.shortcuts import render, redirect,get_object_or_404
from .models import EspacioEstudio,Reserva

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
# Página de inicio
def inicio(request):
    return render(request, 'inicio.html')
# Presenta el formulario para registrar un nuevo espacio de estudio
def nuevoEspacioestudio(request):
    return render(request, 'nuevoEspacioestudio.html')
# Presenta el listado de espacios de estudio registrados
def listadoEspacioestudio(request):
    espaciosBdd = EspacioEstudio.objects.all()
    return render(request, 'listadoEspacios.html', {'espacios': espaciosBdd})

# Captura los datos del formulario e inserta un nuevo espacio en la base de datos
def guardarEspacio(request):
        nombre = request.POST['txt_nombre']
        apellido = request.POST['txt_apellido']
        ubicacion = request.POST['txt_ubicacion']
        capacidad = request.POST['txt_capacidad']
        descripcion = request.POST['txt_descripcion']
        disponible = request.POST['txt_disponible']  
        nuevoEspacioestudio=EspacioEstudio.objects.create(
            nombre=nombre,
            apellido=apellido,
            ubicacion=ubicacion,
            capacidad=capacidad,
            descripcion=descripcion,
            disponible=disponible
        )
        return redirect('/listadoEspacios')

# Elimina un espacio de estudio por ID
def eliminarEspacioestudio(request, id):
    espacioestudioEliminar = EspacioEstudio.objects.get(id=id)
    espacioestudioEliminar.delete()
    return redirect('/listadoEspacios')
from django.shortcuts import render, redirect, get_object_or_404
from .models import EspacioEstudio  # Asegúrate de importar el modelo correcto

def editarEspacio(request, id):
    # Obtener el espacio de estudio a editar, asegurándose de que exista
    espaciosestudioEditar = get_object_or_404(EspacioEstudio, id=id)
    espacios = EspacioEstudio.objects.all()
    return render(request, 'editarEspaciosestudio.html', {'espaciosestudioEditar': espaciosestudioEditar})

def actualizar_espacio(request, id):
    # Obtén el objeto espacio por id
    espacio = get_object_or_404(Espacio, id=id)

    if request.method == 'POST':
        # Actualiza los campos del espacio con los datos del formulario
        espacio.nombre = request.POST['nombre']
        espacio.apellido = request.POST['apellido']
        espacio.ubicacion = request.POST['ubicacion']
        espacio.capacidad = request.POST['capacidad']
        espacio.descripcion = request.POST['descripcion']
        espacio.disponible = request.POST['disponible']
        espacio.save()  # Guarda los cambios en la base de datos
        return redirect('listadoEspacios')  # Redirige a la lista de espacios
    
    return render(request, 'editarEspaciosestudio.html', {'espacio': espacio})
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def nuevaReserva(request):
    espacios = EspacioEstudio.objects.all()  # Para listar los espacios disponibles en el formulario
    return render(request, 'nuevaReserva.html', {'espacios': espacios})

# Presenta el listado de reservas registradas
def listadoReservas(request):
    reservasBdd = Reserva.objects.all()
    return render(request, 'listadoReservas.html', {'reservas': reservasBdd})

# Captura los datos del formulario e inserta una nueva reserva en la base de datos
def guardarReserva(request):
    if request.method == 'POST':
        apellido = request.POST['txt_apellido']
        espacio_id = request.POST['txt_espacio']
        fecha = request.POST['txt_fecha']
        horainicio = request.POST['txt_horainicio']
        horafin = request.POST['txt_horafin']

        # Crear la nueva reserva
        nuevaReserva = Reserva.objects.create(
            apellido=apellido,
            espacio=EspacioEstudio.objects.get(id=espacio_id),
            fecha=fecha,
            horainicio=horainicio,
            horafin=horafin,
            
        )
        return redirect('/listadoReservas')

# Elimina una reserva por ID
def eliminarReserva(request, id):
    reservaEliminar = get_object_or_404(Reserva, id=id)
    reservaEliminar.delete()
    return redirect('/listadoReservas')

# Presenta el formulario para editar una reserva
def editarReserva(request, id):
    reservaEditar = get_object_or_404(Reserva, id=id)
    espacios = EspacioEstudio.objects.all()  # Para listar los espacios disponibles
    return render(request, 'editarReserva.html', {'reserva': reservaEditar, 'espacios': espacios})

# Actualiza una reserva existente
def actualizar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        # Aquí procesas los datos enviados desde el formulario
        reserva.apellido = request.POST['txt_apellido']
        reserva.espacio_id = request.POST['txt_espacio']
        reserva.fecha = request.POST['txt_fecha']
        reserva.horainicio = request.POST['txt_horainicio']
        reserva.horafin = request.POST['txt_horafin']
        reserva.save()
        return redirect('/listadoReservas')  # Cambia según tu lógica
    return render(request, 'editarReserva.html', {'reserva': reserva})
def exportar_reservas_pdf(request):
    # Crear una respuesta HTTP con el tipo de contenido adecuado para un archivo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reservas.pdf"'
    
    # Crear un objeto canvas de ReportLab para generar el PDF
    p = canvas.Canvas(response, pagesize=letter)
    
    # Establecer las fuentes y tamaños de texto
    p.setFont("Helvetica", 12)
    
    # Establecer el título del reporte
    p.drawString(200, 750, "Reporte de Reservas")
    
    # Escribir los encabezados de la tabla
    p.drawString(50, 730, "ID")
    p.drawString(100, 730, "Apellido")
    p.drawString(200, 730, "Espacio")
    p.drawString(300, 730, "Fecha")
    p.drawString(400, 730, "Hora Inicio")
    p.drawString(500, 730, "Hora Fin")
    
    # Espacio para las filas
    y_position = 710
    
    # Obtener las reservas
    reservas = Reserva.objects.all()
    
    # Iterar sobre las reservas y agregar cada una a la tabla
    for reserva in reservas:
        p.drawString(50, y_position, str(reserva.id))
        p.drawString(100, y_position, reserva.apellido)
        p.drawString(200, y_position, reserva.espacio.descripcion)
        p.drawString(300, y_position, str(reserva.fecha))
        p.drawString(400, y_position, str(reserva.horainicio))
        p.drawString(500, y_position, str(reserva.horafin))
        
        y_position -= 20  # Moverse hacia abajo para la siguiente fila
        
        # Si hemos llegado al final de la página, agregar una nueva página
        if y_position < 50:
            p.showPage()
            p.setFont("Helvetica", 12)
            y_position = 750
    
    # Finalizar el PDF
    p.showPage()
    p.save()
    
    return response
def detalles(request):
    espacios = EspacioEstudio.objects.all()  # Para listar los espacios disponibles en el formulario
    return render(request, 'detalles.html', {'espacios': espacios})

