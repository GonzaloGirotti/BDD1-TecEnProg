import mysql.connector
import Conexion_BD.conexion_db as Conexion_BD

# Conexión a la base de datos
mydb = Conexion_BD.DatosDeConexion()

def CRUDBuscarPacienteDelTurno(turno_paciente_id):
    cursor = mydb.cursor()
    cursor.execute("SELECT Paciente_Nombre FROM Pacientes WHERE Paciente_ID = %s", (turno_paciente_id,))
    resultado = cursor.fetchone()
    cursor.close()
    return resultado

def CRUDBuscarDoctorDelTurno(turno_doctor_id):
    cursor = mydb.cursor()
    cursor.execute("SELECT Doctor_Nombre FROM Doctores WHERE Doctor_ID = %s", (turno_doctor_id,))
    resultado = cursor.fetchone()
    cursor.close()
    return resultado

def CRUDSeleccionarTurnoPaciente(turno_id):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Turnos_Pacientes WHERE Turno_ID = %s", (turno_id,))
    resultado = cursor.fetchone()
    cursor.close()
    return resultado

def CRUDSeleccionarTurnoFecha(turno_id):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Turnos_Fechas WHERE Turno_ID = %s", (turno_id,))
    resultado = cursor.fetchone()
    cursor.close()
    return resultado

def CRUDAgregarTurno(turno_fecha, turno_hora):
    cursor = mydb.cursor()
    sql = 'INSERT INTO Turnos_Fechas (Turno_Fecha, Turno_Hora) VALUES (%s, %s)'
    valores = (turno_fecha, turno_hora)
    cursor.execute(sql, valores)
    mydb.commit()
    cursor.close()

def CRUDAsignarTurno(turno_id, paciente_id, doctor_id):
    cursor = mydb.cursor()
    sql = 'INSERT INTO Turnos_Pacientes (Turno_ID, Turno_Paciente_ID, Turno_Doctor_ID) VALUES (%s, %s, %s)'
    valores = (turno_id, paciente_id, doctor_id)
    cursor.execute(sql, valores)
    mydb.commit()
    cursor.close()
    print("Turno asignado correctamente!")

def CRUDListarTurnos():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Turnos_Fechas")
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

def CRUDListarTurnosPacientes():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Turnos_Pacientes")
    resultados = cursor.fetchall()
    turnos = []
    for turno in resultados:
        turnos.append(turno)
    cursor.close()
    return turnos

def CRUDActualizarTurno(turno_id, turno_fecha, turno_hora, turno_doctor_id):
    cursor = mydb.cursor()
    sqlTurnoFecha = 'UPDATE Turnos_Fechas SET Turno_Fecha = %s, Turno_Hora = %s WHERE Turno_ID = %s'
    valoresTurnoFecha = (turno_fecha, turno_hora, turno_id)
    cursor.execute(sqlTurnoFecha, valoresTurnoFecha)
    sqlTurnoDoctor = 'UPDATE Turnos_Pacientes SET Turno_Doctor_ID = %s WHERE Turno_ID = %s'
    valoresTurnoDoctor = (turno_doctor_id, turno_id)
    cursor.execute(sqlTurnoDoctor, valoresTurnoDoctor)
    mydb.commit()
    cursor.close()

def CRUDListarFechasDisponibles():
    cursor = mydb.cursor()
    cursor.execute("SELECT Turno_Fecha FROM Turnos_Fechas")
    resultados = cursor.fetchall()
    for turno in resultados:
        print(turno)
    cursor.close()

def CRUDListarHorasDisponibles():
    cursor = mydb.cursor()
    cursor.execute("SELECT Turno_Hora FROM Turnos_Fechas")
    resultados = cursor.fetchall()
    for turno in resultados:
        print(turno)
    cursor.close()

def CRUDObtenerIDSDeLosDoctores():
    cursor = mydb.cursor()
    cursor.execute("SELECT Doctor_ID FROM Doctores")
    resultados = cursor.fetchall()
    ids = []
    for doctor in resultados:
        ids.append(doctor[0])
    cursor.close()
    return ids

def CRUDObtenerIDSDeLosPacientes():
    cursor = mydb.cursor()
    cursor.execute("SELECT Paciente_ID FROM Pacientes")
    resultados = cursor.fetchall()
    ids = []
    for paciente in resultados:
        ids.append(paciente[0])
    cursor.close()
    return ids

def CRUDEliminarTurnosDeUnDoctor(idDoctor):
    cursor = mydb.cursor()

    sqlDoctor = "SELECT Turno_ID FROM Turnos_Pacientes WHERE Turno_Doctor_ID = %s"
    cursor.execute(sqlDoctor, (idDoctor,))
    resultados = cursor.fetchall()
    idsTurnos = []
    for turno in resultados:
        idsTurnos.append(turno)

    sqlTurnos = "DELETE FROM Turnos_Fechas WHERE Turno_ID = %s"
    for idTurno in idsTurnos:
        cursor.execute(sqlTurnos, idTurno)

    mydb.commit()
    cursor.close()

def CRUDEliminarTurnosDeRangoDeFechas(fechaInicio, fechaFin):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM Turnos_Fechas WHERE Turno_Fecha BETWEEN %s AND %s", (fechaInicio, fechaFin))
    mydb.commit()
    cursor.close()

def CRUDListarTurnosDeUnDoctor(idDoctor):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Turnos_Pacientes WHERE Turno_Doctor_ID = %s", (idDoctor,))
    resultados = cursor.fetchall()
    turnos = []
    for turno in resultados:
        turnos.append(turno)
    cursor.close()
    return turnos

def CRUDListarTurnosPacientesDeUnRangoDeFechas(fechaInicio, fechaFin):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Turnos_Pacientes WHERE Turno_ID IN (SELECT Turno_ID FROM Turnos_Fechas WHERE Turno_Fecha BETWEEN %s AND %s)", (fechaInicio, fechaFin))
    resultados = cursor.fetchall()
    turnos = []
    for turno in resultados:
        turnos.append(turno)
    cursor.close()
    return turnos


