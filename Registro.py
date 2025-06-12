# Simulación de una base de datos en memoria
usuarios_registrados = {}

class RegistroInvalido(Exception):
    pass

class UsuarioExistente(Exception):
    pass

class Huesped:
    def __init__(self, nombre, apellido, email, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email.lower()
        self.contraseña = contraseña  # En un sistema real, se debe encriptar

    def __repr__(self):
        return f"Huésped({self.nombre} {self.apellido}, {self.email})"

class RegistroHuesped:
    @staticmethod
    def registrar(nombre, apellido, email, contraseña):
        # Validación de campos obligatorios
        if not all([nombre, apellido, email, contraseña]):
            raise RegistroInvalido("Todos los campos son obligatorios.")
        
        email = email.lower()
        # Validar si el correo ya está registrado
        if email in usuarios_registrados:
            raise UsuarioExistente(f"El correo '{email}' ya está registrado.")

        # Crear nuevo huésped
        nuevo_huesped = Huesped(nombre, apellido, email, contraseña)
        usuarios_registrados[email] = nuevo_huesped
        return nuevo_huesped

# ---------- Ejemplo de uso (simulación) ----------

def simular_registro():
    try:
        huesped = RegistroHuesped.registrar(
            nombre="Lucía",
            apellido="Pérez",
            email="lucia@example.com",
            contraseña="password123"
        )
        print("Registro exitoso:", huesped)
    except RegistroInvalido as e:
        print("Error de validación:", e)
    except UsuarioExistente as e:
        print("Error de registro:", e)

simular_registro()
