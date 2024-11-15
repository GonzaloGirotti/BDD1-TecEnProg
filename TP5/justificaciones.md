# JUSTIFICACIONES:

## Tabla ***Deportista*** :

* **COMPOSICIÓN DE LA TABLA:** Deportista (id_deportista, nombre_deportista, id_pais):

* **DEPENDENCIA/S FUNCIONALES:** Las columnas ***nombre_deportista*** e ***id_pais*** dependen de la columna ***deportista_id***, ya que esta última es la **Primary Key** de la tabla, lo cual hace que:
    * Cada combinación ***nombre del deportista - pais del deportista*** tenga un ID único en cada registro de esta tabla, garantizando la unicidad. 
    * Al elegir uno u otro ID, la combinación ***nombre del deportista - pais del deportista*** referenciada cambie. (por mas que haya dos deportistas de igual nombre e igual país, el id asignado hace que se haga referencia a otra persona).

* **Clave candidata:** La columna elegida como **clave candidata** es la columna ***deportista_id***. Esto ya que hace que cada combinación ***nombre del deportista - pais del deportista*** tenga un registro único en la tabla y, además, es la clave que va a ser usada como referencia en otras tablas para hacer alusion a deportistas especificos (ejemplo: la tabla participaciones hará referencia a esta tabla para anotar las participaciones de los deportistas en los JJOO).
  
## Tabla ***Pais*** :

* **COMPOSICIÓN DE LA TABLA:** Pais (id_pais, nombre_pais)

* **DEPENDENCIA/S FUNCIONALES:** La columna ***nombre_pais*** depende de la columna ***id_pais***, ya que esta última es la **Primary Key** de la tabla, lo cual hace que solo haya un nombre de país para cada registro de esta tabla. También hace que al elegir uno u otro ID, el país referenciado cambie.

* **Clave candidata:** La columna elegida como **clave candidata** es la columna ***id_pais***. Esto ya que hace que cada nombre de pais tenga un registro único en la tabla y, además, es la clave que va a ser usada como referencia en otras tablas para hacer alusion a paises específicos (ejemplo: las tablas ***Deportista*** y ***Olimpiadas*** hacen referencia a los *id* de los paises para registrar el pais del deportista o el pais de cada olimpiada respectivamente).

## Tabla ***Disciplina*** :

* **COMPOSICIÓN DE LA TABLA:** Disciplina (id_disciplina, nombre_disciplina)

* **DEPENDENCIA/S FUNCIONALES:** La columna ***nombre_disciplina*** depende de la columna ***id_disciplina***, ya que esta última es la **Primary Key** de la tabla, lo cual hace que solo haya un nombre de disciplina para cada registro de esta tabla. También hace que al elegir uno u otro ID, la disciplina referenciada cambie.

* **Clave candidata:** La columna elegida como **clave candidata** es la columna ***id_disciplina***. Esto ya que hace que cada nombre de disciplina tenga un registro único en la tabla y, además, es la clave que va a ser usada como referencia en otras tablas para hacer alusion a disciplinas específicas (ejemplo: la tabla ***Participaciones*** hace referencia a los ID de las disciplinas para registrar en que disciplina participó cada deportista en cada olimpiada).

## Tabla ***Asistente*** :

* **COMPOSICIÓN DE LA TABLA:** Asistente (id_asistente, nombre_asistente)

* **DEPENDENCIA/S FUNCIONALES:** La columna ***nombre_asistente*** depende de la columna ***id_asistente***, ya que esta última es la **Primary Key** de la tabla, lo cual hace que solo haya un nombre de asistente para cada registro de esta tabla. También hace que al elegir uno u otro ID, el asistente referenciado cambie.

* **Clave candidata:** La columna elegida como **clave candidata** es la columna ***id_asistente***. Esto ya que hace que cada nombre de asistente tenga un registro único en la tabla y, además, es la clave que va a ser usada como referencia en otras tablas para hacer alusion a asistentes específicos (ejemplo: la tabla ***Participaciones*** hace referencia a los ID de los asistentes para registrar que asistente ayudó a cada deportista en cada olimpiada).

