from datetime import datetime
import TurnosCRUD as MetodosCRUD
import MetodosDoctores as MetodosDoctores
import MetodosPacientes as MetodosPacientes
import Utils as Utils

def ObtenerIDSDoctores():
    idsDoctores = MetodosCRUD.CRUDObtenerIDSDeLosDoctores()
    return idsDoctores

def ObtenerIDSPacientes():
    idsPacientes = MetodosCRUD.CRUDObtenerIDSDeLosPacientes()
    return idsPacientes

def BuscarPacienteDelTurno(id):
    paciente = MetodosCRUD.CRUDBuscarPacienteDelTurno(id)
    return paciente

def BuscarDoctorDelTurno(id):
    doctor = MetodosCRUD.CRUDBuscarDoctorDelTurno(id)
    return doctor

def BuscarFechaHoraDelTurno(id):
    fechaHora = MetodosCRUD.CRUDSeleccionarTurnoFecha(id)
    return fechaHora

def MostrarPacientesDisponibles():
    print("PACIENTES DISPONIBLES: ")
    MetodosPacientes.USUARIOListarPacientes()

def MostrarDoctoresDisponibles():
    print("DOCTORES DISPONIBLES: ")
    MetodosDoctores.USUARIOListarDoctores()

def MostrarTurnosDisponibles():
    print("TURNOS DISPONIBLES: ")
    turnosPacientes = MetodosCRUD.CRUDListarTurnosPacientes()
    turnos = []
    
    for turnopaciente in turnosPacientes:
        turno = tuple(turnopaciente)
        idTurno = turno[1]
        idPaciente = turno[2]
        idDoctor = turno[3]

        paciente = BuscarPacienteDelTurno(idPaciente)
        doctor = BuscarDoctorDelTurno(idDoctor)
        fechaHora = BuscarFechaHoraDelTurno(idTurno)
        fecha = fechaHora[1].strftime("%Y-%m-%d")
        hora = str(fechaHora[2])
        turnos.append((idTurno, paciente, doctor, fecha, hora))

    for turno in turnos:
        turnoIterado = tuple(turno)
        print(f"ID: {turnoIterado[0]}, Paciente: {turnoIterado[1]}, Doctor: {turnoIterado[2]}, Fecha: {turnoIterado[3]}, Hora: {turnoIterado[4]}")


def ObtenerUltimoIDTurno():
    turnos = MetodosCRUD.CRUDListarTurnos()
    listaIds = []
    if len(turnos) == 0:
        return 1
    else:
        for turno in turnos:
            turnoIterado = tuple(turno)
            id = turnoIterado[0]
            listaIds.append(id)
    
    return max(listaIds)
    
def ObtenerLosIdsTurnos():
    turnos = MetodosCRUD.CRUDListarTurnosPacientes()
    listaIds = []
    for turno in turnos:
        turnoIterado = tuple(turno)
        id = turnoIterado[1]
        listaIds.append(id)
    
    return listaIds

def IngresarDatosParaActualizarTurno(idDoctorOriginal, fechaOriginal, horaOriginal):
    opcionDoctor = 'j'
    opcionFecha = 'j'
    opcionHora = 'j'
    idDoctor = -1
    fecha = -1
    hora = -1

    while opcionDoctor != 's' and opcionDoctor != 'n':
        print("\n ¿Desea actualizar el doctor? (s/n): ")
        opcionDoctor = input().strip().lower()
        if opcionDoctor == "s":
            idDoctor = IngresarIDDoctor()
            break
        elif opcionDoctor == "n":
            idDoctor = idDoctorOriginal
            break
        else:
            print("Por favor, ingrese una opción válida")
    
    while opcionFecha != 's' and opcionFecha != 'n':
        print("\n ¿Desea actualizar la fecha? (s/n): ")
        opcionFecha = input().strip().lower()
        if opcionFecha == "s":
            fecha = IngresarFechaTurno()
            break
        elif opcionFecha == "n":
            fecha = fechaOriginal
            break
        else:
            print("Por favor, ingrese una opción válida")

    while opcionHora != 's' and opcionHora != 'n':
        print("\n ¿Desea actualizar la hora? (s/n): ")
        opcionHora = input().strip().lower()
        if opcionHora == "s":
            hora = IngresarHoraTurno()
            break
        elif opcionHora == "n":
            hora = horaOriginal
            break
        else:
            print("Por favor, ingrese una opción válida")

    datosActualizados = (idDoctor, fecha, hora)
    return datosActualizados



