import mysql.connector

#INSERTE SUS DATOS DE CONEXIÓN AQUÍ
#INSERTE SUS DATOS DE CONEXIÓN AQUÍ
#INSERTE SUS DATOS DE CONEXIÓN AQUÍ
mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)
#INSERTE SUS DATOS DE CONEXIÓN AQUÍ
#INSERTE SUS DATOS DE CONEXIÓN AQUÍ
#INSERTE SUS DATOS DE CONEXIÓN AQUÍ

def DatosDeConexion():
    return mydb

mycursor = mydb.cursor()

if mydb.is_connected():
    print("Conexión exitosa")
else:
    print("No se pudo conectar")

def LlamarProcedimientoCrearTablas():
    mycursor.callproc("CrearTablas", ())
    mydb.commit()
    print("Tablas creadas")

def LlamarProcedimientoCargarDatos():
    mycursor.callproc("InsertarDatos", ())
    mydb.commit()
    print("Datos cargados")

def InicializarDatabase():
    LlamarProcedimientoCrearTablas()
    LlamarProcedimientoCargarDatos()