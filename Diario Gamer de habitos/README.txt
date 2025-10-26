Proyecto: Diario Gamer de Hábitos
Autor: (Tu nombre aquí)
Lenguaje: Python 3
Nivel: Principiante
Descripción: Un programa tipo “juego de hábitos”, donde el usuario puede ganar experiencia (XP), subir de nivel y mejorar su personaje al cumplir tareas diarias.

🎯 OBJETIVO DEL PROGRAMA

El objetivo es motivar al usuario a cumplir hábitos diarios, pero de forma divertida, como si fuera un videojuego.
Cada tarea completada otorga puntos de experiencia (XP), y al acumularlos el jugador sube de nivel.
Los datos del progreso se guardan automáticamente en un archivo para continuar otro día.

🧩 ESTRUCTURA DEL PROYECTO
DiarioGamer/
│
├── main.py               ← Archivo principal (menú del juego)
├── jugador.py            ← Maneja la información del jugador
├── habitos.py            ← Contiene las misiones y XP
├── guardar_datos.py      ← Guarda y carga el progreso en JSON
└── README.txt             ← Este archivo de documentación

⚙️ FUNCIONAMIENTO GENERAL
🔹 1. main.py

Es el centro del programa.
Aquí se muestra el menú principal, se reciben las opciones del usuario y se conectan las funciones de los demás archivos.

Opciones del menú:

Ver misiones del día

Marcar misiones completadas

Ver progreso del jugador

Guardar y salir del programa

🔹 2. jugador.py

Aquí se crean y administran los datos del jugador.
Contiene funciones para:

Crear un nuevo jugador

Ver su perfil (nombre, nivel, energía, XP)

Subir de nivel cuando alcanza 100 XP

Ejemplo de datos guardados:

{
  "nombre": "Juan",
  "nivel": 2,
  "xp": 45,
  "energia": 90
}

🔹 3. habitos.py

Define las misiones del día y cuántos puntos de XP da cada una.

Ejemplo:

1. Estudiar 30 minutos (+20 XP)
2. Hacer ejercicio (+25 XP)
3. Leer un capítulo (+15 XP)


El jugador puede marcar las que completó, y el programa le suma la experiencia ganada automáticamente.

🔹 4. guardar_datos.py

Guarda los datos del jugador en un archivo JSON llamado progreso.json.
Esto permite continuar el juego otro día sin perder los avances.

Funciones:

guardar_progreso(jugador) → guarda los datos.

cargar_progreso() → carga los datos si el archivo existe.

🕹️ CÓMO USAR EL PROGRAMA

Abre una terminal o consola.

Entra a la carpeta del proyecto:

cd DiarioGamer


Ejecuta el programa principal:

python main.py


Sigue las instrucciones en pantalla:

Elige tus misiones del día.

Marca las que cumpliste.

Gana XP y sube de nivel.

Guarda tu progreso antes de salir.

💾 ARCHIVO DE PROGRESO

Después de jugar, se genera un archivo llamado progreso.json.
Ejemplo del contenido:

{
    "nombre": "Juan",
    "nivel": 3,
    "xp": 60,
    "energia": 80
}


Este archivo se actualiza automáticamente cada vez que eliges “Guardar y salir”.

🚀 FUTURAS MEJORAS (ideas)

Si más adelante quieres hacerlo más avanzado, puedes:

Agregar más misiones dinámicas o aleatorias.

Incluir recompensas visuales o sonidos.

Hacer una versión con interfaz gráfica usando tkinter.

Permitir varios jugadores o perfiles distintos.

Mostrar una barra de progreso o “vida”.

💬 NOTAS FINALES

Este proyecto fue diseñado con código sencillo para que cualquier persona que esté empezando en Python lo entienda fácilmente.
Usa conceptos básicos de:

Condicionales (if, else)

Listas y diccionarios

Funciones

Módulos (import)

Archivos JSON