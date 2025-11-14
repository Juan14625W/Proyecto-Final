"""
data_manager.py
Gestión de perfiles del Diario Gamer de Hábitos usando archivos JSON.

Autor: Juan David Paz Rodríguez
Proyecto: Diario Gamer de Hábitos
Versión: simple, sin pathlib ni datetime
"""

import json
import os

# Carpeta donde se guardarán los archivos de los jugadores
DATA_FOLDER = "data"

# Estructura base del jugador
DEFAULT_STRUCTURE = {
    "jugador": {
        "nombre": "",
        "nivel": 1,
        "xp": 0,
        "energia": 100
    },
    "habitos": []
}


# ------------------------------
# FUNCIONES PRINCIPALES
# ------------------------------

def ensure_data_folder():
    """Crea la carpeta 'data' si no existe."""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)


def get_profile_path(nombre):
    """
    Retorna la ruta del archivo JSON del jugador.
    Ejemplo: data/JuanKnight.json
    """
    ensure_data_folder()
    nombre_archivo = nombre.strip().replace(" ", "_") + ".json"
    return os.path.join(DATA_FOLDER, nombre_archivo)


def create_new_profile(nombre):
    """
    Crea un nuevo perfil JSON para el jugador.
    Si ya existe uno con el mismo nombre, se sobrescribe.
    """
    data = DEFAULT_STRUCTURE.copy()
    data["jugador"]["nombre"] = nombre
    save_progress(nombre, data)
    return data


def save_progress(nombre, data):
    """
    Guarda el progreso del jugador en un archivo JSON.
    """
    ruta = get_profile_path(nombre)
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, ensure_ascii=False, indent=4)


def load_progress(nombre):
    """
    Carga el progreso del jugador desde su archivo JSON.
    Si no existe o está dañado, crea uno nuevo.
    """
    ruta = get_profile_path(nombre)
    if not os.path.exists(ruta):
        return create_new_profile(nombre)

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
            return data
    except Exception:
        print("⚠️ Archivo dañado o ilegible. Se creará un nuevo perfil.")
        return create_new_profile(nombre)


def list_profiles():
    """
    Devuelve una lista con los nombres de los jugadores guardados.
    """
    ensure_data_folder()
    perfiles = []
    for archivo in os.listdir(DATA_FOLDER):
        if archivo.endswith(".json"):
            perfiles.append(archivo.replace(".json", ""))
    return perfiles


# ------------------------------
# PRUEBA RÁPIDA (puedes borrar)
# ------------------------------
if __name__ == "__main__":
    print("=== Prueba del módulo data_manager ===")

    nombre = input("Ingresa tu nombre de jugador: ")

    # Cargar o crear perfil
    data = load_progress(nombre)
    print(f"\nPerfil cargado: {data['jugador']['nombre']}")
    print(data)

    # Simular progreso
    data["jugador"]["xp"] += 10
    data["jugador"]["nivel"] += 1
    save_progress(nombre, data)
    print("\nProgreso guardado correctamente.")

    print("\nPerfiles disponibles:", list_profiles())
