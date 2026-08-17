from flask import Flask, render_template, request, jsonify, session
import sqlite3

app = Flask(__name__)
app.secret_key = "clave_secreta_para_pos"

def get_db():
    conn = sqlite3.connect("pos_tienda.db")
    conn.row_factory = sqlite3.Row
    return conn

# Crear tablas si no existen
def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo_barras TEXT UNIQUE,
            nombre TEXT NOT NULL,
            precio_compra REAL NOT NULL,
            precio_venta REAL NOT NULL,
            stock INTEGER NOT NULL,
            stock_minimo INTEGER DEFAULT 5
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS caja_turnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_apertura DATETIME DEFAULT CURRENT_TIMESTAMP,
            monto_inicial_efectivo REAL NOT NULL,
            estado TEXT DEFAULT 'ABIERTA'
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno_id INTEGER,
            fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
            metodo_pago TEXT NOT NULL,
            total REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def inicio():
    return "<h1>¡Sistema Punto de Venta Activo!</h1><p>El backend y la base de datos están funcionando correctamente.</p>"

if __name__ == '__main__':
    app.run(debug=True)
