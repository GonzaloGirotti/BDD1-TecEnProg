# JUSTIFICACIONES:

## Tabla ***Pacientes*** :

* **COMPOSICIÓN DE LA TABLA:** Pacientes (Paciente_ID, Paciente_Nombre, Paciente_FechaNacimiento, Paciente_Telefono, Paciente_Direccion).

* **Atributos:** 
    * ***Paciente_ID:*** Es un número entero que se asigna automáticamente a cada paciente que ingresa al sistema. Es la clave primaria de la tabla.
    * ***Paciente_Nombre:*** Es el nombre del paciente. Es un string.
    * ***Paciente_FechaNacimiento:*** Es la fecha de nacimiento del paciente. Es un tipo de dato DATE.
    * ***Paciente_Telefono:*** Es el número de teléfono del paciente. Es un bigint
    * ***Paciente_Direccion:*** Es la dirección del paciente. Es un string.
 
* **DEPENDENCIA/S FUNCIONALES:** No existen dependencias funcionales en la tabla ***Pacientes***.

* **Entidades Fuertes/Debil:** La tabla ***Pacientes*** es una **entidad fuerte** ya que no depende de ninguna otra tabla para existir. Es decir, no necesita de otra tabla para tener sentido en la base de datos.

* **Clave candidata:** La columna elegida como **clave candidata** es la columna ***Paciente_ID***. Esto ya que hace que cada *paciente* tenga un registro único en la tabla y, además, es la clave que va a ser usada como referencia en otras tablas para hacer alusion a pacientes especificos (ejemplo: la tabla Turnos_Pacientes hará referencia a esta tabla para anotar a los pacientes en sus respectivos turnos medicos).

* **Relaciones y cardinalidades:** La tabla ***Pacientes*** tiene una relación de **1 a muchos** con la tabla ***Turnos_Pacientes***. Esto ya que un paciente puede tener muchos turnos médicos, pero un turno médico solo puede tener un paciente.


  
## Tabla ***Doctores*** :

* **COMPOSICIÓN DE LA TABLA:**  (Doctor_ID, Doctor_Nombre, Doctor_Telefono, Doctor_Direccion, Doctor_Especialidad):

* **Atributos:** 
    * ***Doctor_ID:*** Es un número entero que se asigna automáticamente a cada doctor que ingresa al sistema. Es la clave primaria de la tabla.
    * ***Doctor_Nombre:*** Es el nombre del doctor. Es un string.
    * ***Doctor_Telefono:*** Es el número de teléfono del doctor. Es un bigint
    * ***Doctor_Direccion:*** Es la dirección del doctor. Es un string.
    * ***Doctor_Especialidad:*** Es la especialidad del doctor. Es un string.

* **DEPENDENCIA/S FUNCIONALES:** No existen dependencias funcionales en la tabla ***Doctores***.

* **Entidad Fuerte/Debil:** La tabla ***Doctores*** es una **entidad fuerte** ya que no depende de ninguna otra tabla para existir. Es decir, no necesita de otra tabla para tener sentido en la base de datos.

* **Clave candidata:** La columna elegida como **clave candidata** es la columna ***Doctor_ID***. Esto ya que hace que cada *doctor* tenga un registro único en la tabla y, además, es la clave que va a ser usada como referencia en otras tablas para hacer alusion a doctores especificos (ejemplo: la tabla Turnos_Pacientes hará referencia a esta tabla para anotar a los doctores en sus respectivos turnos medicos).

* **Relaciones y cardinalidades:** La tabla ***Doctores*** tiene una relación de **1 a muchos** con la tabla ***Turnos_Pacientes***. Esto ya que un doctor puede tener muchos turnos médicos, pero un turno médico solo puede tener un doctor.

## Tabla ***Turnos_Fechas*** :

* **COMPOSICIÓN DE LA TABLA:**  (Turno_ID, Turno_Fecha, Turno_Hora):

* **Atributos:** 
    * ***Turno_ID:*** Es un número entero que se asigna automáticamente a cada turno que se registra en el sistema. Es la clave primaria de la tabla.
    * ***Turno_Fecha:*** Es la fecha del turno. Es un tipo de dato DATE.
    * ***Turno_Hora:*** Es la hora del turno. Es un tipo de dato TIME.
  
* **DEPENDENCIA/S FUNCIONALES:** No existen dependencias funcionales en la tabla ***Turnos_Fechas***.

* **Entidad Fuerte/Debil:** La tabla ***Turnos_Fechas*** es una **entidad fuerte** ya que no depende de ninguna otra tabla para existir. Es decir, no necesita de otra tabla para tener sentido en la base de datos.

* **Clave candidata:** La columna elegida como **clave candidata** es la columna ***Turno_ID***. Esto ya que hace que cada *turno* tenga un registro único en la tabla y, además, es la clave que va a ser usada como referencia en otras tablas para hacer alusion a turnos especificos (ejemplo: la tabla Turnos_Pacientes hará referencia a esta tabla para anotar fecha y hora de los turnos en los que se atenderán a los pacientes).

