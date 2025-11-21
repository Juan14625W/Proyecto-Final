"""
main.py
Punto de entrada del Diario Gamer de Hábitos.
"""

from data_manager import load_progress, save_progress, list_profiles
import logic

print("👉 LOGIC.PY CARGADO DESDE:", logic.__file__)

def mostrar_menu():
    print("\n==============================")
    print("   🎮 DIARIO GAMER DE HÁBITOS 🎮")
    print("==============================")
    print("1. Ver estado del jugador")
    print("2. Ver hábitos")
    print("3. Agregar hábito")
    print("4. Completar hábito")
    print("5. Reiniciar hábitos del día")
    print("6. Guardar progreso")
    print("7. Registrar historial del día")
    print("8. Ver el máximo XP del mes")
    print("9. Cambiar de jugador")
    print("10. Salir")
    print("==============================")


def seleccionar_jugador():
    print("\n=== Selección de jugador ===")
    
    perfiles = list_profiles()
    if perfiles:
        print("Perfiles existentes:")
        for p in perfiles:
            print(" -", p)
    else:
        print("Aún no hay perfiles guardados.")
    
    nombre = input("\nIngresa tu nombre de jugador: ")
    data = load_progress(nombre)
    print(f"\n✨ Bienvenido, {data['jugador']['nombre']}! ✨")
    return nombre, data


def main():
    nombre, data = seleccionar_jugador()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        # ------------------- OPCIÓN 1 -------------------
        if opcion == "1":
            logic.mostrar_estado(data)

        # ------------------- OPCIÓN 2 -------------------
        elif opcion == "2":
            logic.mostrar_habitos(data)

        # ------------------- OPCIÓN 3 -------------------
        elif opcion == "3":
            nuevo = input("Ingresa el nombre del nuevo hábito: ")
            data = logic.agregar_habito(data, nuevo)
            print("Hábito agregado con éxito.")

        # ------------------- OPCIÓN 4 -------------------
        elif opcion == "4":
            logic.mostrar_habitos(data)
            if len(data["habitos"]) > 0:
                try:
                    numero = int(input("Número del hábito a completar: "))
                    data = logic.completar_habito(data, numero)
                    logic.registrar_historial(data)
                except ValueError:
                    print("Debes ingresar un número válido.")

        # ------------------- OPCIÓN 5 -------------------
        elif opcion == "5":
            data = logic.reiniciar_habitos(data)
            logic.registrar_historial(data)

        # ------------------- OPCIÓN 6 -------------------
        elif opcion == "6":
            save_progress(nombre, data)
            logic.registrar_historial(data)
            print("Progreso guardado correctamente.")

        # ------------------- OPCIÓN 7 -------------------
        elif opcion == "7":
            data = logic.registrar_historial(data)
            save_progress(nombre, data)
            print("Historial del día registrado.")

        # ------------------- OPCIÓN 8 -------------------
        elif opcion == "8":
            maximo = logic.maximo_xp_mes(data)
            if maximo is None:
                print("No hay datos registrados este mes.")
            else:
                print(f"📅 Máximo XP en este mes: {maximo}")

        # ------------------- OPCIÓN 9 -------------------
        elif opcion == "9":
            save_progress(nombre, data)
            nombre, data = seleccionar_jugador()

        # ------------------- OPCIÓN 10 -------------------
        elif opcion == "10":
            save_progress(nombre, data)
            print("\n Gracias por jugar. ¡Sigue subiendo de nivel en la vida real!")
            break

        # ------------------- OPCIÓN INVÁLIDA -------------------
        else:
            print("Opción no válida. Intenta de nuevo.")


# ------------------- EJECUCIÓN PRINCIPAL -------------------
if __name__ == "__main__":
    main()