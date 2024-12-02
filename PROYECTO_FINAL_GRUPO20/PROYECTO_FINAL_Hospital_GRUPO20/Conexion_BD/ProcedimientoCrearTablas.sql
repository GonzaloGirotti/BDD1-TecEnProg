CREATE PROCEDURE CrearTablas() BEGIN CREATE TABLE IF NOT EXISTS Pacientes (
    Paciente_ID int not null primary key auto_increment,
    Paciente_Nombre varchar(40) not null,
    Paciente_FechaNacimiento date not null,
    Paciente_Telefono bigint(11) not null,
    Paciente_Direccion varchar(40) not null,
    UNIQUE(Paciente_Telefono)
);
CREATE TABLE IF NOT EXISTS Doctores (
    Doctor_ID int not null primary key auto_increment,
    Doctor_Nombre varchar(40) not null,
    Doctor_Telefono bigint(11) not null,
    Doctor_Direccion varchar(40) not null,
    Doctor_Especialidad varchar(40) not null,
    UNIQUE(Doctor_Nombre, Doctor_Especialidad),
    UNIQUE(Doctor_Telefono)
);
CREATE TABLE IF NOT EXISTS Turnos_Fechas(
    Turno_ID int not null primary key auto_increment,
    Turno_Fecha date not null,
    Turno_Hora time not null,
    UNIQUE (Turno_Fecha, Turno_Hora)
);
CREATE TABLE IF NOT EXISTS Turnos_Pacientes(
    ID_Turno_Asignado int not null primary key auto_increment,
    Turno_ID int not null,
    Turno_Paciente_ID int not null,
    Turno_Doctor_ID int not null,
    FOREIGN KEY (Turno_ID) REFERENCES Turnos_Fechas(Turno_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Turno_Paciente_ID) REFERENCES Pacientes(Paciente_ID) ON DELETE CASCADE,
    FOREIGN KEY (Turno_Doctor_ID) REFERENCES Doctores(Doctor_ID),
    UNIQUE (Turno_ID, Turno_Paciente_ID),
    UNIQUE (Turno_ID, Turno_Doctor_ID)
);
END