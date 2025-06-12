Trabajo Practico
Fecha: 11/7/2025
Alumnos: Chimbo Noel, Romero Valentina, Rivero Pablo

Sistema de Hotel

Historia 1: Registro de Huésped
Como huésped Quiero registrarme con mis datos personales
Para poder hacer reservas en el hotel

Criterios de Aceptación:
Dado que soy un nuevo usuario 
Cuando ingreso mis datos en el formulario de registro 
Entonces mi cuenta debe ser creada correctamente

Historia 2: Autenticación del Huésped
Como huésped Quiero iniciar sesión con mi correo 
y contraseña Para acceder a mi panel de reservas
Criterios de Aceptación:
Dado que ya tengo una cuenta Cuando ingreso mis credenciales
correctas Entonces debo poder acceder a mi cuenta

Historia 3: Validación de QR por Recepcionista
Como recepcionista Quiero escanear un código QR 
Para verificar la validez de la reserva del huésped

Criterios de Aceptación:
Dado que un huésped llega al hotel
Cuando presento el QR y este es escaneado Entonces se debe mostrar la información válida de la reserva

Historia 4: Realizar Reserva
Como huésped
Quiero seleccionar fechas, tipo de habitación y confirmar mi reserva
Para asegurar mi estadía en el hotel

Criterios de Aceptación:
Dado que estoy autenticado
Cuando selecciono una habitación disponible y confirmo
Entonces el sistema debe registrar la reserva y generar un código QR

Historia 5: Cancelar Reserva
Como huésped
Quiero cancelar una reserva activa
Para liberar la habitación si ya no voy a asistir

Criterios de Aceptación:
Dado que tengo una reserva
Cuando hago clic en “Cancelar”
Entonces la reserva debe eliminarse del sistema y la habitación quedar disponible

Historia 6: Gestión de Habitaciones
Como administrador del hotel
Quiero agregar, modificar o eliminar habitaciones
Para tener control sobre la disponibilidad y tipos de habitaciones

Criterios de Aceptación:
Dado que soy administrador
Cuando ingreso a la gestión de habitaciones
Entonces puedo ver, agregar, editar o eliminar habitaciones existentes

Historia 7: Panel del Huésped
Como huésped
Quiero ver un resumen de mis reservas activas y pasadas
Para poder gestionar mis viajes y confirmaciones

Criterios de Aceptación:
Dado que accedí con mi cuenta
Cuando entro a “Mis Reservas”
Entonces puedo ver todas mis reservas, estado, fechas, habitación y QR

Historia 8: Reportes de Reservas (Administrador)
Como administrador
Quiero generar reportes de reservas por fechas
Para tener control de ocupación y planificación del hotel

Criterios de Aceptación:
Dado que soy administrador
Cuando selecciono un rango de fechas
Entonces el sistema muestra el total de reservas, huéspedes y habitaciones ocupadas
