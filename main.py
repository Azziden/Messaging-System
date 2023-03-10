import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Credenciales de correo electrónico
correo_origen = os.environ['CORREO_ELECTRONICO']
contraseña = os.environ['CONTRASEÑA']

# Configuración del servidor SMTP de Gmail
servidor_smtp = 'smtp.gmail.com'
puerto_smtp = 587

# Crea un objeto de mensaje MIME
mensaje = MIMEMultipart()
mensaje['From'] = correo_origen
mensaje['To'] = 'destinatario@example.com'
mensaje['Subject'] = 'Asunto del correo electrónico'

# Cuerpo del correo electrónico
cuerpo = 'Este es el cuerpo del correo electrónico.'
mensaje.attach(MIMEText(cuerpo, 'plain'))

# Crea una conexión al servidor SMTP de Gmail
smtp_server = smtplib.SMTP(servidor_smtp, puerto_smtp)
smtp_server.starttls()

# Inicia sesión en la cuenta de correo electrónico
smtp_server.login(correo_origen, contraseña)

# Envía el correo electrónico
texto = mensaje.as_string()
smtp_server.sendmail(correo_origen, 'destinatario@example.com', texto)

# Cierra la conexión al servidor SMTP
smtp_server.quit()
