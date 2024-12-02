from datetime import datetime
import PacientesCRUD as MetodosCRUD
import Utils as Utils

#METODO PARA OBTENER UNA LISTA CON LOS ID DE LOS PACIENTES
def ListaIDPacientes():
    pacientes = MetodosCRUD.CRUDListarPacientes()
    listaID = []
    for paciente in pacientes:
        listaID.append(paciente[0])
    return listaID

#METODO PARA CORROBORAR TELEFONO DUPLICADO:
def CorroborarTelefonoDuplicado(telefono):
    pacientes = MetodosCRUD.CRUDListarPacientes()
    for paciente in pacientes:
        if paciente[3] == telefono:
            return True
    return False


def IngresarDatosPaciente():

    pacienteCorrecto = False
    datos = ()

    while not pacienteCorrecto:
        listaErrores = []


        nombre = input("\nIngrese el nombre del paciente: ").strip()
        direccion = input("\nIngrese la dirección del paciente: ").strip()
        

        try:
            entradaFecha = input("\nIngrese la fecha de nacimiento del paciente (YYYY-MM-DD): ").strip()
            if entradaFecha == "":
                listaErrores.append("Por favor, llene el campo de fecha de nacimiento")
            else:
                fechanacimiento = datetime.strptime(entradaFecha, "%Y-%m-%d")
                if fechanacimiento > datetime.now():
                    listaErrores.append("Por favor, ingrese una fecha de nacimiento real")
        except ValueError:
            listaErrores.append("Por favor, ingrese una fecha de nacimiento válida (YYYY-MM-DD)")

        try:
            entradaTelefono = input("\nIngrese el teléfono del paciente (solo 9 o 10 dígitos): ").strip()
            if entradaTelefono == "":
                listaErrores.append("Por favor, llene el campo de teléfono")
            else:
                telefono = int(entradaTelefono)
                if len(str(telefono)) < 9 or len(str(telefono)) > 10:
                    listaErrores.append("El número de teléfono debe tener 9 o 10 dígitos")
        except ValueError:
            listaErrores.append("Por favor, ingrese un número de teléfono válido")


        if not nombre:
            listaErrores.append("Por favor, llene el campo de nombre")
        if not direccion:
            listaErrores.append("Por favor, llene el campo de dirección")


        if listaErrores:
            Utils.LimpiarConsola()
            print("Errores detectados:")
            for error in listaErrores:
                print(f"- {error}")
            print("\nIntento finalizado con errores. Intente nuevamente...\n")
        else:
            pacienteCorrecto = True
            print("\nIntento finalizado correctamente. Datos del paciente: ")
            print(f"Nombre: {nombre}")
            print(f"Fecha de nacimiento: {entradaFecha}")
            print(f"Teléfono: {telefono}")
            print(f"Dirección: {direccion}")
            print("\n")
            
    datos = (nombre, fechanacimiento, telefono, direccion)

    return datos

#METODO PARA AGREGAR UN PACIENTE
def USUARIOAgregarPaciente():
    datosPaciente = ()
    Utils.LimpiarConsola()

    print("AGREGAR NUEVO PACIENTE...\n")
    print("Por favor, llene los siguientes campos:\n")
    datosPaciente = IngresarDatosPaciente()

    return datosPaciente

#METODO PARA ELIMINAR UN PACIENTE
def USUARIOEliminarPaciente():


    pacientes = MetodosCRUD.CRUDListarPacientes()
    cantidadPacientes = len(pacientes)
    Utils.LimpiarConsola()

    if cantidadPacientes == 0:
        Utils.LimpiarConsola()
        print("No hay pacientes para mostrar.")
        Utils.TiempoSleep("el menú principal")
        Utils.VolverMenuPrincipal()
    else:
        print("HA SELECCIONADO LA OPCION DE ELIMINAR PACIENTE... ")
        print("Lista de pacientes: \n")
        for paciente in pacientes:
            print(f"ID: {paciente[0]} - Nombre: {paciente[1]} - Fecha de nacimiento: {paciente[2]} - Teléfono: {paciente[3]} - Dirección: {paciente[4]}")
        print("\n")
        
        try:
            entradaIdPaciente = input("\nIngrese el ID del paciente a eliminar: ").strip()

            if entradaIdPaciente == "":
                Utils.LimpiarConsola()
                print("Por favor, ingrese un ID de paciente")
                Utils.TiempoSleep("intentar")
                USUARIOEliminarPaciente()
            else:
                idPaciente = int(entradaIdPaciente)
                listaIds = ListaIDPacientes()
                if not idPaciente in listaIds:
                    Utils.LimpiarConsola()
                    print("El id ingresado no existe. Por favor, ingrese un ID válido")
                    Utils.TiempoSleep("intentar")
                    USUARIOEliminarPaciente()
                    pass

                MetodosCRUD.CRUDEliminarPaciente(idPaciente)
        except ValueError:
            Utils.LimpiarConsola()
            print("Por favor, ingrese solo dígitos")
            Utils.TiempoSleep("intentar")
            USUARIOEliminarPaciente()


