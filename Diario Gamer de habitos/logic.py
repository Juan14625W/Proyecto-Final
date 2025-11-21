"""
logic.py
Lógica principal del Diario Gamer de Hábitos.
Maneja experiencia, niveles, energía y hábitos.
"""

from datetime import date, datetime


# -----------------------------
# SISTEMA DE XP Y NIVELES
# -----------------------------

def calcular_nivel(xp_actual):
    nivel = (xp_actual // 100) + 1
    return nivel


def agregar_experiencia(data, xp_ganada):
    data["jugador"]["xp"] += xp_ganada
    data["jugador"]["nivel"] = calcular_nivel(data["jugador"]["xp"])

    # Recuperación de energía
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
# HISTORIAL
# -----------------------------

def registrar_historial(data):
    """
    Guarda una entrada diaria en el historial.
    """
    hoy = str(date.today())

    entrada = {
        "fecha": hoy,
        "xp": data["jugador"]["xp"],
        "nivel": data["jugador"]["nivel"],
        "energia": data["jugador"]["energia"]
    }

    data["historial"].append(entrada)
    return data


def maximo_xp_mes(data):
    """
    Devuelve el máximo XP registrado en el mes actual.
    """
    if "historial" not in data or not data["historial"]:
        return None

    hoy = datetime.today()
    registros_mes = []

    for h in data["historial"]:
        try:
            fecha = datetime.fromisoformat(h["fecha"])
            if fecha.month == hoy.month and fecha.year == hoy.year:
                registros_mes.append(h["xp"])
        except:
            pass

    if not registros_mes:
        return None

    return max(registros_mes)


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