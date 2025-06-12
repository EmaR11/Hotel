from datetime import date
from typing import List, Set, Dict


# Modelo de Reserva
class Reserva:
    def __init__(self, id_reserva: int, huesped_id: int, habitacion_num: int, fecha_inicio: date, fecha_fin: date):
        if fecha_inicio > fecha_fin:
            raise ValueError("La fecha de inicio no puede ser posterior a la fecha de fin.")
        
        self.id_reserva = id_reserva
        self.huesped_id = huesped_id
        self.habitacion_num = habitacion_num
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def esta_en_rango(self, desde: date, hasta: date) -> bool:
        """Determina si esta reserva se superpone con el rango especificado."""
        return self.fecha_inicio <= hasta and self.fecha_fin >= desde

    def __repr__(self):
        return (f"Reserva({self.id_reserva}: Huesped {self.huesped_id}, "
                f"Habitación {self.habitacion_num}, {self.fecha_inicio} a {self.fecha_fin})")


# Generador de Reportes
class GeneradorReporteReservas:
    def __init__(self, reservas: List[Reserva]):
        self.reservas = reservas

    def generar_reporte(self, desde: date, hasta: date) -> Dict[str, int]:
        if desde > hasta:
            raise ValueError("La fecha 'desde' no puede ser posterior a la fecha 'hasta'.")

        reservas_filtradas = [r for r in self.reservas if r.esta_en_rango(desde, hasta)]
        
        huespedes: Set[int] = set()
        habitaciones: Set[int] = set()

        for r in reservas_filtradas:
            huespedes.add(r.huesped_id)
            habitaciones.add(r.habitacion_num)

        return {
            "total_reservas": len(reservas_filtradas),
            "total_huespedes": len(huespedes),
            "habitaciones_ocupadas": len(habitaciones)
        }

    def mostrar_reporte(self, desde: date, hasta: date):
        datos = self.generar_reporte(desde, hasta)
        print("\n📊 Reporte de Reservas")
        print(f"   Rango: {desde} a {hasta}")
        print(f"   - Total de Reservas:        {datos['total_reservas']}")
        print(f"   - Total de Huéspedes únicos: {datos['total_huespedes']}")
        print(f"   - Habitaciones Ocupadas:    {datos['habitaciones_ocupadas']}")


# ---------- DEMO DE USO ----------
def demo_reportes():
    reservas = [
        Reserva(1, 201, 101, date(2025, 6, 10), date(2025, 6, 12)),
        Reserva(2, 202, 102, date(2025, 6, 11), date(2025, 6, 14)),
        Reserva(3, 203, 103, date(2025, 6, 15), date(2025, 6, 18)),
        Reserva(4, 201, 101, date(2025, 6, 20), date(2025, 6, 22)),  # mismo huésped, otra reserva
    ]

    reporteador = GeneradorReporteReservas(reservas)

    # Consulta válida
    reporteador.mostrar_reporte(date(2025, 6, 10), date(2025, 6, 15))

    # Consulta parcial
    reporteador.mostrar_reporte(date(2025, 6, 13), date(2025, 6, 21))

    # Consulta vacía
    reporteador.mostrar_reporte(date(2025, 7, 1), date(2025, 7, 10))


if __name__ == "__main__":
    demo_reportes()
