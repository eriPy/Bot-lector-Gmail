import os#para leer variables del sistema
import imaplib#para conectarse al servidor IMAP
import email#para convertir el correo crudo a objeto leible
from email.header import decode_header#para decodificar asuntos codificados
from dotenv import load_dotenv#para leer el archivo .env
load_dotenv()#lee el archivo .env y carga las variables
correo = os.getenv("GMAIL_USER")#agarra el valor de GMAIL_USER del correo que recibira los mensajes del .env
contraseña = os.getenv("GMAIL_PASS")# agarra el valor de GMAIL_PASS del .env
conexion = imaplib.IMAP4_SSL("imap.gmail.com", 993)#entra al servidor de Gmail en el puerto 993 con conexión segura
conexion.login(correo, contraseña)#identifica las credenciales para entrar
conexion.select("INBOX")#seleccionamos la bandeja de entrada
# buscamos correos no leídos
_, mensajes = conexion.search(None, "UNSEEN")
ids_correos = mensajes[0].split()
print(f"Correos no leídos: {len(ids_correos)}")
for id_correo in ids_correos:
    _, datos = conexion.fetch(id_correo, "(RFC822)")
    mensaje = email.message_from_bytes(datos[0][1])
    # extraer remitente
    remitente = mensaje["From"]
    # extraer y decodificar asunto
    asunto_crudo = mensaje["Subject"]
    partes = decode_header(asunto_crudo)[0]
    asunto, encoding = partes
    if isinstance(asunto, bytes):
        asunto = asunto.decode(encoding or "utf-8")
    print(f"De: {remitente}")
    print(f"Asunto: {asunto}")
    print("---")
conexion.logout()