from flask import Flask, request, redirect, url_for, render_template_string, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Configuración de la aplicación
app = Flask(__name__)
app.secret_key = 'supersecreto123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///huéspedes.db'
db = SQLAlchemy(app)

# Modelo de Usuario
class Huesped(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    contrasena_hash = db.Column(db.String(128), nullable=False)

    def verificar_contrasena(self, contrasena):
        return check_password_hash(self.contrasena_hash, contrasena)

# Página de inicio
@app.route('/')
def home():
    if 'usuario_id' in session:
        return f"Bienvenido al panel de reservas, usuario ID: {session['usuario_id']}"
    return redirect(url_for('login'))

# Ruta de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        usuario = Huesped.query.filter_by(correo=correo).first()
        if usuario and usuario.verificar_contrasena(contrasena):
            session['usuario_id'] = usuario.id
            return redirect(url_for('home'))
        return "Credenciales incorrectas", 401

    return render_template_string('''
        <h2>Iniciar sesión</h2>
        <form method="post">
            Correo: <input type="email" name="correo" required><br>
            Contraseña: <input type="password" name="contrasena" required><br>
            <input type="submit" value="Entrar">
        </form>
    ''')

# Ruta para crear usuario de prueba
@app.route('/crear_usuario')
def crear_usuario():
    # Crea un usuario de prueba con correo y contraseña "1234"
    correo = 'test@correo.com'
    contrasena = '1234'
    if Huesped.query.filter_by(correo=correo).first() is None:
        nuevo = Huesped(correo=correo, contrasena_hash=generate_password_hash(contrasena))
        db.session.add(nuevo)
        db.session.commit()
        return "Usuario creado"
    return "El usuario ya existe"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
