from flask import Flask, request, redirect, url_for, render_template_string, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
db = SQLAlchemy(app)

# MODELOS
class Huesped(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contrasena_hash = db.Column(db.String(128), nullable=False)

    def verificar_contrasena(self, contrasena):
        return check_password_hash(self.contrasena_hash, contrasena)

class Habitacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(10), unique=True, nullable=False)
    disponible = db.Column(db.Boolean, default=True)

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    huesped_id = db.Column(db.Integer, db.ForeignKey('huesped.id'), nullable=False)
    habitacion_id = db.Column(db.Integer, db.ForeignKey('habitacion.id'), nullable=False)
    activa = db.Column(db.Boolean, default=True)

    huesped = db.relationship('Huesped')
    habitacion = db.relationship('Habitacion')

# INICIO DE SESIÓN SIMPLIFICADO
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        usuario = Huesped.query.filter_by(correo=correo).first()
        if usuario and usuario.verificar_contrasena(contrasena):
            session['usuario_id'] = usuario.id
            return redirect(url_for('mis_reservas'))
        return "Credenciales incorrectas", 401
    return render_template_string('''
        <h2>Iniciar sesión</h2>
        <form method="post">
            Correo: <input name="correo"><br>
            Contraseña: <input type="password" name="contrasena"><br>
            <input type="submit" value="Entrar">
        </form>
    ''')

# VER RESERVAS DEL HUÉSPED
@app.route('/reservas')
def mis_reservas():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    reservas = Reserva.query.filter_by(huesped_id=session['usuario_id'], activa=True).all()
    html = "<h2>Mis Reservas Activas</h2><ul>"
    for r in reservas:
        html += f"<li>Habitación {r.habitacion.numero} <a href='/cancelar_reserva/{r.id}'>Cancelar</a></li>"
    html += "</ul>"
    return html

# CANCELAR RESERVA
@app.route('/cancelar_reserva/<int:reserva_id>')
def cancelar_reserva(reserva_id):
    if 'usuario_id' not in session:
        return redirect(url_for('login'))

    reserva = Reserva.query.get_or_404(reserva_id)
    if reserva.huesped_id != session['usuario_id']:
        return "No autorizado", 403

    # Liberar la habitación
    habitacion = Habitacion.query.get(reserva.habitacion_id)
    habitacion.disponible = True

    # Eliminar o marcar como inactiva la reserva
    db.session.delete(reserva)
    db.session.commit()

    return redirect(url_for('mis_reservas'))

# CREAR DATOS DE PRUEBA
@app.route('/crear_datos')
def crear_datos():
    db.drop_all()
    db.create_all()

    h1 = Habitacion(numero="101", disponible=False)
    h2 = Habitacion(numero="102", disponible=True)
    db.session.add_all([h1, h2])

    u = Huesped(correo="huesped@correo.com", contrasena_hash=generate_password_hash("1234"))
    db.session.add(u)
    db.session.commit()

    r = Reserva(huesped_id=u.id, habitacion_id=h1.id)
    db.session.add(r)
    db.session.commit()

    return "Datos de prueba creados"

if __name__ == '__main__':
    app.run(debug=True)
