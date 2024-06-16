import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host = 'localhost',
    user= 'postgres',
    dbname = 'tarea2',
    password = '', #contraseña
    port = '5432'
)
print("Conexion Exitosa")
cursor = conn.cursor()

create_tables_queries = [
    """
    CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario SERIAL PRIMARY KEY NOT NULL,
    descripcion VARCHAR(255),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    nombre VARCHAR(35) NOT NULL,
    direccion_correo VARCHAR(255) UNIQUE NOT NULL,
    contraseña TEXT NOT NULL,
    es_admin BOOLEAN NOT NULL DEFAULT FALSE 
);

CREATE TABLE IF NOT EXISTS correos (
    id_correo SERIAL PRIMARY KEY,
    remitente INT NOT NULL,
    destinatario INT NOT NULL,
    asunto VARCHAR(255),
    cuerpo TEXT NOT NULL,
    fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    leido BOOLEAN DEFAULT FALSE,
    es_favorito BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (remitente) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (destinatario) REFERENCES usuarios(id_usuario)
);

CREATE TABLE IF NOT EXISTS correos_favoritos (
    id_correo_favorito SERIAL PRIMARY KEY,
    usuario_id INT NOT NULL,
    correo_id INT NOT NULL,
    fecha_anadido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (correo_id) REFERENCES correos(id_correo)
);

CREATE TABLE IF NOT EXISTS usuarios_bloqueados (
    id_bloqueado SERIAL PRIMARY KEY,
    usuario_bloqueado INT NOT NULL,
    usuario_id INT NOT NULL,
    fecha_bloqueo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_bloqueado) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id_usuario)
);
    """
]

cursor.execute(create_tables_queries)
conn.commit()

cursor.close()
conn.close()

