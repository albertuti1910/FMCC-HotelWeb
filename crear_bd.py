import sqlite3

# Conectar o crear la base de datos
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

# Confirmar cambios
conn.commit()
conn.close()

print("Base de datos y tabla 'clientes' creadas con éxito.")
