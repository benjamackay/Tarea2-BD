import { Elysia } from "elysia";
import { PrismaClient } from "@prisma/client";

const app = new Elysia()
const prisma = new PrismaClient();

/*Comandos para Prisma*/
async function crearUsuario(nombre:string, direccion_correo:string, pass:string) {
  try {
    const nuevoUsuario = await prisma.usuarios.create({
      data: {
        nombre: nombre,
        direccion_correo: direccion_correo,
        contrase_a: pass,
      },
    });
    console.log('Usuario creado:', nuevoUsuario);
    return nuevoUsuario;
  } catch (error) {
    console.error('Error al crear usuario:', error);
    throw error;
  }
}

crearUsuario('Benjamin', 'Benjamin@example.com', 'password123')
  .then((usuario) => {
    console.log('Usuario creado exitosamente:', usuario);
  })
  .catch((error) => {
    console.error('Error al crear usuario:', error);
  });

crearUsuario('Magdiel', 'Magdiel@example.com', 'password123')
  .then((usuario) => {
    console.log('Usuario creado exitosamente:', usuario);
  })
  .catch((error) => {
    console.error('Error al crear usuario:', error);
  });

  crearUsuario('Patricio', 'Patricio@example.com', 'password123')
  .then((usuario) => {
    console.log('Usuario creado exitosamente:', usuario);
  })
  .catch((error) => {
    console.error('Error al crear usuario:', error);
  });
