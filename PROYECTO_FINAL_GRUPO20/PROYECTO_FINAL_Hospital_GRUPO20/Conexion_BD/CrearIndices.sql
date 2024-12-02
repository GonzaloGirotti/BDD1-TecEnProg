CREATE INDEX ind_pacienteID ON Pacientes(Paciente_ID);
CREATE INDEX ind_pacienteNombre ON Pacientes(Paciente_Nombre);
CREATE INDEX ind_doctorID ON Doctores(Doctor_ID);
CREATE INDEX ind_doctorNombre ON Doctores(Doctor_Nombre);
CREATE INDEX ind_doctorEspecialidad ON Doctores(Doctor_Especialidad);
CREATE INDEX ind_doctorCompleto ON Doctores(Doctor_ID, Doctor_Nombre, Doctor_Especialidad);
CREATE INDEX ind_turnoID ON Turnos_Fechas(Turno_ID);
CREATE INDEX ind_turnoFecha ON Turnos_Fechas(Turno_Fecha);
CREATE INDEX ind_turnoHora ON Turnos_Fechas(Turno_Hora);
CREATE INDEX ind_turnoPacienteID ON Turnos_Pacientes(ID_Turno_Asignado);
CREATE INDEX ind_turnoDoctorID ON Turnos_Pacientes(Turno_Doctor_ID);