def IngresarHoraTurno():
    hora = -1
    print("Ingrese la hora del turno (hh:mm): ")

    while True:
        try:
            entradaHora = input().strip()
            if entradaHora == "":
                print("Hora no ingresada. Ingrese la hora del turno (hh:mm): ")
            else:
                hora = datetime.strptime(entradaHora, "%H:%M")
                break
        except ValueError:
            print("Por favor, ingrese una hora válida. Ingrese la hora del turno (hh:mm): ")

    return hora

def IngresarFechaTurno():
    fecha = -1
    print("Ingrese la fecha del turno (yyyy-mm-dd): ")

    while True:
        try:
            entradaFecha = input().strip()
            if entradaFecha == "":
                print("Fecha no ingresada. Ingrese la fecha del turno (yyyy-mm-dd): ")
            else:
                fecha = datetime.strptime(entradaFecha, "%Y-%m-%d")
                if not Utils.CorroborarFechaRealParaTurno(fecha.strftime("%Y-%m-%d")):
                    print("Fecha incorrecta. Por favor, ingrese una fecha válida")
                else:
                    break
        except ValueError:
            print("Por favor, ingrese una fecha válida. Ingrese la fecha del turno (yyyy-mm-dd): ")

    
    return fecha


def IngresarIDPaciente():
    idPaciente = -1
    pacientes = MetodosPacientes.USUARIOListarPacientes()

    if len(pacientes) == 0:
        print("No hay pacientes disponibles para programar un turno")
        Utils.TiempoSleep("el menú de turnos")
        Utils.VolverMenuTurnos()
    
    idsPacientes = ObtenerIDSPacientes()

    print("Ingrese el ID del paciente: ")

    while True:
        try:
            entradaIdPaciente = input().strip()
            if entradaIdPaciente == "":
                print("ID no ingresado, por favor ingrese un ID válido")
            else:
                idPaciente = int(entradaIdPaciente)
                if not idPaciente in idsPacientes:
                    print("ID de paciente no existente, por favor ingrese un ID válido")
                else:
                    break
        except ValueError:
            print("Por favor, ingrese un número entero")
        
    return idPaciente

def IngresarIDDoctor():
    idDoctor = -1
    doctores = MetodosDoctores.USUARIOListarDoctores()
    if len(doctores) == 0:
        print("No hay doctores disponibles para programar un turno")
        Utils.TiempoSleep("el menú de turnos")
        Utils.VolverMenuTurnos()
    
    idsDoctores = ObtenerIDSDoctores()

    print("Ingrese el ID del doctor: ")

    while True:
        try:
            entradaIdDoctor = input().strip()
            if entradaIdDoctor == "":
                print("ID no ingresado, por favor ingrese un ID válido")
            else:
                idDoctor = int(entradaIdDoctor)
                if not idDoctor in idsDoctores:
                    print("ID de doctor no existente, por favor ingrese un ID válido")
                else:
                    break
        except ValueError:
            print("Por favor, ingrese un número entero")
        
    return idDoctor
    

def USUARIOProgramarTurno():
    print("PROGRAMAR TURNO: ")
    print("Ingrese los datos del turno a programar: \n")

    idPaciente = IngresarIDPaciente()
    idDoctor = IngresarIDDoctor()
    fecha = IngresarFechaTurno()
    hora = IngresarHoraTurno()
    try:
        MetodosCRUD.CRUDAgregarTurno(fecha, hora)
        idTurno = ObtenerUltimoIDTurno()
        MetodosCRUD.CRUDAsignarTurno(idTurno, idPaciente, idDoctor)
        print("Turno creado correctamente")
    except ValueError:
        print("Fecha y/u hora incorrecta")
        Utils.TiempoSleep("el menú de turnos")
        Utils.VolverMenuTurnos()

