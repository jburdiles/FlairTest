
---

# **Simulación de Zombies en un Edificio**

¡Bienvenido a la **Simulación de Zombies en un Edificio**! Este es un juego de simulación en el que debes sobrevivir a una invasión de zombies en un edificio de varios pisos y habitaciones. A continuación, encontrarás una guía completa sobre cómo funciona el proyecto.

---

## **Índice**
1. [Introducción](#introducción)
2. [Supuestos del Juego](#supuestos-del-juego)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Clases](#clases)
   - [Room](#room)
   - [Floor](#floor)
   - [Building](#building)
   - [Simulation](#simulation)
5. [Funciones](#funciones)
   - [Funciones Principales](#funciones-principales)
   - [Funciones de Utilidad](#funciones-de-utilidad)
6. [Guardado y Carga del Juego](#guardado-y-carga-del-juego)
7. [Cómo Jugar](#cómo-jugar)

---

## **Introducción**
Este proyecto es una simulación interactiva en la que el jugador debe sobrevivir a una invasión de zombies en un edificio. El jugador puede bloquear habitaciones y limpiar habitaciones de zombies. El juego se desarrolla por rondas, y en cada ronda los zombies se mueven y aparecen nuevos en el primer piso. El fin es intentar llegar al mayor número de rondas.

---

## **Supuestos del Juego**
1. **Edificio**: El usuario decide la cantidad de pisos y habitaciones. Además se asume que todos los pisos tienen la misma cantidad de habitaciones.
2. **Jugador**: El jugador comienza en una posición definida por el usuario.
3. **Zombies**: Los zombies aparecen en el primer piso cada ronda y se mueven aleatoriamente por el edificio. Estos pueden trasladarse o expandirse de forma aleatoria.
4. **Acciones Especiales**: El jugador puede limpiar una habitación de zombies o bloquear una habitación para evitar que los zombies entren, sin embargo, los zombies pueden romper los bloqueos.
5. **Fin del Juego**: El juego termina si el jugador es alcanzado por los zombies.

---

## **Estructura del Proyecto**
El proyecto está organizado en varios archivos:

- **`main.py`**: Punto de entrada del programa. Solicita al usuario la configuración inicial del juego.
- **`building.py`**: Contiene las clases `Room`, `Floor` y `Building`.
- **`simulation.py`**: Contiene la clase `Simulation`, que maneja la lógica principal del juego.
- **`save_load.py`**: Contiene funciones para guardar y cargar el estado del juego.
- **`utils.py`**: Contiene funciones de utilidad, como la impresión de mensajes en colores.

---

## **Clases**

### **Room**
Representa una habitación en el edificio.

- **Atributos**:
  - `zombies`: Cantidad de zombies en la habitación.
  - `sensor`: Estado del sensor (`"Normal"` o `"Alerta"`).
  - `blocked`: Indica si la habitación está bloqueada.
  - `player_in_room`: Indica si el jugador está en la habitación.

- **Métodos**:
  - `__str__`: Devuelve una representación en cadena de la habitación.

---

### **Floor**
Representa un piso del edificio.

- **Atributos**:
  - `rooms`: Lista de habitaciones en el piso.

- **Métodos**:
  - `__str__`: Devuelve una representación en cadena del piso.

---

### **Building**
Representa el edificio completo.

- **Atributos**:
  - `floors`: Lista de pisos en el edificio.
  - `n_floors`: Número de pisos.
  - `n_rooms`: Número de habitaciones por piso.

- **Métodos**:
  - `__str__`: Devuelve una representación en cadena del edificio.

---

### **Simulation**
Maneja la lógica principal del juego.

- **Atributos**:
  - `building`: Instancia de `Building`.
  - `player_position`: Posición actual del jugador.
  - `round`: Número de ronda actual.
  - `end_state`: Indica si el juego ha terminado.
  - `directions`: Diccionario con las direcciones posibles para los zombies.
  - `special_actions`: Lista de acciones especiales disponibles (Acciones del jugador).

- **Métodos**:
  - `display_menu`: Muestra el menú principal y maneja las opciones del usuario.
  - `continue_simulation`: Avanza la simulación un turno.
  - `show_special_actions`: Muestra el menú de acciones especiales.
  - `show_map`: Muestra un mapa visual del edificio.
  - `check_end_game`: Verifica si el jugador ha sido alcanzado por los zombies.
  - `move_zombies`: Mueve los zombies aleatoriamente.
  - `add_zombies_to_first_floor`: Agrega nuevos zombies al primer piso (Simula que entran zombies al edificio cada ronda).
  - `update_sensor`: Actualiza el estado de los sensores (Normal si no hay zombies, Alerta si hay).
  - `clean_room`: Permite al jugador limpiar una habitación de zombies.
  - `block_room`: Permite al jugador bloquear una habitación.
  - `initialize_first_round`: Inicializa la primera ronda del juego.
  - `show_building_state`: Muestra el estado actual del edificio.
  - `load_saved_game`: Carga un juego guardado.

---

## **Funciones**

### **Funciones Principales**
- **`get_integer_input(prompt, min_value=1)`**: Solicita al usuario un valor entero y valida que sea mayor o igual a `min_value` (En este caso 1).
- **`get_player_position(n_floors, n_rooms)`**: Solicita al usuario la posición inicial del jugador.
- **`main()`**: Función principal que inicia la simulación.

### **Funciones de Utilidad**
- **`print_error(message)`**: Imprime un mensaje de error en rojo.
- **`print_success(message)`**: Imprime un mensaje de éxito en verde.

---

## **Guardado y Carga del Juego**
El juego permite guardar y cargar el estado actual. Las funciones `save_game` y `load_game` en `save_load.py` manejan esta funcionalidad.

- **`save_game(simulation, filename="save_game.json")`**: Guarda el estado del juego en un archivo JSON.
- **`load_game(filename="save_game.json")`**: Carga el estado del juego desde un archivo JSON.

---

## **Cómo Jugar**
1. Asegurese de tener instalado `colorama` (pip install colorama)
1. Ejecuta `main.py` para iniciar el juego.
2. Ingresa la cantidad de pisos y habitaciones por piso.
3. Selecciona la posición del jugador.
4. Usa el menú principal para realizar acciones especiales, guardar, cargar el juego u otro. (Seleccionando siempre el número de la izquierda de aquello que quieres realizar)
5. ¡Sobrevive!