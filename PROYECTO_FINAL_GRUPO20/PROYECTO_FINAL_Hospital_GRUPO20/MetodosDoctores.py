from datetime import datetime
import DoctoresCRUD as MetodosCRUD
import Utils as Utils

# GESTIÓN DE DOCTORES

#METODO PARA OBTENER UNA LISTA CON LOS ID DE LOS DOCTORES
def ListaIDDoctores():
    doctores = MetodosCRUD.CRUDListarDoctores()
    listaID = []
    for doctor in doctores:   
        listaID.append(doctor[0])
    return listaID

# Método para buscar datos duplicados
def BuscarDatosDuplicados(doctorIngresado):
    doctores = MetodosCRUD.CRUDListarDoctores()
    noHayDuplicados = (False, "")
    for doctor in doctores:
        doctorDuplicado = (doctorIngresado[0] == doctor[1] and doctorIngresado[3] == doctor[4])
        telefonoDuplicado = doctorIngresado[1] == doctor[2]
        if telefonoDuplicado:
            return (True, "telefono")
        elif doctorDuplicado:
            return (True, "doctor")
    return noHayDuplicados



# Método para agregar un nuevo doctor
def IngresarDatosDoctor():
    doctorCorrecto = False
    datosDoctor = ()

    while not doctorCorrecto:
        listaErrores = []


        nombre = input("\nIngrese el nombre del doctor: ").strip()
        direccion = input("\nIngrese la dirección del doctor: ").strip()
        especialidad = input("\nIngrese la especialidad del doctor: ").strip()

        try:
            entradaTelefono = input("\nIngrese el teléfono del doctor (solo 9 o 10 dígitos): ").strip()
            if entradaTelefono == "":
                listaErrores.append("Por favor, llene el campo de telefono")
            else:
                telefono = int(entradaTelefono)
                if len(str(telefono)) < 9 or len(str(telefono)) > 10:
                    listaErrores.append("El número de teléfono debe tener 9 o 10 dígitos")
        except ValueError:
            listaErrores.append("Por favor, ingrese un número de teléfono válido")


        if not nombre:
            listaErrores.append("Por favor, llene el campo de nombre")
        if not direccion:
            listaErrores.append("Por favor, llene el campo de direccion")
        if not especialidad:
            listaErrores.append("Por favor, llene el campo de especialidad")


        if listaErrores:
            Utils.LimpiarConsola()
            print("Errores detectados:")
            for error in listaErrores:
                print(f"- {error}")
            print("\nIntento finalizado con errores. Intente nuevamente...\n")
        else:
            doctorCorrecto = True
            print("\nIntento finalizado correctamente. Datos del doctor: ")
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {telefono}")
            print(f"Dirección: {direccion}")
            print(f"Especialidad: {especialidad}")
            print("\n")
            
    datosDoctor = (nombre, telefono, direccion, especialidad)

    return datosDoctor

#METODO PARA AGREGAR UN DOCTOR
def USUARIOAgregarDoctor():
    datosDoctor = ()
    Utils.LimpiarConsola()

    print("AGREGAR NUEVO DOCTOR...\n")
    print("Por favor, llene los siguientes campos:\n")
    datosDoctor = IngresarDatosDoctor()

    return datosDoctor

# Método para listar todos los doctores
def USUARIOListarDoctores():
    doctores = MetodosCRUD.CRUDListarDoctores()

    if doctores is None or len(doctores) == 0:
        print("No hay doctores para mostrar.")
        Utils.TiempoSleep("el menú principal")
        Utils.VolverMenuPrincipal()
    else:
        Utils.LimpiarConsola()
        print("LISTA DE DOCTORES...\n")
        for doctor in doctores:
            print(f"ID: {doctor[0]} - Nombre: {doctor[1]} - Telefono: {doctor[2]} - Direccion: {doctor[3]} - Especialidad: {doctor[4]}")
        print("\n")
    
    return doctores