def USUARIOActualizarTurno():
    Utils.LimpiarConsola()

    idTurno = -1
    idsTurnos = []
    entradaIdTurno = 'j'
    datosFecha = ()
    datosTurno = ()
    idDoctorOriginal = -1
    fechaOriginal = -1
    horaOriginal = -1
    pacienteOriginal = ""
    doctorOriginal = ""

    print("TURNOS: ")
    MostrarTurnosDisponibles()

    print("ACTUALIZAR TURNO: ")
    print("Ingrese el ID del turno a actualizar: ")

    idsTurnos = ObtenerLosIdsTurnos()
    if len(idsTurnos) == 0:
        print("No hay turnos disponibles para actualizar")
        Utils.TiempoSleep("el menú de turnos")
        Utils.VolverMenuTurnos()

    try:
        entradaIdTurno = input().strip()
        if entradaIdTurno == "":
            print("ID no ingresado")
            Utils.TiempoSleep("el menú de turnos")
            Utils.VolverMenuTurnos()
        else:
            idTurno = int(entradaIdTurno)
            if not idTurno in idsTurnos:
                print("ID de turno no existente")
                Utils.TiempoSleep("el menú de turnos")
                Utils.VolverMenuTurnos()

            
    except ValueError:
        print("Por favor, ingrese un número entero")
        Utils.TiempoSleep("el menú de turnos")
        Utils.VolverMenuTurnos()

    
    datosTurno = MetodosCRUD.CRUDSeleccionarTurnoPaciente(idTurno)
    datosFecha = MetodosCRUD.CRUDSeleccionarTurnoFecha(idTurno)

    if datosTurno == None or datosFecha == None:
        print("El turno no existe")
        Utils.TiempoSleep("el menú de turnos")
        Utils.VolverMenuTurnos()
    
    idDoctorOriginal = datosTurno[3]
    fechaOriginal = datosFecha[1]
    horaOriginal = datosFecha[2]

    pacienteOriginal = BuscarPacienteDelTurno(datosTurno[2])
    doctorOriginal = BuscarDoctorDelTurno(idDoctorOriginal)

    print("Datos del turno a actualizar: ")
    print("ID del turno: ", idTurno)
    print("Paciente: ", pacienteOriginal)
    print("Doctor: ", doctorOriginal)
    print("Fecha: ", fechaOriginal)
    print("Hora: ", horaOriginal)

    print("Ingrese los nuevos datos del turno: \n")
    datosActualizados = IngresarDatosParaActualizarTurno(idDoctorOriginal, fechaOriginal, horaOriginal)

    idDoctor = datosActualizados[0]
    fecha = datosActualizados[1]
    hora = datosActualizados[2]

    try:
        MetodosCRUD.CRUDActualizarTurno(idTurno, fecha, hora, idDoctor)
        print("Turno actualizado correctamente")
    except ValueError:
        print("Fecha y/u hora incorrecta")
        Utils.TiempoSleep("el menú de turnos")
        Utils.VolverMenuTurnos()

