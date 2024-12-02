import mysql.connector
import Conexion_BD.conexion_db as Conexion_BD

# Conexión a la base de datos
mydb = Conexion_BD.DatosDeConexion()



def CRUDListarPacientes():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Pacientes")
    resultados = cursor.fetchall()
    pacientes = []
    for item in resultados:
        pacientes.append(item)
    cursor.close()
    return pacientes

def CRUDAgregarPaciente(nombre, fechaNacimiento, telefono, direccion):
    cursor = mydb.cursor()
    sql = 'INSERT INTO Pacientes (Paciente_Nombre, Paciente_FechaNacimiento, Paciente_Telefono, Paciente_Direccion) VALUES (%s, %s, %s, %s)'
    valores = (nombre,  fechaNacimiento, telefono, direccion)
    cursor.execute(sql, valores)
    mydb.commit()
    cursor.close()

def CRUDModificarPaciente(id, nombre, fechaNacimiento, telefono, direccion):
    cursor = mydb.cursor()
    sql = 'UPDATE Pacientes SET Paciente_Nombre=%s, Paciente_FechaNacimiento = %s, Paciente_Telefono = %s, Paciente_Direccion = %s WHERE Paciente_ID = %s'
    valores = (nombre, fechaNacimiento, telefono, direccion, id)
    cursor.execute(sql, valores)
    mydb.commit()
    print("Paciente modificado con éxito!")
    cursor.close()


def CRUDEliminarPaciente(id):
    cursor = mydb.cursor()
    sql = f'DELETE FROM Pacientes WHERE Paciente_ID = {id}'
    cursor.execute(sql)
    mydb.commit()
    print("Paciente eliminado con éxito!")
    cursor.close()

def CRUDBuscarUnPaciente(id):
    cursor = mydb.cursor()
    sql = f'SELECT * FROM Pacientes WHERE Paciente_ID = {id}'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado

def CRUDBuscarPaciente(nombre, id):
    cursor = mydb.cursor()
    
    if id == "":
        sql = f'SELECT * FROM Pacientes WHERE Paciente_Nombre LIKE "%{nombre}%"'
    else:
        sql = f'SELECT * FROM Pacientes WHERE Paciente_ID = {id}'

    cursor.execute(sql)
    resultados = cursor.fetchall()

    pacientes = []

    for paciente in resultados:
        pacientes.append(paciente)


    cursor.close()

    return pacientes