# Método para actualizar la información de un doctor
def USUARIOModificarDoctor():

    datosDoctorModificado = ()
    doctores = MetodosCRUD.CRUDListarDoctores()
    cantidadDoctores = doctores.__len__()
    Utils.LimpiarConsola()

    if cantidadDoctores == 0:
        Utils.LimpiarConsola()
        print("No hay doctores para mostrar.")
        Utils.TiempoSleep("el menú principal")
        Utils.VolverMenuPrincipal()
    else:
        print("HA SELECCIONADO LA OPCION DE MODIFICAR DOCTOR... ")
        print("Lista de doctores: \n")
        for doctor in doctores:
            print(f"ID: {doctor[0]} - Nombre: {doctor[1]} - Telefono: {doctor[2]} - Direccion: {doctor[3]} - Especialidad: {doctor[4]}")
        print("\n")
        
        try:
            entradaIdDoctor = input("\nIngrese el ID del doctor a modificar: ").strip()

            if entradaIdDoctor == "":
                Utils.LimpiarConsola()
                print("Por favor, ingrese un ID de doctor")
                Utils.TiempoSleep("menu de doctores")
                Utils.VolverMenuDoctores()
            else:
                idDoctor = int(entradaIdDoctor)
                listaIds = ListaIDDoctores()
                if not idDoctor in listaIds:
                    Utils.LimpiarConsola()
                    print("El id ingresado no existe. Por favor, ingrese un ID válido")
                    Utils.TiempoSleep("menu de doctores")
                    Utils.VolverMenuDoctores()
                    pass

                print("Datos actuales del doctor: ")
                doctor = MetodosCRUD.CRUDVerDetalleDoctor(idDoctor)
                idDoctor = doctor[0]
                print(f"ID: {doctor[0]} - Nombre: {doctor[1]} - Telefono: {doctor[2]} - Direccion: {doctor[3]} - Especialidad: {doctor[4]}")
                print("\n")
                print("Ingrese los nuevos datos del doctor: ")
                datosIngresados = IngresarDatosDoctor()
                listaDatos = list(datosIngresados)
                listaDatos.insert(0, idDoctor)
                datosDoctorModificado = tuple(listaDatos)
        except ValueError:
            Utils.LimpiarConsola()
            print("Por favor, ingrese solo dígitos")
            Utils.TiempoSleep("menu de doctores")
            Utils.VolverMenuDoctores()

        datosDuplicados = BuscarDatosDuplicados(datosDoctorModificado)

        if datosDuplicados[0]:
            if datosDuplicados[1] == "telefono":
                Utils.LimpiarConsola()
                print("El teléfono ingresado ya está registrado. Por favor, ingrese otro teléfono")
                Utils.TiempoSleep("menu de doctores")
                Utils.VolverMenuDoctores()
            elif datosDuplicados[1] == "doctor":
                Utils.LimpiarConsola()
                print("El doctor ingresado ya está registrado. Por favor, ingrese otro doctor")
                Utils.TiempoSleep("menu de doctores")
                Utils.VolverMenuDoctores()
        else:
            Utils.LimpiarConsola()
            print("Datos del doctor modificados correctamente: ")
            print(f"ID: {datosDoctorModificado[0]} - Nombre: {datosDoctorModificado[1]} - Telefono: {datosDoctorModificado[2]} - Direccion: {datosDoctorModificado[3]} - Especialidad: {datosDoctorModificado[4]}")
            MetodosCRUD.CRUDModificarDoctor(datosDoctorModificado[0], datosDoctorModificado[1], datosDoctorModificado[2], datosDoctorModificado[3], datosDoctorModificado[4])
            print("\n")

# Método para listar detalles de un doctor específico
def USUARIOVerDetalleDoctor():
    Utils.LimpiarConsola()
    
    print("VER DETALLES DE UN DOCTOR...\n")

    while True:
        try:
            entradaIdDoctor = input("Ingrese el ID del doctor a ver detalles: ").strip()
            if entradaIdDoctor == "":
                Utils.LimpiarConsola()
                print("Por favor, ingrese un ID de doctor")
            else:
                idDoctor = int(entradaIdDoctor)
                listaIds = ListaIDDoctores()
                if not idDoctor in listaIds:
                    Utils.LimpiarConsola()
                    print("El id ingresado no existe. Por favor, ingrese un ID válido")
                else:
                    doctor = MetodosCRUD.CRUDVerDetalleDoctor(idDoctor)
                    print(f"ID: {doctor[0]} - Nombre: {doctor[1]} - Telefono: {doctor[2]} - Direccion: {doctor[3]} - Especialidad: {doctor[4]}")
                    break
        except ValueError:
            Utils.LimpiarConsola()
            print("Por favor, ingrese solo dígitos")
    