* **Relaciones y cardinalidades:** La tabla ***Turnos_Fechas*** tiene una relación de **1 a uno** con la tabla ***Turnos_Pacientes***. Esto ya que un turno solo puede tener una fecha y hora, y una fecha y hora solo puede ser asignada a un turno.

## Tabla ***Turnos_Pacientes*** :

* **COMPOSICIÓN DE LA TABLA:**  (ID_Turno_Asignado, Turno_ID, Paciente_ID, Doctor_ID).
  
* **Atributos:** 
    * ***ID_Turno_Asignado:*** Es un número entero que se asigna automáticamente a cada turno asignado a un paciente. Es la clave primaria de la tabla.
    * ***Turno_ID:*** Es un número entero que hace referencia a la tabla ***Turnos_Fechas***. Es una clave foránea de la tabla. Corrobora que la fecha y hora del turno asignado exista en la tabla ***Turnos_Fechas***.
    * ***Paciente_ID:*** Es un número entero que hace referencia a la tabla ***Pacientes***. Es una clave foránea de la tabla. Corrobora que el paciente asignado exista en la tabla ***Pacientes***.
    * ***Doctor_ID:*** Es un número entero que hace referencia a la tabla ***Doctores***. Es una clave foránea de la tabla. Corrobora que el doctor asignado exista en la tabla ***Doctores***.
  
* **DEPENDENCIA/S FUNCIONALES:** La tabla ***Turnos_Pacientes*** tiene dependencia funcional con las tablas ***Pacientes***, ***Doctores*** y ***Turnos_Fechas***. Esto ya que los atributos ***Paciente_ID***, ***Doctor_ID*** y ***Turno_ID*** son claves foráneas que hacen referencia a las tablas mencionadas.

* **Entidad Fuerte/Debil:** La tabla ***Turnos_Pacientes*** es una **entidad debil**. Esta debido a que combina datos de las tablas ***Turnos_Fechas***, ***Pacientes***, y ***Doctores***. No puede existir sin estas tres entidades, ya que:
    Turno_ID (referencia a Turnos_Fechas).
    Turno_Paciente_ID (referencia a Pacientes).
    Turno_Doctor_ID (referencia a Doctores).

* **Clave candidata:** La columna elegida como **clave candidata** es la columna ***ID_Turno_Asignado***. Esto ya que hace que cada *turno asignado* tenga un registro único en la tabla y, además, es la clave que va a ser usada como referencia en otras tablas para hacer alusion a turnos asignados especificos.

* **Relaciones y cardinalidades:** La tabla ***Turnos_Pacientes*** tiene una relación de **1 a uno** con la tabla ***Turnos_Fechas***. Esto ya que un turno asignado solo puede tener una fecha y hora, y una fecha y hora solo puede ser asignada a un turno. Además, la tabla ***Turnos_Pacientes*** tiene una relación con la tabla ***Pacientes*** y ***Doctores*** de **1 a muchos**. Esto ya que un paciente puede tener muchos turnos asignados, y un doctor puede tener muchos turnos asignados. Pero, un turno asignado solo puede tener un paciente y un doctor.


### RESTRICCIONES ADICIONALES:

* **TABLA Pacientes:** La columna ***Paciente_Telefono*** tiene restricción *UNIQUE* ya que de no ser así, se podrían repetir números de teléfono en la tabla, lo cual no es posible en la realidad.

* **TABLA Doctores:** 
- La columna ***Doctor_Telefono*** tiene restricción *UNIQUE* ya que de no ser así, se podrían repetir números de teléfono en la tabla, lo cual no es posible en la realidad.
- Se estableció como regla que no pueda haber 2 doctores de igual nombre con igual especialidad, por lo que las columnas ***Doctor_Nombre*** y ***Doctor_Especialidad*** tienen restricción *UNIQUE* ya que de no ser así, se podrían repetir nombres y especialidades de doctores en la tabla.

* **TABLA Turnos_Fechas:** Las columnas ***Turno_Fecha*** y ***Turno_Hora*** tienen restricción *UNIQUE* ya que de no ser así, se podrían repetir fechas y horas en la tabla, lo cual no es posible en la realidad (esto ya que en esta tabla solo se guardan las fechas y horas, no las asignaciones a pacientes).

* **TABLA Turnos_Pacientes:** 
- La columna ***Turno_ID*** tiene las opciones *ON DELETE CASCADE* y *ON DELETE UPDATE* ya que si se elimina o modifica un turno de la tabla ***Turnos_Fechas***, se debe eliminar el turno asignado en esta tabla. La columna ***Paciente_ID*** tiene la opcion *ON DELETE CASCADE* ya que si se elimina un paciente de la tabla ***Pacientes*** se deben eliminar los turnos asignados a el en esta tabla.
- Las columnas *Turno_ID* y *Turno_Paciente_ID* tienen restricción *UNIQUE* ya que de no ser así, se podrían repetir turnos asignados a un paciente en la tabla, lo cual no es posible en la realidad. Lo mismo con la columna *Turno_ID* y *Turno_Doctor_ID*.








