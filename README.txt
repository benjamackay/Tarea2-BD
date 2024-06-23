Pasos para el correcto funcionamiento de nuestra tarea. Primero aclarar que nuestra tarea está completamente levantada en wsl, por lo que se tendrá que tener todo lo que necesitamos en wsl. Postgre en wsl, Python en wsl y Prisma+Elysia en wsl.

1-.Crear la base de datos con el archivo TablasBD.py, modificando el conn(), para establecer una correcta conexión entre el corrector y la       base de datos
2-.Luego de usar los comandos escritos en el "requierements.txt" se tendrán que modificar los siguientes archivos.
  1-. .env con las direcciones especificasDATABASE_URL="postgresql://<usuario>:<contraseña>@localhost:<port>/<nombre_db>"
  2-. Modificar el archivo creado por el script "bun create elysia". Especificamente el src/index.ts con el archivo que se encuentra en la          carpeta "Api"
3-.Luego que las conexiones fueron establecidas, correr el archivo "script.ts" el cual poblará con usuarios la bd, para testeo.
4-.Asegurarse de usar "bun run src/index.ts" para luego consumir la API desde Python.
5-.Desde la terminal usar "python3 Cliente.py" para correr el programa principal.
