from openpyxl import Workbook#libreria para poder crear datos en excel
from plyer import notification
from email.header import decode_header
from datetime import datetime
import time
wb = Workbook()#crea un libro de excel
hoja = wb.active#crea una hoja en ese libro
hoja.title = "Log"#le coloca un titulo a la hoja
#datos a evaluar
correos_crudos = [
    {"From": "Juan Pérez <juan@gmail.com>", "Subject": "=?UTF-8?b?UmV1bmlvbiBtYcOxYW5h?=", "leido": False},
    {"From": "Banco Nacional <banco@notificacion.com>", "Subject": "=?UTF-8?b?TW92aW1pZW50byBlbiB0dSBjdWVudGE=?=", "leido": False},
    {"From": "María López <maria@trabajo.com>", "Subject": "=?UTF-8?b?SW5mb3JtZSBkZSB2ZW50YXM=?=", "leido": False},
    {"From": "Juan Pérez <juan@gmail.com>", "Subject": "=?UTF-8?b?QWN0dWFsaXphY2lvbiBkZWwgcHJveWVjdG8=?=", "leido": False},
    {"From": "Spam Promo <spam@promo.com>", "Subject": "=?UTF-8?b?T2ZlcnRhIGVzcGVjaWFs?=", "leido": False},
    {"From": "María López <maria@trabajo.com>", "Subject": "=?UTF-8?b?UmV1bmlvbiBkZSBlcXVpcG8=?=", "leido": False},
    {"From": "Juan Pérez <juan@gmail.com>", "Subject": "=?UTF-8?b?UHJlZ3VudGEgcnVwaWRh?=", "leido": False},
]
remitentes_importantes = ["juan@gmail.com", "maria@trabajo.com"]
#creamos la funcion para filtrar los correos
def revisar_correos(correos_evaluar, reminente_buscado):#los parametros seran la lista de correos y el reminente a buscar
    for i in correos_evaluar:#evaluara cada correo
        #es una lista compactada, por cada remitente que haya en la lista de remitentes a buscar evaluara si coincide con el From
        if any(remitente in i["From"] for remitente in reminente_buscado):
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
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M")#ingresamos la fecha del momento en que sucede
            hoja.append([fecha, reminente, asunto])#agregamos los datos a la hoja de excel
contador = 0
hoja.append(["Fecha", "Remitente", "Asunto"])#le agregamos un encabezado
while contador < 3:
    revisar_correos(correos_crudos, remitentes_importantes)
    wb.save("log.xlsx")#guardamos los datos después de cada revisión
    time.sleep(5)
    contador += 1