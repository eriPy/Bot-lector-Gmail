from email.header import decode_header#ahora usaremos esta libreria
import re#usarmos la libreria re para buscar palabras
#--------------ejercicio_1--------------------------------------
correos = [#primro declaramos la lista de correos, asustons y si los hemos leido
    {"de": "juan@gmail.com", "asunto": "Reunión mañana", "leido": False},
    {"de": "spam@promo.com", "asunto": "Oferta especial", "leido": False},
    {"de": "juan@gmail.com", "asunto": "Actualización del proyecto", "leido": False},
    {"de": "banco@notificacion.com", "asunto": "Movimiento en tu cuenta", "leido": False},
    {"de": "juan@gmail.com", "asunto": "¿Viste mi mensaje?", "leido": False},
]
remitente_importante = "juan@gmail.com"#seleccionamos el remitente del que queremos recibir
print(f"correos recibidos de {remitente_importante}")
for i in correos:#primero buscaremos en cada objeto de esta lista
    if i["de"] == remitente_importante:#si es de remitente que queremos hara lo siguiente
        i["leido"] = True#volvera True el leido
        print(f"de: {i["de"]}\nAsunto: {i["asunto"]}\nLeido: {i["leido"]}")#va a mostrar el siguiente mensaje
#---------------ejercicio_2-------------------------------
correos_crudos = [#ahora un correo que si revisara el bot
    {#son practicamete lo mismo pero ahora se debera mostrar de manera legible
        "From": "Juan Pérez <juan@gmail.com>",
        "Subject": "=?UTF-8?b?UmV1bmlvbiBtYcOxYW5h?=",
        "leido": False
    },
    {
        "From": "Banco Nacional <banco@notificacion.com>",
        "Subject": "=?UTF-8?b?TW92aW1pZW50byBlbiB0dSBjdWVudGE=?=",
        "leido": False
    },
    {
        "From": "Juan Pérez <juan@gmail.com>",
        "Subject": "=?UTF-8?b?QWN0dWFsaXphY2lvbiBkZWwgcHJveWVjdG8=?=",
        "leido": False
    },
]
print("REVISION DE CORREOS EN CRUDO")
for i in correos_crudos:
    if remitente_importante in i['From']:#si el remitente que queremos esta en from
        i['leido'] = True#volveremos true para que sea leido
        asunto_crudo = i['Subject']#luego el asunto crudo sera el subject de la lista
        partes = decode_header(asunto_crudo)
        asunto, encoding = partes[0]
        if isinstance(asunto, bytes):
            asunto = asunto.decode(encoding or "utf-8")
        print(f"De: {i['From']}\nAsunto: {asunto}\nLeido: {i['leido']}")
#---------------ejercicio_3----------------------------
nuevos_correos_crudos = [
    {"From": "Juan Pérez <juan@gmail.com>", "Subject": "=?UTF-8?b?UmV1bmlvbiBtYcOxYW5h?=", "leido": False},
    {"From": "Banco Nacional <banco@notificacion.com>", "Subject": "=?UTF-8?b?TW92aW1pZW50byBlbiB0dSBjdWVudGE=?=", "leido": False},
    {"From": "Juan Pérez <juan@gmail.com>", "Subject": "=?UTF-8?b?QWN0dWFsaXphY2lvbiBkZWwgcHJveWVjdG8=?=", "leido": False},
]
nuevo_remitente_importante = "juan@gmail.com"
print('Parseo completo + filtrado')
for i in nuevos_correos_crudos:
    if nuevo_remitente_importante in i["From"]:
        i["leido"] = True
        correo_limpio = i["From"].split("<")[1].replace(">", "")
        nuevo_asunto = i["Subject"]
        nuevas_partes = decode_header(nuevo_asunto)
        asunto_leido, codificado = nuevas_partes[0]
        if isinstance(asunto_leido, bytes):
            asunto_leido = asunto_leido.decode(codificado or "utf-8")
        print(f"De: {correo_limpio}\nAsunto: {asunto_leido}\nLeido: {i['leido']}")
        print("---")