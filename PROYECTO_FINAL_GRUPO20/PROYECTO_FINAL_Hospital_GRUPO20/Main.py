import MenuPrincipal as MenuPrincipal
import Conexion_BD.conexion_db as Conexion_BD

def IniciarPrograma():
    Conexion_BD.InicializarDatabase()
    MenuPrincipal.MostrarMenuPrincipal()

IniciarPrograma()