def USUARIOEliminarTurnosDeUnDoctor(idDoctor):
    turnosDelDoctor = MetodosCRUD.CRUDListarTurnosDeUnDoctor(idDoctor)
    if len(turnosDelDoctor) == 0:
        print("El doctor no tiene turnos programados")
        Utils.TiempoSleep("el menú de turnos")
        Utils.VolverMenuTurnos()
    
    print("TURNOS DEL DOCTOR: ")
    for turno in turnosDelDoctor:
        turnoIterado = tuple(turno)

        idTurnoFecha = turnoIterado[1]
        idPaciente = turnoIterado[2]
        idDoctor = turnoIterado[3]
        paciente = BuscarPacienteDelTurno(idPaciente)
        doctor = BuscarDoctorDelTurno(idDoctor)
        fechaHora = BuscarFechaHoraDelTurno(idTurnoFecha)

        print("ID del turno: ", idTurnoFecha)
        print("Paciente: ", paciente)
        print("Doctor: ", doctor)

        print("Fecha: ", fechaHora[1])
        print("Hora: ", fechaHora[2])
        print("\n")

    print("¿Desea eliminar los turnos del doctor? (s/n): ")
    opcion = 'j'
    while opcion != 's' and opcion != 'n':
        opcion = input().strip().lower()
        if opcion == "s":
            MetodosCRUD.CRUDEliminarTurnosDeUnDoctor(idDoctor)
            print("Turnos eliminados correctamente")
            Utils.TiempoSleep("el menú de turnos")
            Utils.VolverMenuTurnos()
        elif opcion == "n":
            print("No se eliminaron los turnos")
            Utils.TiempoSleep("el menú de turnos")
            Utils.VolverMenuTurnos()
        else:
            print("Por favor, ingrese una opción válida")

def USUARIOEliminarTurnosEnRangoDeFechas(fechaInicio, fechaFin):
    turnos = MetodosCRUD.CRUDListarTurnosPacientesDeUnRangoDeFechas(fechaInicio, fechaFin)
    if len(turnos) == 0:
        print("No hay turnos programados")
        Utils.TiempoSleep("el menú de turnos")
        Utils.VolverMenuTurnos()
    
    print("TURNOS PROGRAMADOS: ")
    for turno in turnos:
        turnoIterado = tuple(turno)

        idTurnoFecha = turnoIterado[1]
        idPaciente = turnoIterado[2]
        idDoctor = turnoIterado[3]
        paciente = BuscarPacienteDelTurno(idPaciente)
        doctor = BuscarDoctorDelTurno(idDoctor)
        fechaHora = BuscarFechaHoraDelTurno(idTurnoFecha)

        print("ID del turno: ", idTurnoFecha)
        print("Paciente: ", paciente)
        print("Doctor: ", doctor)

        print("Fecha: ", fechaHora[1])
        print("Hora: ", fechaHora[2])
        print("\n")

    print(f"¿Desea eliminar los turnos en el rango de fechas {fechaInicio} - {fechaFin}? (s/n): ")
    opcion = 'j'
    while opcion != 's' and opcion != 'n':
        opcion = input().strip().lower()
        if opcion == "s":
            MetodosCRUD.CRUDEliminarTurnosDeRangoDeFechas(fechaInicio, fechaFin)
            print("Turnos eliminados correctamente")
            Utils.TiempoSleep("el menú de turnos")
            Utils.VolverMenuTurnos()
        elif opcion == "n":
            print("No se eliminaron los turnos")
            Utils.TiempoSleep("el menú de turnos")
            Utils.VolverMenuTurnos()
        else:
            print("Por favor, ingrese una opción válida")

def USUARIOELIMINARTurnos():
    print("ELIMINAR TURNOS: ")
    print("Seleccione una opción: ")
    print("1. Eliminar turnos de un doctor")
    print("2. Eliminar turnos en un rango de fechas")
    print("3. Volver al menú de turnos")

    opcion = 'j'
    while opcion != '1' and opcion != '2' and opcion != '3':
        opcion = input().strip()
        if opcion == "1":
            idDoctor = IngresarIDDoctor()
            USUARIOEliminarTurnosDeUnDoctor(idDoctor)
        elif opcion == "2":
            print("Ingrese el rango de fechas para eliminar los turnos: ")
            print("Fecha de inicio: ")
            fechaInicio = IngresarFechaTurno()
            print("Fecha de fin: ")
            fechaFin = IngresarFechaTurno()
            USUARIOEliminarTurnosEnRangoDeFechas(fechaInicio, fechaFin)
        elif opcion == "3":
            Utils.VolverMenuTurnos()
        else:
            print("Por favor, ingrese una opción válida")