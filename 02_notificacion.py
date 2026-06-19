#ahora se vera la libreria plyer
#la libreria se encarga de enviar notificaciones nativas al escritorio de window
from plyer import notification#importaremos notification de plyer
from email.header import decode_header#ahora usaremos esta libreria
correos_crudos = [
    {"From": "Juan Pérez <juan@gmail.com>", "Subject": "=?UTF-8?b?UmV1bmlvbiBtYcOxYW5h?=", "leido": False},
    {"From": "Banco Nacional <banco@notificacion.com>", "Subject": "=?UTF-8?b?TW92aW1pZW50byBlbiB0dSBjdWVudGE=?=", "leido": False},
    {"From": "Juan Pérez <juan@gmail.com>", "Subject": "=?UTF-8?b?QWN0dWFsaXphY2lvbiBkZWwgcHJveWVjdG8=?=", "leido": False},
]
remitente_deseado = "juan@gmail.com"
for i in correos_crudos:
    if remitente_deseado in i["From"]:#evaluamos si el remitente deseado esta en el turno evaluado de la lista
        i["leido"] = True#cambiamos el valor de leido a true
        #primero cortara las cosas desde <, luego agarrara lo que este despues de eso, que es el correo que queremos, y despues
        correo_limpio = i["From"].split("<")[1].replace(">", "")#con replace quitamos > por un nada, para que se vea bien
        asunto = i["Subject"]#agarramos el asunto en crudo y lo convertimos en una variable
        #luego con decode va a a separar el lado utf-8, y b que es byte, en orden volviendolo indirectamente un array
        partes = decode_header(asunto)#dando un resultado tipo [b?el texto, utf-8]
        asunto_leido, codificado = partes[0]#luego de eso separamos el pimero como el asunt en crudo, y el resto como el codigo en el que esta
        if isinstance(asunto_leido, bytes):#ahora evaluando el mensaje en bytes volvera el asunto en crudo a leible
            asunto_leido = asunto_leido.decode(codificado or "utf-8")#usando el codificado, o utf-8 si el codificado llega a quedar vacio
        notification.notify(#luego usaremos notify el cual se encargara de mandarnos una notificacion local
            title = f"Nuevo correo de {correo_limpio}",#este sera el titulo del mensaje
            message = asunto_leido,#lo que dira el mensaje
            app_name = "Bot de correos",#este practicamente no hace nada, ya que suele dar el mensaje de python, pero por si las moscas
            timeout = 10,#segundos que dura visible
        )
