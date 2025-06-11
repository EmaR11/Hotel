pip install opencv-python pyzbar qrcode

import cv2
import qrcode
from pyzbar.pyzbar import decode

# -----------------------------
# Simulación de base de datos
# -----------------------------
reservas = {
    "123ABC": {"nombre": "Ana Pérez", "habitación": 101, "fecha": "2025-06-10"},
    "456DEF": {"nombre": "Carlos Ruiz", "habitación": 202, "fecha": "2025-06-12"},
    "789GHI": {"nombre": "Lucía Torres", "habitación": 303, "fecha": "2025-06-15"},
}

# -----------------------------
# Función para generar un QR (opcional)
# -----------------------------
def generar_qr(codigo_reserva):
    img = qrcode.make(codigo_reserva)
    nombre_archivo = f"qr_{codigo_reserva}.png"
    img.save(nombre_archivo)
    print(f"QR generado y guardado como '{nombre_archivo}'")

# Descomentar esta línea si querés generar un QR
# generar_qr("123ABC")

# -----------------------------
# Validación en tiempo real con cámara
# -----------------------------
def escanear_qr_con_camara():
    cap = cv2.VideoCapture(0)
    print("Escaneando... presioná 'q' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Decodificar códigos QR en el frame
        codigos = decode(frame)
        for codigo in codigos:
            datos = codigo.data.decode('utf-8')
            puntos = codigo.polygon

            # Dibujar un rectángulo alrededor del QR
            if puntos:
                pts = [(p.x, p.y) for p in puntos]
                cv2.polylines(frame, [np.array(pts)], isClosed=True, color=(0, 255, 0), thickness=3)

            # Mostrar datos del QR en pantalla
            cv2.putText(frame, datos, (codigo.rect.left, codigo.rect.top - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

            # Verificar si la reserva existe
            if datos in reservas:
                info = reservas[datos]
                print("✅ Reserva válida:")
                print(f"   Código: {datos}")
                print(f"   Huésped: {info['nombre']}")
                print(f"   Habitación: {info['habitación']}")
                print(f"   Fecha: {info['fecha']}")
            else:
                print("❌ Código de reserva no válido:", datos)

        # Mostrar la imagen en ventana
        cv2.imshow("Escáner QR - Presioná 'q' para salir", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# -----------------------------
# Ejecutar el escáner
# -----------------------------
if __name__ == "__main__":
    import numpy as np
    escanear_qr_con_camara()
