# ==========================================
# habitos.py
# ------------------------------------------
# Define las misiones del día y cómo se
# completan para ganar XP (experiencia).
# ==========================================

# Lista de misiones con su valor en XP
misiones = [
    {"nombre": "Estudiar 30 minutos", "xp": 20},
    {"nombre": "Hacer ejercicio", "xp": 25},
    {"nombre": "Leer un capítulo", "xp": 15},
    {"nombre": "Tomar 8 vasos de agua", "xp": 10},
    {"nombre": "Meditar 5 minutos", "xp": 15}
]


def mostrar_misiones():
    """Muestras las misiones disponibles para el día."""

    print("\n--- Misiones del Día: ---")
    for i, m in enumerate(misiones, start=1):
        print(f"{i}. {m['nombre']} (+{m['xp']} XP)")
    print("-" * 35)


def completar_misiones(jugador):
    """Permite al usuario marcxar misiones que completo.
        Aumenta el XP del jugador según las misiones completadas.
    """

    mostrar_misiones()
    respuesta = input("¿Cuales misiones completaste? (ej: 1,2,3,5): ")

    #Divide las misiones por comas
    try: 
        indices = [int(i.strip()) - 1 for i in respuesta.split(',')]
    except ValueError:
        print("Error: Usa números separados por comas.")
        return
    
    xp_ganado = 0
    for i in indices:
        if 0 <= i < len(misiones):
            xp_ganado += misiones[i]['xp']

    jugador['xp'] += xp_ganado
    jugador['energia'] -= 1

    print(f"\n Completaste {len(indices)} misiones.")
    print(f"Ganaste {xp_ganado} puntos de experincia")