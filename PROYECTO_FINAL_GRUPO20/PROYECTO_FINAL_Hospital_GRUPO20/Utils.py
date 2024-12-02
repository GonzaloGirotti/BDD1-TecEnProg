import os

#METODO PARA LIMPIAR LA CONSOLA
def LimpiarConsola():
    os.system('cls')

#METODO PARA VALIDAR ID
def ValidarID(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Por favor, ingrese un ID mayor a 0")
            else:
                return valor
        except ValueError:
            print("Por favor, ingrese solo dígitos")

#METODO PARA VALIDAR TELEFONO DE 9 o 10 DIGITOS
def ValidarTelefono(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 100000000 or valor > 9999999999:
                print("Por favor, ingrese un número de teléfono válido")
            else:
                return valor
        except ValueError:
            print("Por favor, ingrese solo dígitos")
        



#METODO PARA PONER 3 SEGUNDOS DE ESPERA
def TiempoSleep(mensaje):
    import time
    input("Presione cualquier tecla para continuar...")
    print(f"Volviendo a {mensaje} en 3 segundos...")
    time.sleep(3)

def VolverMenuPrincipal():
    import MenuPrincipal
    MenuPrincipal.MostrarMenuPrincipal()

def VolverMenuPacientes():
    import MenuPrincipal
    MenuPrincipal.MostrarMenuPacientes()

def VolverMenuDoctores():
    import MenuPrincipal
    MenuPrincipal.MostrarMenuDoctores()

def VolverMenuTurnos():
    import MenuPrincipal
    MenuPrincipal.MostrarMenuTurnos()

#Corroborar que la fecha del turno sea mas adelante que hoy
def CorroborarFechaRealParaTurno(fecha):
    from datetime import datetime
    fecha = datetime.strptime(fecha, "%Y-%m-%d")
    fechaActual = datetime.now()
    if fecha < fechaActual:
        return False
    return True



def PreguntaVolverAlMenuAnterior(menuAnteriorNombre):
    entrada = input("Desea volver al menú anterior? S / cualquier caracter para salir del programa: ").strip()
    if entrada.lower() == "s":
        if menuAnteriorNombre == "MenuPrincipal":
            TiempoSleep("el menú principal")
            VolverMenuPrincipal()
        elif menuAnteriorNombre == "MenuPacientes":
            TiempoSleep("el menú de pacientes")
            VolverMenuPacientes()
        elif menuAnteriorNombre == "MenuDoctores":
            TiempoSleep("el menú de doctores")
            VolverMenuDoctores()
        elif menuAnteriorNombre == "MenuTurnos":
            TiempoSleep("el menú de turnos")
            VolverMenuTurnos()
    else:
        print("Gracias por usar el sistema")
        exit()