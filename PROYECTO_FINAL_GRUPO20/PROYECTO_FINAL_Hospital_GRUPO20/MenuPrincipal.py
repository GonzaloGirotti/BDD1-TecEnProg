import Utils as Utils
import MetodosPacientes as MetodosPacientes
import MetodosDoctores as MetodosDoctores
import PacientesCRUD as MetodosCRUDPacientes
import DoctoresCRUD as MetodosCRUDDoctores
import MetodosTurnos as MetodosTurnos
import TurnosCRUD as MetodosCRUDTurnos

def MostrarMenuPrincipal():
    Utils.LimpiarConsola()

    print("BIENVENIDO AL SISTEMA DE GESTION DE TURNOS DEL HOSPITAL!")
    print("Ingrese una opcion: ")
    print("1. Menu pacientes")
    print("2. Menu doctores")
    print("3. Menu turnos")
    print("4. Salir")
    
    opcion = 0

    while True:
        try:
            opcion = int(input("Ingrese una opcion del 1 al 4: "))

            if opcion < 1 or opcion > 4:
                Utils.LimpiarConsola()
                print("Por favor, ingrese una opción válida  (1-4)")
                Utils.TiempoSleep("el menú principal")
                MostrarMenuPrincipal()
                pass
        except ValueError:
            Utils.LimpiarConsola()
            print("Por favor, ingrese un número entero")
            Utils.TiempoSleep("el menú principal")
            MostrarMenuPrincipal()
            pass

        if opcion == 1:
            MostrarMenuPacientes()
        elif opcion == 2:
            MostrarMenuDoctores()
        elif opcion == 3:
            MostrarMenuTurnos()
        elif opcion == 4:
            print("Gracias por usar el sistema")
            break
        else:
            print(f"Opcion invalida, intente de nuevo \n")
            


def MostrarMenuPacientes():
    Utils.LimpiarConsola()

    print("MENU PACIENTES: ")
    print("Ingrese una opcion: ")
    print("\t 1. Agregar paciente")
    print("\t 2. Busqueda avanzada de pacientes")
    print("\t 3. Modificar paciente")
    print("\t 4. Eliminar paciente")
    print("\t 5. Listar todos los pacientes")
    print("\t 6. Volver al menu principal")
    print("")

    opcion = 0

    try:
        entradaOpcion = input("Ingrese una opcion del 1 al 6: ").strip()
        if entradaOpcion == "":
            print("Opcion no ingresada")
            Utils.TiempoSleep("el menú de pacientes")
            MostrarMenuPacientes()
        else:
            opcion = int(entradaOpcion)
            if opcion < 1 or opcion > 6:
                print("Opcion no existente")
                Utils.TiempoSleep("el menú de pacientes")
                MostrarMenuPacientes()
    except ValueError:
        print("Por favor, ingrese un número entero")
        Utils.TiempoSleep("el menú de pacientes")
        MostrarMenuPacientes()

    SeleccionMenuPacientes(opcion)



def SeleccionMenuPacientes(opcion):
    if opcion == 1:
        datosNuevoPaciente = MetodosPacientes.USUARIOAgregarPaciente() #ARRANCA LA FUNCION AGREGAR PACIENTE
        nombrePaciente = datosNuevoPaciente[0]
        fechaNacimientoPaciente = datosNuevoPaciente[1]
        telefonoPaciente = datosNuevoPaciente[2]
        direccionPaciente = datosNuevoPaciente[3]
        MetodosCRUDPacientes.CRUDAgregarPaciente(nombrePaciente, fechaNacimientoPaciente, telefonoPaciente, direccionPaciente)
        volver = input("Desea agregar otro paciente? S/N \n").strip()
        if volver.lower() == "s":
            Utils.TiempoSleep("AGREGAR PACIENTE")
            SeleccionMenuPacientes(1)
        else:
            Utils.PreguntaVolverAlMenuAnterior("MenuPacientes")

    elif opcion == 2:
        MetodosPacientes.USUARIOBusquedaAvanzadaPacientes()
        volver = input("Desea buscar otro paciente? S/N \n").strip()
        if volver.lower() == "s":
            Utils.TiempoSleep("BUSCAR PACIENTE")
            SeleccionMenuPacientes(2)
        else:
            Utils.PreguntaVolverAlMenuAnterior("MenuPacientes")

    elif opcion == 3:
        MetodosPacientes.USUARIOModificarPaciente()
        volver = input("Desea modificar otro paciente? S/N \n").strip()
        if volver.lower() == "s":
            Utils.TiempoSleep("MODIFICAR PACIENTE")
            SeleccionMenuPacientes(3)
        else:
            Utils.PreguntaVolverAlMenuAnterior("MenuPacientes")

    elif opcion == 4:
        MetodosPacientes.USUARIOEliminarPaciente()
        volver = input("Desea eliminar otro paciente? S/N \n").strip()
        if volver.lower() == "s":
            Utils.TiempoSleep("ELIMINAR PACIENTE")
            SeleccionMenuPacientes(4)
        else:
            Utils.PreguntaVolverAlMenuAnterior("MenuPacientes")

    elif opcion == 5:
        MetodosPacientes.USUARIOListarPacientes()
        Utils.TiempoSleep("el menú principal")
        MostrarMenuPrincipal()
    
    elif opcion == 6:
        MostrarMenuPrincipal()