#METODO PARA LISTAR LOS PACIENTES
def USUARIOListarPacientes():

    pacientes = MetodosCRUD.CRUDListarPacientes()

    if pacientes is None or len(pacientes) == 0:
        print("No hay pacientes para mostrar.")
        Utils.TiempoSleep("el menú principal")
        Utils.VolverMenuPrincipal()
    else:
        Utils.LimpiarConsola()
        print("LISTA DE PACIENTES: \n")
        for paciente in pacientes:
            print(f"ID: {paciente[0]} - Nombre: {paciente[1]} - Fecha de nacimiento: {paciente[2]} - Teléfono: {paciente[3]} - Dirección: {paciente[4]} ")
    
    print("\n")
    
    return pacientes

def USUARIOModificarPaciente():
    pacientes = MetodosCRUD.CRUDListarPacientes()
    cantidadPacientes = len(pacientes)
    Utils.LimpiarConsola()

    if cantidadPacientes == 0:
        Utils.LimpiarConsola()
        print("No hay pacientes para mostrar.")
        Utils.TiempoSleep("el menú principal")
        Utils.VolverMenuPrincipal()
    else:
        print("HA SELECCIONADO LA OPCION DE MODIFICAR PACIENTE... ")
        print("Lista de pacientes: \n")
        for paciente in pacientes:
            print(f"ID: {paciente[0]} - Nombre: {paciente[1]} - Fecha de nacimiento: {paciente[2]} - Teléfono: {paciente[3]} - Dirección: {paciente[4]}")
        print("\n")
        
        try:
            entradaIdPaciente = input("\nIngrese el ID del paciente a modificar: ").strip()

            if entradaIdPaciente == "":
                Utils.LimpiarConsola()
                print("Por favor, ingrese un ID de paciente")
                Utils.TiempoSleep("menu de pacientes")
                Utils.VolverMenuPacientes()
                pass
            else:
                idPaciente = int(entradaIdPaciente)
                listaIds = ListaIDPacientes()
                if not idPaciente in listaIds:
                    Utils.LimpiarConsola()
                    print("El id ingresado no existe. Por favor, ingrese un ID válido")
                    Utils.TiempoSleep("menu de pacientes")
                    Utils.VolverMenuPacientes()
                    pass

                paciente = MetodosCRUD.CRUDBuscarUnPaciente(idPaciente)
                print("\nDatos del paciente a modificar: ")
                print(f"ID: {paciente[0][0]} - Nombre: {paciente[0][1]} - Fecha de nacimiento: {paciente[0][2]} - Teléfono: {paciente[0][3]} - Dirección: {paciente[0][4]} \n")
                datosPaciente = IngresarDatosPaciente()
                datosPaciente = (idPaciente,) + datosPaciente
                MetodosCRUD.CRUDModificarPaciente(datosPaciente[0], datosPaciente[1], datosPaciente[2], datosPaciente[3], datosPaciente[4])
        except ValueError:
            Utils.LimpiarConsola()
            print("Por favor, ingrese solo dígitos")
            Utils.TiempoSleep("menu de pacientes")
            Utils.VolverMenuPacientes()
            pass

def USUARIOBusquedaAvanzadaPacientes():
    opcion = 0
    filtros = ()
    Utils.LimpiarConsola()

    print("HA SELECCIONADO LA OPCION DE BUSCAR PACIENTE... \n")
    print("Seleccione una opcion: ")
    print("\t 1. Buscar por nombre")
    print("\t 2. Buscar por ID")

    while opcion < 1 or opcion > 2:
        try:
            opcion = int(input("\nIngrese una opcion: ").strip())
        except ValueError:
            Utils.LimpiarConsola()
            print("Por favor, ingrese solo dígitos")

    if opcion == 1:
        nombre = input("\nIngrese el nombre del paciente: ").strip()
        filtros = (nombre, "")
    else:
        try:
            idPaciente = int(input("\nIngrese el ID del paciente: ").strip())
            filtros = ("", idPaciente)
        except ValueError:
            Utils.LimpiarConsola()
            print("Por favor, ingrese solo dígitos")
            USUARIOBusquedaAvanzadaPacientes()

    if filtros != ():
        pacientes = MetodosCRUD.CRUDBuscarPaciente(filtros[0], filtros[1])
    else:
        pacientes = None

    if pacientes is None or len(pacientes) == 0:
        print("No existe ningun paciente con ese ID / con ese nombre.")
    else:
        for paciente in pacientes:
            print(f"ID: {paciente[0]} - Nombre: {paciente[1]} - Fecha de nacimiento: {paciente[2]} - Teléfono: {paciente[3]} - Dirección: {paciente[4]} \n")