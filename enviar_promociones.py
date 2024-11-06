import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import sqlite3

# Cargar las variables de entorno
load_dotenv()

def enviar_correo(destinatario, nombre, asunto, mensaje):
    remitente = os.getenv("EMAIL_USER")
    contraseña = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Personalizar el mensaje con el nombre del cliente
    mensaje_personalizado = mensaje.format(nombre=nombre)
    msg.attach(MIMEText(mensaje_personalizado, 'html'))  # Cambiar 'html' para contenido HTML

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Activar la conexión segura TLS
            server.login(remitente, contraseña)
            server.sendmail(remitente, destinatario, msg.as_string())
        print(f"Correo enviado a {nombre} ({destinatario})")
    except Exception as e:
        print(f"No se pudo enviar el correo a {nombre} ({destinatario}): {e}")

def enviar_promociones():
    # Definir el asunto y el mensaje HTML
    asunto = "Promoción Especial del Navidad"
    mensaje = """
    <html>
        <body style="text-align: center; font-family: Arial, sans-serif; color: #333;">
            <h2>Hola {nombre},</h2>
            <p>¡Te invitamos a descubrir nuestra promoción especial para esta Navidad!</p>
            <div style="display: flex; justify-content: center;">
                <img src="https://raw.githubusercontent.com/albertuti1910/FMCC-HotelWeb/main/images/hotel-riu-palace-maspalomas.jpg"
                    alt="Hotel Riu Palace Maspalomas"
                    style="width:100%; max-width:600px; border-radius:8px;">
            </div>
            <p><strong>Descuento exclusivo del 20%</strong> en reservas de mínimo 3 noches usando el código:</p>
            <h3 style="color: #e63946;">NAVIDAD2024</h3>
            <p>Además, disfruta de desayuno gratuito y experiencias únicas en nuestra región.</p>
            <p><a href="https://albertuti1910.github.io/FMCC-HotelWeb/" style="color: blue;">Reserva ahora y asegura tu lugar</a></p>
            <p>¡Te esperamos!</p>
            <br>
            <p>Saludos,<br>El equipo de Riu Palace Maspalomas</p>
            <hr>
            <p style="font-size: small; color: gray;">
                Si deseas dejar de recibir promociones, haz clic en el siguiente enlace:
                <a href="https://albertuti1910.github.io/FMCC-HotelWeb/unsubscribe.html" style="color: red;">Cancelar suscripción</a>
            </p>
        </body>
    </html>
    """

    # Obtener clientes que desean recibir promociones
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, correo FROM clientes WHERE comunicaciones = 1")
    clientes = cursor.fetchall()
    conn.close()

    # Enviar correo a cada cliente
    for nombre, correo in clientes:
        enviar_correo(correo, nombre, asunto, mensaje)

# Ejemplo de uso: Enviar promociones a los clientes interesados
enviar_promociones()