def MostrarMenuDoctores():
    Utils.LimpiarConsola()
    
    print("MENU DOCTORES: ")
    print("Ingrese una opcion: ")
    print("\t 1. Agregar doctor")
    print("\t 2. Busqueda avanzada de doctores")
    print("\t 3. Modificar doctor")
    print("\t 4. Listar todos los doctores")
    print("\t 5. Reporte de doctores con mas turnos")
    print("\t 6. Volver al menú principal")

    opcion = 0

    try:
        entradaOpcion = input("Ingrese una opcion del 1 al 6: ").strip()
        if entradaOpcion == "":
            print("Opcion no ingresada")
            Utils.TiempoSleep("el menu de doctores")
            MostrarMenuDoctores()
        else:
            opcion = int(entradaOpcion)
            if opcion < 1 or opcion > 6:
                print("Opcion no existente")
                Utils.TiempoSleep("el menu de doctores")
                MostrarMenuDoctores()
    except ValueError:
        print("Por favor, ingrese un número entero")
        Utils.TiempoSleep("el menu de doctores")
        MostrarMenuDoctores()

    SeleccionMenuDoctores(opcion)



def SeleccionMenuDoctores(opcion):
    if opcion == 1:
        datosNuevoDoctor = MetodosDoctores.USUARIOAgregarDoctor()
        nombreDoctor = datosNuevoDoctor[0]
        telefonoDoctor = datosNuevoDoctor[1]
        direccionDoctor = datosNuevoDoctor[2]
        especialidadDoctor = datosNuevoDoctor[3]
        MetodosCRUDDoctores.CRUDAgregarDoctor(nombreDoctor, telefonoDoctor, direccionDoctor, especialidadDoctor)
        volver = input("Desea agregar otro doctor? S/N \n").strip()
        if volver.lower() == "s":
            Utils.TiempoSleep("AGREGAR DOCTOR")
            SeleccionMenuDoctores(1)
        else:
            Utils.PreguntaVolverAlMenuAnterior("MenuDoctores")
    elif opcion == 2:
        MetodosDoctores.USUARIOBusquedaAvanzadaDoctores()
        volver = input("Desea buscar otro doctor? S/N \n").strip()
        if volver.lower() == "s":
            Utils.TiempoSleep("BUSCAR DOCTOR")
            SeleccionMenuDoctores(2)
        else:
            Utils.PreguntaVolverAlMenuAnterior("MenuDoctores")
    elif opcion == 3:
        MetodosDoctores.USUARIOModificarDoctor()
        volver = input("Desea modificar otro doctor? S/N \n").strip()
        if volver.lower() == "s":
            Utils.TiempoSleep("MODIFICAR DOCTOR")
            SeleccionMenuDoctores(3)
        else:
            Utils.PreguntaVolverAlMenuAnterior("MenuDoctores")
    elif opcion == 4:
        MetodosDoctores.USUARIOListarDoctores()
        Utils.TiempoSleep("el menú principal")
        MostrarMenuPrincipal()
    elif opcion == 5:
        MetodosDoctores.USUARIODoctoresConMasTurnos()
        Utils.TiempoSleep("el menú principal")
        MostrarMenuPrincipal()
    elif opcion == 6:
        MostrarMenuPrincipal()



def MostrarMenuTurnos():
    Utils.LimpiarConsola()

    print("MENU TURNOS: ")
    print("Ingrese una opción: ")
    print("\t 1. Programar turno")
    print("\t 2. Actualizar turno")
    print("\t 3. Cancelar turno")
    print("\t 4. Volver al menú principal")

    opcion = 0

    try:
        entradaOpcion = input("Ingrese una opcion del 1 al 4: ").strip()
        if entradaOpcion == "":
            print("Opcion no ingresada")
            Utils.TiempoSleep("el menu de turnos")
            MostrarMenuTurnos()
        else:
            opcion = int(entradaOpcion)
            if opcion < 1 or opcion > 4:
                print("Opcion no existente")
                Utils.TiempoSleep("el menu de turnos")
                MostrarMenuTurnos()
    except ValueError:
        print("Por favor, ingrese un número entero")
        Utils.TiempoSleep("el menu de turnos")
        MostrarMenuTurnos()

    SeleccionMenuTurnos(opcion)

def SeleccionMenuTurnos(opcion):
    if opcion == 1:
        MetodosTurnos.USUARIOProgramarTurno()
        volver = input("Desea programar otro turno? S/N \n").strip()
        if volver.lower() == "s":
            Utils.TiempoSleep("PROGRAMAR TURNO")
            SeleccionMenuTurnos(1)
        else:
            Utils.PreguntaVolverAlMenuAnterior("MenuTurnos")
    elif opcion == 2:
        MetodosTurnos.USUARIOActualizarTurno()
        volver = input("Desea actualizar otro turno? S/N \n").strip()
        if volver.lower() == "s":
            Utils.TiempoSleep("ACTUALIZAR TURNO")
            SeleccionMenuTurnos(2)
        else:
            Utils.PreguntaVolverAlMenuAnterior("MenuTurnos")
    elif opcion == 3:
        MetodosTurnos.USUARIOELIMINARTurnos()
        volver = input("Desea cancelar otro turno? S/N \n").strip()
        if volver.lower() == "s":
            Utils.TiempoSleep("CANCELAR TURNO")
            SeleccionMenuTurnos(3)
        else:
            Utils.PreguntaVolverAlMenuAnterior("MenuTurnos")
    elif opcion == 4:
        MostrarMenuPrincipal()