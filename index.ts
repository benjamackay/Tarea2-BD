import { Elysia } from "elysia";
import { PrismaClient } from "@prisma/client";


const prisma = new PrismaClient();
const app = new Elysia();


interface UserBody {
  name: string;
  address: string;
  pass: string;
  description?: string;
}

app.get('/', ()=>'Hello Elysia');

/*POST para registrar usuarios*/
app.post('/api/registrar', async ({ body }: { body: UserBody }) => {
  const { name, address, pass, description } = body;
  try {
    const usuario = await prisma.usuarios.create({
      data: {
        nombre: name,
        direccion_correo: address,
        contrase_a: pass,
        descripcion: description,
      },
    });
    return { status: 201, body: usuario };
  } catch (error: any) {
    return { status: 400, body: { error: error.message || 'Error desconocido' } };
  }
});

interface BloqUser {
  correo: string,
  clave: string,
  correo_bloquear: string,
}


/*POST para bloquear el correo de otros usuarios*/
app.post('/api/bloquear', async ({ body }: { body: BloqUser }) => {
  const { correo, clave, correo_bloquear } = body;
  try {
    const usuariobloqueado = await prisma.usuarios_bloqueados.create({
      data: {
        correo: correo,
        clave : clave,
        correo_bloqueado: correo_bloquear,
      },
    });
    return { status: 201, body: usuariobloqueado };
  } catch (error: any) {
    return { status: 400, body: { error: error.message || 'Error desconocido' } };
  }
});

/*GET para obtener la información de correo*/
app.get('/api/informacion/:correo', async ({ params }: { params: { correo: string } }) => {
  const { correo } = params;
  try {
    const informacion = await prisma.usuarios.findUnique({
      where: {
        direccion_correo: correo,
      },
    });

    if (!informacion) {
      return { status: 404, body: { error: 'No se encontró la información del usuario' } };
    }

    const { nombre, direccion_correo, descripcion } = informacion;

    return { status: 200, body: { nombre, direccion_correo, descripcion } };
  } catch (error: any) {
    return { status: 500, body: { error: error.message || 'Error al buscar la información del usuario' } };
  }
});

interface MarcarCorreo {
  correo: string,
  clave: string,
  id_correo: number,
  id_correo_favorito: number,
}

/*POST para marcar correo favorito*/
app.post('/api/marcarcorreo', async ({ body }: { body: MarcarCorreo }) => {
  const { correo, clave, id_correo} = body;
  try {
    const correo_favorito = await prisma.correos_favoritos.create({
      data: {
        direccion_correo: correo,
        clave: clave,
        id_correo: id_correo,
      },
    });
    return { status: 201, body: correo_favorito };
  } catch (error: any) {
    return { status: 400, body: { error: error.message || 'Error desconocido' } };
  }
});

/*DELETE para desmarcar correo*/
app.delete('/api/desmarcarcorreo', async ({ body }: { body: MarcarCorreo }) => {
  const { correo, clave, id_correo, id_correo_favorito} = body;
  try {
    const correo_favorito = await prisma.correos_favoritos.findUnique({
      where: {
        direccion_correo: correo,
        id_correo: id_correo,
        clave: clave,
        id_correo_favorito: id_correo_favorito,
      },
    });

    if (!correo_favorito) {
      return { status: 404, body: { error: "Correo no encontrado" } };
    }

    await prisma.correos_favoritos.delete({
      where: {
        direccion_correo: correo,
        id_correo: id_correo,
        clave: clave,
        id_correo_favorito: id_correo_favorito,
      },
    });

    return { status: 200, body: { message: 'Correo Desmarcado' } };
  } catch (error: any) {
    return { status: 500, body: { error: error.message } };
  }
});

app.listen(3000);
console.log("SERVIDOR ACTIVO EN PORT: 3000")

