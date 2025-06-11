import os
from datetime import datetime

# Simulación de base de datos (usado desde el sistema de reservas anterior)
usuarios = {
    "ana@mail.com": {"nombre": "Ana García", "password": "1234"},
    "juan@mail.com": {"nombre": "Juan Pérez", "password": "abcd"},
}

reservas = [
    {
        "reserva_id": "abc123",
        "usuario": "ana@mail.com",
        "tipo_habitacion": "doble",
        "fecha_entrada": "2024-12-01",
        "fecha_salida": "2024-12-05"
    },
    {
        "reserva_id": "xyz789",
        "usuario": "ana@mail.com",
        "tipo_habitacion": "suite",
        "fecha_entrada": "2023-07-15",
        "fecha_salida": "2023-07-20"
    }
]

# Función para autenticar al huésped
def autenticar_usuario():
    correo = input("Ingrese su correo: ").lower()
    contraseña = input("Ingrese su contraseña: ")
    usuario = usuarios.get(correo)
    
    if usuario and usuario["password"] == contraseña:
        print(f"\nBienvenido/a, {usuario['nombre']}\n")
        return correo
    else:
        print("Credenciales inválidas.\n")
        return None

# Función para ver el panel de reservas del huésped
def ver_panel(usuario_email):
    print("📋 Tus Reservas:\n")
    ahora = datetime.now()
    reservas_usuario = [r for r in reservas if r["usuario"] == usuario_email]
    
    if not reservas_usuario:
        print("No tenés reservas registradas.")
        return

    for r in reservas_usuario:
        entrada = datetime.strptime(r["fecha_entrada"], "%Y-%m-%d")
        salida = datetime.strp
