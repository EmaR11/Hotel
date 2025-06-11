from typing import Dict, List


# Excepciones personalizadas
class HabitacionError(Exception):
    pass

class HabitacionNoEncontrada(HabitacionError):
    pass

class HabitacionExistente(HabitacionError):
    pass


# Modelo de habitación
class Habitacion:
    def __init__(self, numero: int, tipo: str, disponible: bool = True):
        self.numero = numero
        self.tipo = tipo.capitalize()  # Simple, Doble, Suite...
        self.disponible = disponible

    def actualizar(self, tipo: str = None, disponible: bool = None):
        if tipo:
            self.tipo = tipo.capitalize()
        if disponible is not None:
            self.disponible = disponible

    def __repr__(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero} - {self.tipo} ({estado})"


# Servicio de gestión de habitaciones
class GestionHabitaciones:
    def __init__(self):
        self.habitaciones: Dict[int, Habitacion] = {}

    def agregar(self, numero: int, tipo: str) -> Habitacion:
        if numero in self.habitaciones:
            raise HabitacionExistente(f"Ya existe la habitación número {numero}.")
        nueva = Habitacion(numero, tipo)
        self.habitaciones[numero] = nueva
        return nueva

    def editar(self, numero: int, tipo: str = None, disponible: bool = None) -> Habitacion:
        habitacion = self.habitaciones.get(numero)
        if not habitacion:
            raise HabitacionNoEncontrada(f"No se encontró la habitación número {numero}.")
        habitacion.actualizar(tipo, disponible)
        return habitacion

    def eliminar(self, numero: int) -> None:
        if numero not in self.habitaciones:
            raise HabitacionNoEncontrada(f"No se puede eliminar: la habitación {numero} no existe.")
        del self.habitaciones[numero]

    def listar(self) -> List[Habitacion]:
        return list(self.habitaciones.values())


# ----------- DEMO: Uso del sistema -----------

def demo_gestion():
    gestion = GestionHabitaciones()

    try:
        print("📌 Agregando habitaciones...")
        gestion.agregar(101, "simple")
        gestion.agregar(102, "doble")
        gestion.agregar(103, "s
