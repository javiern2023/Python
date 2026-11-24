'''
Característica	        MySQL	    PostgreSQL
Facilidad inicial	   Muy buena	 Buena
Rendimiento	           Muy bueno	Muy bueno
Consultas complejas    Muy bueno	Excelente
Integridad de datos	   Muy buena	Excelente
Python	                  Sí	       Sí
Uso profesional	          Sí	       Sí


MySQL	      mysql-connector-python	pip install mysql-connector-python
PostgreSQL	  psycopg	                pip install "psycopg[binary]"
Añadir dependencias

Conexión	Comunicación entre Python y MySQL
Cursor	    Objeto que permite ejecutar instrucciones SQL
Execute	    Ejecuta una consulta
Commit	    Confirma los cambios realizados
Fetch	    Recupera los resultados de una consulta
Close	    Cierra una conexión o cursor

Conexión: Es el establecimiento de comunicación con la base de datos.

Necesitamos conocer:
- Servidor.
- Puerto.
- Usuario.
- Contraseña.
- Nombre de la base de datos.

Cursor: Es el intermediario que permite enviar instrucciones SQL a MySQL.
Una conexión puede tener diferentes cursores.

Execute: Permite ejecutar una instrucción SQL.

Commit: Confirma definitivamente los cambios de una transacción.
Se utiliza principalmente después de insertar, modificar o eliminar registros.

Fetch: Permite recuperar los resultados de una consulta SELECT.
Tenemos dos operaciones fundamentales:
- fetchone(): recupera un registro.
- fetchall(): recupera todos los registros.

Close: Cierra el cursor o la conexión para liberar recursos.
'''