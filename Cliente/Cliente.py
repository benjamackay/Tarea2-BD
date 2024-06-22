import requests
from datetime import datetime

# Obtener la hora y los minutos actuales
ahora = datetime.now()
hora_actual = ahora.strftime("%H:%M")
hora_actual = "["+hora_actual+"]"


#URLs de las endpoints
URLResponse= "http://localhost:3000/" #URL de la raíz del servidor, para verificar la conexión
URLRegistrar = "http://localhost:3000/api/registrar" #URL para registrar un usuario
URLBloquear = "http://localhost:3000/api/bloquear" #URL para bloquear un correo
URLInfoCorreo = "http://localhost:3000/api/informacion/:correo" #URL para obtener información de un correo
URLMarcarCorreo = "http://localhost:3000/api/marcarcorreo" #URL para marcar un correo como favorito
URLDesmarcarCorreo = "http://localhost:3000/api/desmarcarcorreo" #URL para desmarcar un correo como favorito



def Registrar (correo, contrasena,nombre,descripcion): #Función para registrar un usuario
    response = requests.post(URLRegistrar, data = {'correo': correo, 'contrasena': contrasena , 'nombre': nombre, 'descripcion': descripcion}) #Envío los datos del nuevo usuario y espero una respuesta
    if response.status_code == 200: #Si la respuesta fue exitosa, muestro mensaje de éxito
        print(hora_actual,"Usuario registrado con éxito")
    else:
        print(hora_actual,"Error al registrar usuario, detalles: ", response.text)


def iniciarSesion (correo, contrasena): #Función para iniciar sesión
    response = requests.get(URLInfoCorreo, data = {'correo': correo, 'contrasena': contrasena}) #Envío los datos de inicio de sesión y espero una respuesta
    if response.status_code == 200:
        print(hora_actual,"Sesión iniciada con éxito")
        return True #Si la respuesta fue exitosa, retorno True
    else:
        print(hora_actual,"Error al iniciar sesión, detalles: ", response.text)
        return False #Si la respuesta no fue exitosa, retorno False

response = requests.get(URLResponse) #Intento conectarme al servidor

comando = True
print("Bienvenido al sistema CommuniKen")
print("Intentando conexión con el servidor...")

if response.status_code == 200: #checkeo si la conexión fue exitosa
    print("Conexión exitosa")
    print("Se iniciará sesión con un usuario existente...")
    print("Ingrese correo:")
    correo = input()
    print("Ingrese contraseña:")
    contrasena = input()
    comando=iniciarSesion(correo, contrasena) #Intento iniciar sesión con el correo y contraseña ingresados
    while (comando): #Main loop del programa
        print("¿Que desea hacer?")
        print("1. Bloquear un correo")
        print("2. Marcar un correo como favorito")
        print("3. Desmarcar un correo como favorito")
        print("4. Revisar información de un correo")
        print("5. Registrar un usuario nuevo")
        print("6. Salir del sistema")
        opcion = input()
        if opcion == "1":   #Bloquear un correo
            print("Ingrese el correo que desea bloquear:")
            correo_bloquear = input()#Pido el correo a bloquear
            response = requests.post(URLBloquear, data = {'correo': correo, 'pass': contrasena, 'correo_bloquear': correo_bloquear})#Envío el correo a bloquear
            if response.status_code == 200:#Si la respuesta fue exitosa, muestro mensaje de éxito
                print(hora_actual,"Correo bloqueado con éxito")
            else:
                print(hora_actual,"Error al bloquear correo, detalles: ", response.text)
        
        
        
        #Marcar un correo como favorito
        elif opcion == "2":
            print("Ingrese el correo que desea marcar como favorito:") 
            correo_Fav = input()#Pido el correo a marcar
            response = requests.post(URLMarcarCorreo, data = {'correo': correo, 'pass': contrasena, 'id_correo_favorito': correo_Fav}) #Envío el correo a marcar y espero una respuesta
            if response.status_code == 200: #Si la respuesta fue exitosa, muestro mensaje de éxito
                print(hora_actual,"Correo marcado con éxito")
            else:   #Si la respuesta no fue exitosa, muestro el error
                print(hora_actual,"Error al marcar correo, detalles: ", response.text)
        
        
        
        #Desmarcar un correo
        elif opcion == "3":
            print("Ingrese el correo que desea desmarcar:")
            correo_Fav = input() #Pido el correo a desmarcar
            response = requests.post(URLDesmarcarCorreo, data = {'correo': correo , 'pass': contrasena, 'id_correo_favorito': correo_Fav}) #Envío el correo a desmarcar y espero una respuesta
            if response.status_code == 200: #Si la respuesta fue exitosa, muestro mensaje de éxito
                print(hora_actual,"Correo desmarcado con éxito")
            else:#Si la respuesta no fue exitosa, muestro el error
                print(hora_actual,"Error al desmarcar correo, detalles: ", response.text)
        
        
        
        #Revisar información de un correo 
        elif opcion == "4":
            print("Ingrese el correo del que desea obtener información:")
            correo_Buscar = input() #Pido el correo del que quiero obtener información
            response = requests.get(URLInfoCorreo, data = {'correo': correo_Buscar}) #Envío el correo y espero una respuesta
            if response.status_code == 200:#Si la respuesta fue exitosa, muestro la información
                print(hora_actual,"Información obtenida con éxito")
                print(response.text)
            else:#Si la respuesta no fue exitosa, muestro el error
                print(hora_actual,"Error al obtener información, detalles: ", response.text)
        
        
        
        #Registrar un usuario nuevo
        elif opcion == "5": 
            #Se piden los datos del nuevo usuario
            print("Ingrese el correo del nuevo usuario:")
            NuevoCorreo = input()
            print("Ingrese la contraseña del nuevo usuario:")
            NuevaContrasena = input()
            print("Ingrese el nombre del nuevo usuario:")
            nombre = input()
            print("Ingrese una descripción del nuevo usuario:")
            descripcion = input()
            Registrar(NuevoCorreo, NuevaContrasena, nombre, descripcion) #Se envían los datos del nuevo usuario para registrarlo
        else:
            print("Opción inválida, intente de nuevo")
            
else:
    print("Error en la conexión, detalles: ", response.text) #Si la conexión no fue exitosa, muestro el error
