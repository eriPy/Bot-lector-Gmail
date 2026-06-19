# Bot Lector de Correos

Bot en python que se asegura de en este caso, revisar correos no leidos, y orientado a revisar si hay correos de un correo en especifico

## ¿Qué hace?
- Se conecta a Gmail via IMAP
- Filtra correos por remitente
- Envía notificación de escritorio
- Guarda los datos del correo en Excel(fecha/remitente/asunto)

## Instalación
1. Clonar el repositorio
2. pip install -r requirements.txt
3. Crear archivo .env con tus credenciales (ver .env.example)
4. Correr revisor_de_correos.py

## Tecnologías
Python, imaplib, openpyxl, plyer, python-dotenv

## 🚀 Cómo usar

### 1. Clonar el repositorio
\`\`\`bash
git clone https://github.com/TU_USUARIO/gmail-bot.git
cd gmail-bot
\`\`\`

### 2. Crear archivo `.env`
\`\`\`bash
cp .env.example .env
\`\`\`

### 3. Editar el `.env` con tus datos
Abre el archivo `.env` y completa:
\`\`\`
GMAIL_USER=tu_email@gmail.com
GMAIL_PASSWORD=tu_contraseña_app_16_digitos
TARGET_EMAIL=correo_a_monitorear@gmail.com
\`\`\`

### 4. Instalar dependencias
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 5. Ejecutar
\`\`\`bash
python 06_revisor_de_correos.py
\`\`\`

## Seguridad
- **NUNCA** subir el archivo '.env' conlas creedenciales reales
- **USAR** contraseña de 16 digitos de google, no la normal

## Estructura del proyecto
- 01_parseo.py muestra como decodificar el correo porque los reales no son leibles
- 02_notificacion.py muestra como notificar localmente en caso de que encontro un resultado
- 03_txt_loop.py  muestra como agregar la informacion encontrada a un archivo txt y como hacerlo bucle
- 04_excel_loop.py muestra como agregar la informacion a Excel
- 05_conexion_gmail.py muestra como se conectara a Gmail para revisar los correos
- 06_revisor_de_correos.py es la estructura del proyecto final