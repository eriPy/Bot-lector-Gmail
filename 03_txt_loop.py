from plyer import notification
from email.header import decode_header
from datetime import datetime
import time
#primero creamos una funcion la cual evalue, decodifique, notifique y anote los mensajes para llamarla cuando sea necesario
def revisar_correos(correos_evaluar, reminente_buscado):#los parametros seran la lista de correos y el reminente a buscar
    for i in correos_evaluar:#evaluara cada correo
        if reminente_buscado in i["From"]:#evaluara si el remitente esta en From
            i["leido"] = True#marca como leido el correo
            reminente = i["From"].split("<")[1].replace(">", "")#limpia el remitente para que solo se vea el correo
            asunto_crudo = i["Subject"]#tomams el asunto en crudo
            partes_asunto_crudo = decode_header(asunto_crudo)#luego lo dividimos en una lista tipo: ["mensaje", "codigo"]
            asunto_codificado, codigo = partes_asunto_crudo[0]#separamos la lista
            if isinstance(asunto_codificado, bytes):#si esta en bytes
                asunto = asunto_codificado.decode(codigo or "utf-8")#va a cambiar el codigo a utf-8 para que sea leible
            notification.notify(#va a notificar mostrando
                title = f'Nuevo correo de {reminente}',#de quien es el correo
                message = asunto,#el asunto
                app_name = "Bot",#el bot 
                timeout = 10,#el tiempo que mostrara la notificacion
            )
            #luego con un open añadiremos la informacion de la fecha/reminente/asunto del correo en un .txt
            with open("log_correos.txt", "a", encoding = "utf-8") as archivo:#en un archivo .txt o creamos ese archivo
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M")#ingresamos la fecha del momento en que sucede
                archivo.write(f"{fecha} De: {reminente} - Asunto: {asunto}\n")#añadimos estos datos
#informacion a usar:
correos_crudos = [#correos en crudo
    {"From": "Juan Pérez <juan@gmail.com>", "Subject": "=?UTF-8?b?UmV1bmlvbiBtYcOxYW5h?=", "leido": False},
    {"From": "Banco Nacional <banco@notificacion.com>", "Subject": "=?UTF-8?b?TW92aW1pZW50byBlbiB0dSBjdWVudGE=?=", "leido": False},
    {"From": "Juan Pérez <juan@gmail.com>", "Subject": "=?UTF-8?b?QWN0dWFsaXphY2lvbiBkZWwgcHJveWVjdG8=?=", "leido": False},
]
remitente_deseado = "juan@gmail.com"
contador = 0#creamos un contador de las veces que evaluara los datos
while contador < 3: #cuando alla evaluado todo 3 veces terminara
    revisar_correos(correos_crudos, remitente_deseado)#evalua los datos
    time.sleep(5)#cada 5 segundos
    contador += 1#cada evaluacion aumenta el contador en 1