# Método para listar doctores según especialidad
def USUARIOBusquedaAvanzadaDoctores():
    Utils.LimpiarConsola()
    opcionFiltro = "nada"

    print("BUSQUEDA AVANZADA DE DOCTORES...\n")
    while(opcionFiltro != 'e' and opcionFiltro != 'E' and opcionFiltro != 'n' and opcionFiltro != 'N' and opcionFiltro != 'i' and opcionFiltro != 'I'):
        opcionFiltro = input("Desea buscar doctores por nombre? (n/N) Desea buscar doctores por especialidad? (e/E)").strip()
        if (opcionFiltro == 'n' or opcionFiltro == 'N'):
            opcionFiltro = 'J'
            USUARIOFiltrarDoctoresPorNombre()
            break
            
        elif (opcionFiltro == 'e' or opcionFiltro == 'E'):
            opcionFiltro = 'J'
            USUARIOFiltrarDoctoresPorEspecialidad()
            break

        else:
            Utils.LimpiarConsola()
            opcionFiltro = 'J'
            print("Por favor, ingrese una opción válida")
            Utils.TiempoSleep("intentar")
            USUARIOBusquedaAvanzadaDoctores()
            break

def USUARIOFiltrarDoctoresPorNombre():
    nombre = ""
    print("Ingrese el nombre del doctor a buscar: ")
    
    while True:
        nombre = input("Nombre: ").strip()
        if nombre == "":
            Utils.LimpiarConsola()
            print("Por favor, ingrese un nombre. Intente nuevamente...")
        else:
            doctores = MetodosCRUD.CRUDListarDoctoresPorNombre(nombre)
            if not doctores:
                print(f"No se encontraron doctores con el nombre '{nombre}'. Intente nuevamente...")
            else:
                print(f"\nDoctores con nombre '{nombre}':")
                for doctor in doctores:
                    print(f"ID: {doctor[0]} - Nombre: {doctor[1]} - Teléfono: {doctor[2]} - Dirección: {doctor[3]} - Especialidad: {doctor[4]}")
            break
    

def USUARIOFiltrarDoctoresPorEspecialidad():
    print("Especialidades disponibles:")
    especialidades = MetodosCRUD.CRUDListarTodasLasEspecialidades()
    for especialidad in especialidades:
        print(f"- {especialidad}")

    print("\n")
    especialidad = input("Ingrese la especialidad a buscar: ").strip()

    while True:
        if especialidad == "":
            Utils.LimpiarConsola()
            print("Por favor, ingrese una especialidad. Intente nuevamente...")
        else:
            doctores = MetodosCRUD.CRUDListarDoctoresPorEspecialidad(especialidad)
            if not doctores:
                print(f"No se encontraron doctores con la especialidad '{especialidad}'. Intente nuevamente...")
            else:
                print(f"\nDoctores con especialidad '{especialidad}':")
                for doctor in doctores:
                    print(f"ID: {doctor[0]} - Nombre: {doctor[1]} - Teléfono: {doctor[2]} - Dirección: {doctor[3]} - Especialidad: {doctor[4]}")
            break

# Método para listar doctores con más turnos
def USUARIODoctoresConMasTurnos():
    doctores = MetodosCRUD.CRUDDoctoresConMasTurnos()
    if not doctores:
        print("No se encontraron doctores con turnos asignados.")
        Utils.TiempoSleep("el menú principal")
        Utils.VolverMenuPrincipal()
    else:
        Utils.LimpiarConsola()
        print("DOCTORES CON MÁS TURNOS...\n")
        for doctor in doctores:
            doctorIterado = tuple(doctor)
            print(f"ID: {doctorIterado[0]} - Nombre: {doctorIterado[1]} - Especialidad: {doctorIterado[2]} - Turnos: {doctorIterado[3]}")
        print("\n")

