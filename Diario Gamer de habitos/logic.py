"""
logic.py
Lógica principal del Diario Gamer de Hábitos.
Maneja experiencia, niveles, energía y hábitos.
"""

# -----------------------------
# SISTEMA DE XP Y NIVELES
# -----------------------------

def calcular_nivel(xp_actual):
    nivel = (xp_actual // 100) + 1
    return nivel


def agregar_experiencia(data, xp_ganada):
    data["jugador"]["xp"] += xp_ganada
    data["jugador"]["nivel"] = calcular_nivel(data["jugador"]["xp"])

    # Recupera energía
    data["jugador"]["energia"] += 5
    if data["jugador"]["energia"] > 100:
        data["jugador"]["energia"] = 100

    return data


# -----------------------------
# SISTEMA DE HÁBITOS
# -----------------------------

def agregar_habito(data, nombre_habito):
    nuevo = {
        "nombre": nombre_habito,
        "completado": False
    }
    data["habitos"].append(nuevo)
    return data


def mostrar_habitos(data):
    if not data["habitos"]:
        print("\n No tienes hábitos registrados aún.")
        return

    print("\n=== TUS HÁBITOS ===")
    for i, hab in enumerate(data["habitos"], start=1):
        estado = "✅" if hab["completado"] else "❌"
        print(f"{i}. {hab['nombre']} - {estado}")


def completar_habito(data, indice):
    if indice < 1 or indice > len(data["habitos"]):
        print("Número de hábito inválido.")
        return data

    hab = data["habitos"][indice - 1]

    if hab["completado"]:
        print("Ya completaste este hábito antes.")
    else:
        hab["completado"] = True
        data = agregar_experiencia(data, 20)
        print(f"Completaste '{hab['nombre']}' y ganaste +20 XP!")

    return data


def reiniciar_habitos(data):
    for h in data["habitos"]:
        h["completado"] = False
    print("🌞 Nuevo día, hábitos reiniciados.")
    return data


# -----------------------------
# ESTADO DEL JUGADOR
# -----------------------------

def mostrar_estado(data):
    jugador = data["jugador"]

    print("\n=== ESTADO DEL JUGADOR ===")
    print(f"👤 Nombre: {jugador['nombre']}")
    print(f"⭐ Nivel: {jugador['nivel']}")
    print(f"⚡ Energía: {jugador['energia']}")
    print(f"🧩 XP Total: {jugador['xp']}")
