# ==========================================
# guardar_datos.py
# ------------------------------------------
# Guarda y carga el progreso del jugador
# en un archivo llamado "progreso.json".
# ==========================================

import json
import os


ARCHIVO ="progreso.json"


def guardar_progreso(jugador):
    """Guardar los datos del jugador en formato JSON."""

    with open(ARCHIVO, 'w', encoding="utf-8") as archivo:
        json.dump(jugador, archivo, indent=4)
    print("Progreso guardado correctamente.")


def cargar_progreso():
    """Cargar los datos del jugador si el archivo existe.
        Si no, retorna None para crear uno nuevo.
    """

    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r', encoding="utf-8") as archivo:
            return json.load(archivo)
    else:
        return None