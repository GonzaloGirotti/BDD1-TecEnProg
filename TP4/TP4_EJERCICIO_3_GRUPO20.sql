drop table if exists usuarios;

CREATE TABLE Usuarios (
    Id INTEGER AUTO_INCREMENT PRIMARY KEY,
    NombreUsuario VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    FechaRegistro DATE NOT NULL,
    Estado VARCHAR(20) NOT NULL -- Ejemplos: 'Activo', 'Inactivo', 'Pendiente'
);

INSERT INTO Usuarios (NombreUsuario, Email, FechaRegistro, Estado) VALUES
('nmartinez', 'nmartinez@gmail.com', '2023-10-01', 'Activo'),
('osanchez', 'osanchez@outlook.com', '2023-09-15', 'Pendiente'),
('pfernandez', 'pfernandez@hotmail.com', '2023-08-20', 'Activo'),
('qlopez', 'qlopez@gmail.com', '2023-06-10', 'Pendiente'),
('rgarcia', 'rgarcia@outlook.com', '2023-05-05', 'Inactivo'),
('sherrera', 'sherrera@hotmail.com', '2022-04-25', 'Activo'),
('tbenitez', 'tbenitez@gmail.com', '2024-10-31', 'Pendiente'),
('umarquez', 'umarquez@outlook.com', '2021-12-15', 'Activo'),
('vchavez', 'vchavez@hotmail.com', '2021-11-10', 'Activo'),
('wtorres', 'wtorres@gmail.com', '2021-09-20', 'Inactivo'),
('xrodriguez', 'xrodriguez@outlook.com', '2024-10-30', 'Pendiente'),
('yhernandez', 'yhernandez@hotmail.com', '2022-02-14', 'Activo'),
('zlopez', 'zlopez@gmail.com', '2023-07-21', 'Activo'),
('abrown', 'abrown@outlook.com', '2021-12-31', 'Inactivo'),
('cbrown', 'cbrown@hotmail.com', '2020-11-05', 'Pendiente');

DROP PROCEDURE IF EXISTS ValidarUsuarios;

DELIMITER $$

CREATE PROCEDURE ValidarUsuarios()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_Id INT;
    DECLARE v_FechaRegistro DATE;
    DECLARE v_Estado VARCHAR(20);

    -- Declaro un cursor para seleccionar Id, FechaRegistro y Estado de la tabla Usuarios
    DECLARE usuario_cursor CURSOR FOR
    SELECT Id, FechaRegistro, Estado FROM Usuarios;

    -- Declaro una condición de salida para el cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Abro el cursor
    OPEN usuario_cursor;

    -- Bucle para iterar sobre cada fila
    read_loop: LOOP
        FETCH usuario_cursor INTO v_Id, v_FechaRegistro, v_Estado;

        -- Verificar si ya no hay más filas
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Regla 1: Si el usuario ha estado en estado 'Pendiente' por más de 7 días, actualizar a 'Inactivo'
        IF v_Estado = 'Pendiente' AND DATEDIFF(CURDATE(), v_FechaRegistro) > 7 THEN
            UPDATE Usuarios SET Estado = 'Inactivo' WHERE Id = v_Id;
            SELECT CONCAT('Usuario con Id ', v_Id, ' actualizado a Inactivo') AS Actualizacion;
        END IF;

        -- Regla 2: Si el usuario está en estado 'Activo' y su fecha de registro fue hace más de un año
        IF v_Estado = 'Activo' AND DATEDIFF(CURDATE(), v_FechaRegistro) > 365 THEN
            SELECT CONCAT('Notificación: El usuario con Id ', v_Id, ' ha estado activo por más de un año.') AS Notificacion;
        END IF;
    END LOOP;

    -- Cerrar el cursor
    CLOSE usuario_cursor;
END $$

DELIMITER ;

CALL ValidarUsuarios();

SELECT * FROM Usuarios;