## Tabla ***Olimpiadas*** :

* **COMPOSICIÓN DE LA TABLA:** Olimpiadas (id_olimpiada, anio_olimpiada, id_pais)

* **DEPENDENCIA/S FUNCIONALES:** Las columnas ***anio_olimpiada*** e ***id_pais*** dependen de la columna ***id_olimpiada***, ya que esta última es la **Primary Key** de la tabla, lo cual hace que:
    * Cada combinación ***año de las olimpiadas - pais donde se jugaron las olimpiadas*** tenga un ID único en cada registro de esta tabla, garantizando la unicidad. 
    * Al elegir uno u otro ID, la combinación ***año de las olimpiadas - pais donde se jugaron las olimpiadas*** referenciada cambie. Aquí, cada registro SIEMPRE será diferente en su año, ya que no se puede dar que se jueguen dos veces o mas las olimpiadas en un mismo año. Lo que podria repetirse de un año a otro es el pais donde se jugaron.

* **Clave candidata:** La columna elegida como **clave candidata** es la columna ***id_olimpiada***. Esto ya que hace que cada combinación ***año de las olimpiadas - pais donde se jugaron las olimpiadas*** tenga un registro único en la tabla y, además, es la clave que va a ser ser usada como referencia en otras tablas para hacer alusion a ***olimpiadas*** específicas (ejemplo: la tabla ***Participaciones*** hace referencia a los ID de las Olimpiadas de los distintos años para registrar las participaciones de los deportistas en cada Olimpiada).

## Tabla ***Participaciones*** :

* **COMPOSICIÓN DE LA TABLA:** Participaciones (participacion_id, olimpiada_code, deportista_code, asistente_code, disciplina_code)

* **DEPENDENCIA/S FUNCIONALES:** Las columnas ***olimpiada_code***, ***deportista_code***, ***asistente_code***, ***disciplina_code*** dependen de la columna ***participacion_id***, ya que esta última es la **Primary Key** de la tabla, lo cual hace que:
    * Cada combinación ***olimipiadas donde participó el deportista - deportista participante - asistente del deportista - disciplina que desarrolló el deportista*** tenga un ID único en cada registro de esta tabla, garantizando la unicidad. 
    * Al elegir uno u otro ID, la combinación ***olimipiadas donde participó el deportista - deportista participante - asistente del deportista - disciplina que desarrolló el deportista*** referenciada cambie.
* **Clave candidata:** La columna elegida como **clave candidata** es la columna ***participacion_id***. Esto ya que hace que cada combinación ***olimipiadas donde participó el deportista - deportista participante - asistente del deportista - disciplina que desarrolló el deportista*** tenga un registro único en la tabla y, además, es la clave que podría ser usada como referencia en otras tablas para hacer alusion a ***Participaciones*** específicas.


### RESTRICCIONES ADICIONALES:

* **TABLA Pais:** La columna ***id_pais*** tiene restricción *UNIQUE* ya que de no ser así, podría haber dos registros de país de igual nombre (ejemplo: podría haber registro con ID 1 - nombre Argentina, y otro con ID 12 - nombre Argentina).

* **TABLA Olimpiadas:** La columna ***anio_olimpiada*** tiene restricción *UNIQUE* ya que de no ser así, se podría dar que se registren dos juegos olimpicos distintos jugados en el mismo año.

* **TABLA Participaciones:** Se crearon dos restricciones de tipo *UNIQUE*:
  * ***(olimpiada_code, deportista_code) [unique] :*** Se creó haciendo que cada combinación de deportista jugando en una olimpiada específica sea única, logrando que no se registre al mismo deportista dos veces en el mismo año de olimpiadas.
  * ***(olimpiada_code, asistente_code) [unique] :*** Se creó haciendo que cada combinación de asistente participando en una olimpiada específica sea única, logrando que no se registre al mismo asistente dos veces en el mismo año de olimpiadas. Esto, ya que un asistente (por lógica) debería ayudar solo a un deportista durante unas olimpiadas.





