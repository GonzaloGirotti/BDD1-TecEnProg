import mysql.connector
import Conexion_BD.conexion_db as Conexion_BD

# Conexión a la base de datos
mydb = Conexion_BD.DatosDeConexion()

#Listar solo las especialidades
def CRUDListarTodasLasEspecialidades():
    cursor = mydb.cursor()
    cursor.execute("SELECT DISTINCT Doctor_Especialidad FROM Doctores")
    resultados = cursor.fetchall()
    especialidades = []
    for item in resultados:
        especialidades.append(item[0])
    cursor.close()
    return especialidades

# Listar todos los Doctores
def CRUDListarDoctores():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Doctores")
    resultados = cursor.fetchall()
    Doctores = []
    for item in resultados:
        Doctores.append(item)
    cursor.close()
    return Doctores

# Ver detalles de un doctor por ID
def CRUDVerDetalleDoctor(id):
    cursor = mydb.cursor()
    sql = "SELECT * FROM Doctores WHERE Doctor_ID = %s"
    cursor.execute(sql, (id,))
    resultado = cursor.fetchone()
    doctor = tuple(resultado)
    cursor.close()
    return doctor

# Agregar un doctor
def CRUDAgregarDoctor(nombre, telefono, direccion, especialidad):
    cursor = mydb.cursor()
    sql = 'INSERT INTO Doctores (Doctor_Nombre, Doctor_Telefono, Doctor_Direccion, Doctor_Especialidad) VALUES (%s, %s, %s, %s)'
    valores = (nombre, telefono, direccion, especialidad)
    cursor.execute(sql, valores)
    mydb.commit()
    print("Doctor agregado")
    cursor.close()

# Modificar la información de un doctor
def CRUDModificarDoctor(id, nombre=None, telefono=None, direccion=None, especialidad=None):
    cursor = mydb.cursor()

    campos = []
    valores = []
    
    if nombre:
        campos.append("Doctor_Nombre=%s")
        valores.append(nombre)
    if telefono:
        campos.append("Doctor_Telefono=%s")
        valores.append(telefono)
    if direccion:
        campos.append("Doctor_Direccion=%s")
        valores.append(direccion)
    if especialidad:
        campos.append("Doctor_Especialidad=%s")
        valores.append(especialidad)

    valores.append(id)
    sql = f"UPDATE Doctores SET {', '.join(campos)} WHERE Doctor_ID=%s"
    cursor.execute(sql, valores)
    mydb.commit()
    print("Doctor modificado")
    cursor.close()

# Listar Doctores por especialidad
def CRUDListarDoctoresPorEspecialidad(especialidad):
    cursor = mydb.cursor()
    sql = "SELECT * FROM Doctores WHERE Doctor_Especialidad = %s"
    cursor.execute(sql, (especialidad,))
    resultados = cursor.fetchall()
    Doctores = []
    for item in resultados:
        Doctores.append(item)
    cursor.close()
    return Doctores

# Listar Doctores por nombre
def CRUDListarDoctoresPorNombre(nombre):
    cursor = mydb.cursor()
    sql = "SELECT * FROM Doctores WHERE Doctor_Nombre LIKE %s"
    cursor.execute(sql, (f'%{nombre}%',))
    resultados = cursor.fetchall()
    Doctores = []
    for item in resultados:
        Doctores.append(item)
    cursor.close()
    return Doctores

# Listar doctor por ID (uno solo)
def CRUDSeleccionarUnDoctor(id):
    cursor = mydb.cursor()
    sql = f'SELECT * FROM Doctores WHERE Doctor_ID = {id}'
    cursor.execute(sql)
    resultado = cursor.fetchone()
    cursor.close()
    return resultado

#Listar los 3 doctores con mas turnos
def CRUDDoctoresConMasTurnos():
    cursor = mydb.cursor()
    sql = "SELECT doc.Doctor_ID, doc.Doctor_Nombre, doc.Doctor_Especialidad, COUNT(*) AS Turnos FROM Doctores doc JOIN Turnos_Pacientes tur ON doc.Doctor_ID = tur.Turno_Doctor_ID GROUP BY doc.Doctor_ID ORDER BY Turnos DESC LIMIT 3"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    doctores = []
    for doctor in resultados:
        doctores.append(doctor)
    cursor.close()
    return doctores

