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
    const usuario = await prisma.usuario.create({
      data: {
        nombre: name,
        direccion_correo: address,
        pass: pass,
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
  pass: string,
  correo_bloquear: string,
}


/*POST para bloquear el correo de otros usuarios*/
app.post('api/bloquear', async({body}:{body: BloqUser})=>{
  const {correo, pass, correo_bloquear} = body;
  try {
    const usuariobloqueado = await prisma.usuariobloqueado.create({
      data: {
        correo: correo,
        pass: pass,
        correo_bloquear: correo_bloquear,
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
    const informacion = await prisma.usuario.findUnique({
      where: {
        direccion_correo: correo,
      },
    });

    if (!informacion) {
      return { status: 404, body: { error: 'No se encontró la información del usuario' } };
    }

    const { nombre, descripcion } = informacion;

    return { status: 200, body: { nombre, correo, descripcion } };
  } catch (error: any) {
    return { status: 500, body: { error: error.message || 'Error al buscar la información del usuario' } };
  }
});

interface MarcarCorreo{
  correo: string,
  clave: string,
  id_correo_favorito: Int16Array,
}

/*POST para marcar un correo como favorito*/
app.post('api/marcarcorreo', async({body}:{body:MarcarCorreo})=> {
  const {correo, clave, id_correo_favorito} = body;
  try{
    const correo_favorito = await prisma.correo_favorito.create({
      data: {
        correo: correo,
        pass: clave,
        id_correo_favorito: id_correo_favorito,
      },
    });
    return { status: 201, body: correo_favorito };
  } catch (error: any) {
    return { status: 400, body: { error: error.message || 'Error desconocido' } };
  }
});

/*DELETE para desmarcar un correo de favoritos */
app.delete('api/desmarcarcorreo', async({body}: {body:MarcarCorreo})=>{
  const { correo, clave, id_correo_favorito} = body;
  try{
    const correo_favorito = await prisma.correo_favorito.findUnique({
      where: {
        correo: correo,
        clave: clave,
        id_correo_favorito: id_correo_favorito,
      }

    });
  if(!correo_favorito){
    return {status: 404, body: {error: "Correo no encontrado"}};
  }
  await prisma.correo_favorito.delete({
    where: {
      correo: correo,
      clave: clave,
      id_correo_favorito: id_correo_favorito,
    }
  });
  return {status: 200, body :{message: 'Correo Desmarcado'}};
  }catch(error:any){
    return {status: 500, body: {error: error.message}};
  }
});
