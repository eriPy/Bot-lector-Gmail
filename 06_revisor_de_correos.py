#importamos las librerias a usar
import os
import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv
from plyer import notification
from openpyxl import Workbook#esta libreria es para guardar los correos en excel y llevarlos al dia
from datetime import datetime#para tener el momento en que se leyeron los correos
import time#para el bucle
from pathlib import Path
load_dotenv(Path(__file__).parent / ".env")
print(os.getenv("GMAIL_ESPERADO"))
wb = Workbook()#creamos un libro de excel
hoja = wb.active#creamos una hoja en ese libro
hoja.title = "Correos"#le coloca un titulo a la hoja
correo = os.getenv("GMAIL_USER")#nuestro gmail
contraseña = os.getenv("GMAIL_PASS")#nuestra contraseña
remitente_esperado = os.getenv("GMAIL_ESPERADO")#el correo que esperamos
#creamos una funcion para que evalue un bucle para que mientras estemos corriendo el programa revise los correos constantemente
def lector_de_correos(correo_esperado):
    conexion = imaplib.IMAP4_SSL("imap.gmail.com", 993)#entramos al servidor de gmail
    conexion.login(correo, contraseña)#nos logeamos
    conexion.select("INBOX")#entramos a la bandeja de entrada
    _, mensajes = conexion.search(None, "UNSEEN")#guarda un estado y el mensaje, solo ocuparemos el mensaje
    ids_correos = mensajes[0].split()#guarda todos los ids de los correos que lea
    for id_correo in ids_correos:
        _, datos = conexion.fetch(id_correo, "(RFC822)")#con fetch recibimos el correo completo
        mensaje = email.message_from_bytes(datos[0][1])#esto lo simplifica convirtendolo en objeto para solo buscar lo que queremos
        remitente = mensaje["From"]#metemos en una variable el correo que nos envio mensaje
        if correo_esperado in remitente:#si el remitente que esperamos esta dentro del remitente que encontro, porque a veces no solo dara correos
            asunto_crudo = mensaje["Subject"]#metera los datos del asunto en una variable
            partes = decode_header(asunto_crudo)[0]##luego lo dividira en una lista tipo: ["mensaje", "codigo"]
            asunto, codigo = partes#lo dividimos en contenido y el codigo del mensaje
            if isinstance(asunto, bytes):#evaluara si esta en bytes
                asunto = asunto.decode(codigo or "utf-8")#lo convertira a texto leible
            notification.notify(#para que nos caiga una notificacion mientras el bot este activo y podamos saber cuando nos cae un nuevo correo
                title=f"Nuevo correo de {remitente}",#vemos el remitente
                message=asunto,#el asunto del mensaje
                app_name="Bot",
                timeout=10#cada cuando caeran si son consecutivos
            )
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M")#guardamos el momento en que guardo el dato
            hoja.append([fecha, correo_esperado, asunto])#agregamos los datos a la hoja de excel     
    conexion.logout()#cerramos sesion
hoja.append(["Fecha", "Remitente", "Asunto"])#hacemos un encabezado para la tabla de excel en donde guardaremos los datos
#ahora hacemos un bucle para que el bot lea la bandeja cada cierto tiempo
intentos = 0
while intentos < 3:#colocamos la cantidad de veces que queremos que lea los mensajes
    lector_de_correos(remitente_esperado)#llamamos la funcion
    wb.save("log.xlsx")#guardamos los datos en excel después de cada revisión
    time.sleep(15)#cada cuanto queremos que lo intente
    intentos += 1