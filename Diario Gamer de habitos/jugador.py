# ==========================================
# jugador.py
# ------------------------------------------
# Maneja la creación, visualización y mejora
# del jugador (nombre, XP, nivel, energía).
# ==========================================

def crear_jugador():
    """Pide el nombre del jugador y crea un perfil basico."""

    nombre = input("Ingrese el nombre de jugador: ")
    jugador = {
        'nombre': nombre,
        'nivel': 1,
        'xp': 0,
        'energia': 100
    }
    print(f"¡Bienvenido, {nombre}! Tu aventura comienza ahora.")
    return jugador


def ver_perfil(jugador):
    """Muestra el perfil actual del jugador."""

    print("\n--- Estadisticas del jugador ---")
    print(f"Nombre: {jugador['nombre']}")
    print(f"Nivel: {jugador['nivel']}")
    print(f"XP: {jugador['xp']}")
    print(f"Energía: {jugador['energia']}/100")
    print("-" * 35)


def subir_nivel(jugador):
    """Si el jugador tiene mas de 100 XP o mas, sube de nivel."""

    if jugador ['xp'] >= 100:
        jugador['nivel'] += 1
        jugador['xp'] -= 100
        jugador['energia'] = 100  # Restaurar energía al subir de nivel
        print(f"¡Felicidades {jugador['nombre']}! Has subido al nivel {jugador['nivel']}!")