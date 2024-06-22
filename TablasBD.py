import psycopg2


conn = psycopg2.connect(
    host='localhost',
    user='benjajjj',
    dbname='tarea2',
    password='' #contraseña
)
print("Conexion Exitosa")

cursor = conn.cursor()


create_tables_queries = ["""
   CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario SERIAL PRIMARY KEY NOT NULL,
    descripcion VARCHAR(255),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    nombre VARCHAR(35) NOT NULL,
    direccion_correo VARCHAR(255) UNIQUE NOT NULL,
    contraseña TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS correos(
    id_correo SERIAL PRIMARY KEY,
    remitente VARCHAR(255) NOT NULL,
    destinatario VARCHAR(255) NOT NULL,
    asunto VARCHAR(255),
    cuerpo TEXT NOT NULL,
    fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    leido BOOLEAN DEFAULT FALSE,
    es_favorito BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (remitente) REFERENCES usuarios(direccion_correo),
    FOREIGN KEY (destinatario) REFERENCES usuarios(direccion_correo)
);

CREATE TABLE IF NOT EXISTS correos_favoritos (
    id_correo_favorito INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    direccion_correo VARCHAR(255) NOT NULL,
    id_corre  INT NOT NULL,
    clave TEXT NOT NULL,
    fecha_anadido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (correo) REFERENCES usuarios(direccion_correo),
    FOREIGN KEY (id_corre) REFERENCES correos(id_correo)
);

CREATE TABLE IF NOT EXISTS usuarios_bloqueados (
    id_bloqueado SERIAL PRIMARY KEY,
    correo VARCHAR(255) NOT NULL,
    correo_bloqueado VARCHAR(255) NOT NULL,
    fecha_bloqueo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    clave TEXT NOT NULL,
    FOREIGN KEY (correo) REFERENCES usuarios(direccion_correo),
    FOREIGN KEY (correo_bloqueado) REFERENCES usuarios(direccion_correo)
);
"""
]


for query in create_tables_queries:
    cursor.execute(query)


conn.commit()


cursor.close()
conn.close()

print("Tablas creadas exitosamente")

conn.commit()

cursor.close()
conn.close()

