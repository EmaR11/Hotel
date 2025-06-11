pip install qrcode[pil]

import qrcode
import uuid
from datetime import datetime

# Simulación de usuarios registrados
usuarios = {
    "ana@mail.com": {"nombre": "Ana García", "password": "1234"},
    "juan@mail.com": {"nombre": "Juan Pérez", "password": "abcd"},
}

# Tipos de habitaciones disponibles
habitaciones_disponibles = {
    "individual": 5,
    "doble": 3,
    "suite": 2
}

# Reservas registradas
reservas = []

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

# Función para realizar una reserva
def realizar_reserva(usuario_email):
    print("Tipos de habitación disponibles:")
    for tipo, cantidad in habitaciones_disponibles.items():
        print(f"- {tipo.capitalize()} ({cantidad} disponibles)")
    
    tipo_habitacion = input("\nSeleccione tipo de habitación: ").lower()
    if tipo_habitacion not in habitaciones_disponibles or habitaciones_disponibles[tipo_habitacion] <= 0:
        print("Tipo de habitación no disponible.\n")
        return

    fecha_entrada = input("Ingrese la fecha de entrada (YYYY-MM-DD): ")
    fecha_salida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
    
    try:
        datetime.strptime(fecha_entrada, "%Y-%m-%d")
        datetime.strptime(fecha_salida, "%Y-%m-%d")
    except ValueError:
        print("Formato de fecha inválido.\n")
        return

    reserva_id = str(uuid.uuid4())[:8]
    reserva = {
        "reserva_id": reserva_id,
        "usuario": usuario_email,
        "tipo_habitacion": tipo_habitacion,
        "fecha_entrada": fecha_entrada,
        "fecha_salida": fecha_salida
    }
    
    reservas.append(reserva)
    habitaciones_disponibles[tipo_habitacion] -= 1
    print("\n✅ ¡Reserva confirmada!")

    generar_qr(reserva)
    print("QR generado con los datos de la reserva.\n")

# Función para generar QR
def generar_qr(reserva):
    datos_qr = f"""Reserva ID: {reserva['reserva_id']}
Email: {reserva['usuario']}
Habitación: {reserva['tipo_habitacion']}
Entrada: {reserva['fecha_entrada']}
Salida: {reserva['fecha_salida']}"""

    qr = qrcode.make(datos_qr)
    qr.save(f"reserva_{reserva['reserva_id']}.png")

# Programa principal
def main():
    print("🛎️ Bienvenido al sistema de reservas del hotel\n")
    usuario = None

    while not usuario:
        usuario = autenticar_usuario()
    
    realizar_reserva(usuario)

if __name__ == "__main__":
    main()
