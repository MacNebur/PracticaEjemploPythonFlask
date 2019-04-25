from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#Conexion base de datos
app.config['MYSQL_HOST'] = 'python.cy1dshhchfxf.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'python123'
app.config['MYSQL_PASSWORD'] = 'python123'
app.config['MYSQL_DB'] = 'servicioautomotriz'
mysql = MySQL(app)

# Sesion
app.secret_key = 'clavesecreta'

@app.route('/')
def index():
    return render_template('index.html')

#Agregar automovil
@app.route('/agregarautomovil', methods = ['POST'])
def agregarautomovil():
    if request.method == 'POST':
        #guardo en variables los valores
        placa = request.form['placa']
        modelo = request.form['modelo']
        marca = request.form['marca']
        linea = request.form['linea']
        color = request.form['color']
        #Insertar a mysql
        cur = mysql.connection.cursor()
        #Insertar consulta
        cur.execute('INSERT INTO automoviles (placa, modelo, marca, linea, color) VALUES (%s, %s, %s, %s, %s)',
        (placa, modelo, marca, linea, color))
        #Ejecucion de consulta
        mysql.connection.commit()
        #Mensaje
        flash('Automovil agregado correctamente')
        #Redireccionar a una url
        return redirect(url_for('paneladministrador'))

@app.route('/editarautomovil/<placa>')
def editarautomovil(placa):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM automoviles WHERE placa = %s', [placa])
    automovil = cur.fetchall()
    return render_template('editarAutomovil.html', automovil = automovil[0])

@app.route('/actualizarautomovil/<placa>', methods = ['POST'])
def actualizarautomovil(placa):
    if request.method == 'POST':
        #guardado en variables
        placaantigua = placa
        placa = request.form['placa']
        modelo = request.form['modelo']
        marca = request.form['marca']
        linea = request.form['linea']
        color = request.form['color']
        
        cur = mysql.connection.cursor()
        cur.execute(""" 
            UPDATE automoviles
            SET placa = %s,
                modelo = %s,
                marca = %s,
                linea = %s,
                color = %s
            WHERE placa = %s
        """, (placa, modelo, marca, linea, color, placaantigua))
        mysql.connection.commit()
        flash('Automovil actualizado correctamente')
        return redirect(url_for('paneladministrador'))

@app.route('/eliminarautomovil/<placa>')
def eliminarautomovil(placa):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM automoviles WHERE placa = %s', [placa])
    mysql.connection.commit()
    flash('Automovil eliminado correctamente')
    return redirect(url_for('paneladministrador'))

@app.route('/paneladministrador')
def paneladministrador():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM automoviles')
    automoviles = cur.fetchall()
    return render_template('paneladministrador.html', automoviles = automoviles)

app.run(host='0.0.0.0', debug=True)