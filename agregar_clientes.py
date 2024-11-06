from dotenv import load_dotenv
import os
import sqlite3

# Cargar las variables de entorno
load_dotenv()

def crear_base_datos():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    # Crear la tabla si no existe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        correo TEXT,
        comunicaciones INTEGER
    )
    ''')
    conn.commit()
    conn.close()
    print("Base de datos y tabla 'clientes' creadas con éxito.")

def clear_db():
    # Eliminar el archivo de la base de datos si existe
    if os.path.exists('clientes.db'):
        os.remove('clientes.db')
        print("La base de datos existente ha sido eliminada.")

    # Crear una nueva base de datos con la tabla 'clientes'
    crear_base_datos()

def agregar_o_actualizar_cliente(nombre, correo, comunicaciones):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()

    # Verificar si el correo ya existe en la base de datos
    cursor.execute("SELECT * FROM clientes WHERE correo = ?", (correo,))
    cliente = cursor.fetchone()

    if cliente:
        # Si el cliente existe, actualizar sus datos
        cursor.execute("UPDATE clientes SET nombre = ?, comunicaciones = ? WHERE correo = ?", 
                      (nombre, comunicaciones, correo))
        print(f"Cliente {nombre} actualizado con éxito.")
    else:
        # Si el cliente no existe, insertar uno nuevo
        cursor.execute("INSERT INTO clientes (nombre, correo, comunicaciones) VALUES (?, ?, ?)",
                      (nombre, correo, comunicaciones))
        print(f"Cliente {nombre} agregado con éxito.")

    conn.commit()
    conn.close()

# Crear una nueva base de datos o limpiar y crear desde cero
clear_db()

# Agregar o actualizar varios clientes usando los correos del archivo .env
clientes = [
    ("Alberto", os.getenv("CORREO_ALBERTO"), 1),
    ("Carlota", os.getenv("CORREO_CARLOTA"), 1),
    ("Joel", os.getenv("CORREO_JOEL"), 1),
    ("Dani", os.getenv("CORREO_DANI"), 1),
]

for nombre, correo, comunicaciones in clientes:
    if correo:
        agregar_o_actualizar_cliente(nombre, correo, comunicaciones)
    else:
        print(f"El correo de {nombre} no está definido en el archivo .env.")
