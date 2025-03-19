from colorama import Fore, Style
from save_load import save_game, load_game
from utils import COLORS, print_error, print_success
import random

class Simulation:
    """
    Clase principal que maneja la simulación del juego.

    Atributos:
        building (Building): El edificio donde ocurre la simulación.
        player_position (list): Posición actual del jugador [piso, habitación].
        round (int): Número de ronda actual.
        end_state (bool): Indica si el juego ha terminado.
        directions (dict): Direcciones posibles para moverse.
        special_actions (list): Acciones especiales disponibles.
    """

    def __init__(self, building, player_position):
        """
        Inicializa la simulación con un edificio y la posición del jugador.

        Parámetros:
            building (Building): El edificio donde ocurre la simulación.
            player_position (list): Posición inicial del jugador [piso, habitación].
        """
        self.building = building
        self.player_position = player_position
        self.round = 0
        self.end_state = False
        self.directions = {
            "Izquierda": (0, -1),
            "Derecha": (0, 1),
            "Arriba": (-1, 0),
            "Abajo": (1, 0)
        }
        self.special_actions = [["Limpiar habitacion", False], ["Bloquear habitacion", False]]
        self.initialize_first_round()
        self.display_menu()

    def display_menu(self):
        """
        Muestra el menú principal y maneja las opciones del usuario.
        """
        while not self.end_state:
            print("""\n\t\t=== Menú Principal ===
            1. Mostrar mapa
            2. Mostrar estado del edificio
            3. Avanzar simulación
            4. Acciones especiales
            5. Guardar juego
            6. Cargar juego
            0. Salir\n""")
            
            try:
                n = int(input("Seleccione una opción: "))
            except ValueError:
                print_error("Opción inválida. Ingrese un número.")
                continue

            if n == 1:
                self.show_map()
            elif n == 2:
                self.show_building_state()
            elif n == 3:
                self.continue_simulation()
            elif n == 4:
                self.show_special_actions()
            elif n == 5:
                save_game(self)
            elif n == 6:
                self.load_saved_game()
            elif n == 0:
                print("Saliendo del juego...")
                save_game(self)
                break
            else:
                print_error("Opción inválida")

    def continue_simulation(self):
        """
        Avanza la simulación un turno: mueve zombies, actualiza sensores y verifica el fin del juego.
        """
        for action in self.special_actions:
            action[1] = False  # Reiniciar acciones especiales
        self.move_zombies()
        self.add_zombies_to_first_floor()
        self.update_sensor()
        self.check_end_game()
        self.round += 1
        print(f"\n--- Fin de la ronda {self.round} ---\n")

    def show_special_actions(self):
        """
        Muestra el menú de acciones especiales y maneja la selección del usuario.
        """
        while True:
            print("Seleccione 0 para volver")
            for i, action in enumerate(self.special_actions):
                status = "(Usada)" if action[1] else ""
                print(f"{i + 1}. {action[0]} {status}")

            try:
                n = int(input("Seleccione una acción: "))
            except ValueError:
                print_error("Opción inválida. Ingrese un número.")
                continue

            if n == 0:
                return
            elif n == 1:
                self.clean_room()
            elif n == 2:
                self.block_room()
            else:
                print_error("Opción inválida")

    def show_map(self):
        """
        Muestra un mapa visual del edificio, indicando la posición del jugador, habitaciones bloqueadas y zombies.
        """
        border = "┌" + "───┬" * (self.building.n_rooms - 1) + "───┐"
        separator = "├" + "───┼" * (self.building.n_rooms - 1) + "───┤"
        end_border = "└" + "───┴" * (self.building.n_rooms - 1) + "───┘"

        print(border)
        for floor in self.building.floors:
            rooms = []
            for room in floor.rooms:
                if room.player_in_room:
                    rooms.append(f'{COLORS["P"]} P {Style.RESET_ALL}')
                elif room.blocked:
                    rooms.append(f'{COLORS["B"]} B {Style.RESET_ALL}')
                else:
                    rooms.append(f'{COLORS["zombies"]}{room.zombies:^3}{Style.RESET_ALL}')
            print("│" + "│".join(rooms) + "│")
            if floor != self.building.floors[-1]:
                print(separator)
        print(end_border)

    def check_end_game(self):
        """
        Verifica si el jugador ha sido alcanzado por los zombies.
        """
        player_room = self.building.floors[self.player_position[0]].rooms[self.player_position[1]]
        if player_room.zombies > 0:
            print(Fore.RED + "¡Has sido alcanzado por los zombies!" + Style.RESET_ALL)
            print(Fore.RED + "¡Juego terminado!" + Style.RESET_ALL)
            self.end_state = True

    def move_zombies(self):
        """
        Mueve los zombies aleatoriamente por el edificio.
        """
        for f in range(self.building.n_floors):
            floor_idx = -f - 1
            for r in range(self.building.n_rooms):
                if self.building.floors[floor_idx].rooms[r].zombies > 0:
                    direction = random.choice(list(self.directions.values()))
                    new_floor = floor_idx + direction[0]
                    new_room = r + direction[1]

                    if 0 <= new_room < self.building.n_rooms and -self.building.n_floors <= new_floor <= -1:
                        if not self.building.floors[new_floor].rooms[new_room].blocked:
                            zombies_to_move = random.randint(1, self.building.floors[floor_idx].rooms[r].zombies)
                            self.building.floors[floor_idx].rooms[r].zombies -= zombies_to_move
                            self.building.floors[new_floor].rooms[new_room].zombies += zombies_to_move
                            print(f"{zombies_to_move} zombies se movieron de piso {-floor_idx}, hab {r + 1} a piso {-new_floor}, hab {new_room + 1}")
                        else:
                            print(f"Los zombies destrozaron el bloqueo habitación en piso {-new_floor}, hab {new_room + 1}")
                            self.building.floors[new_floor].rooms[new_room].blocked = False
    
    def add_zombies_to_first_floor(self):
        """
        Agrega nuevos zombies al primer piso (índice -1).
        """
        first_floor = self.building.floors[-1]  # Primer piso (índice -1)
        for r, room in enumerate(first_floor.rooms):
            if not room.blocked:  # No agregar zombies a habitaciones bloqueadas
                new_zombies = random.randint(0, 5)  # Número aleatorio de nuevos zombies
                room.zombies += new_zombies
                if new_zombies > 0:
                    print(f"{new_zombies} nuevos zombies aparecieron en el piso 1, hab {r + 1}")

    def update_sensor(self):
        """
        Actualiza el estado de los sensores en todas las habitaciones.
        """
        for floor in self.building.floors:
            for room in floor.rooms:
                room.sensor = "Alerta" if room.zombies > 0 else "Normal"

    def clean_room(self):
        """
        Permite al jugador limpiar una habitación de zombies.
        """
        try:
            h = int(input("Ingrese el número de la habitación que desea limpiar: "))
            p = int(input("Ingrese el número del piso: "))
            if 1 <= p <= self.building.n_floors and 1 <= h <= self.building.n_rooms:
                room = self.building.floors[-p].rooms[h - 1]
                room.zombies = 0
                self.special_actions[0][1] = True
                print_success(f"Habitación {h} del piso {p} limpiada")
            else:
                print_error("Habitación o piso inválidos")
        except ValueError:
            print_error("Opción inválida. Ingrese un número.")

    def block_room(self):
        """
        Permite al jugador bloquear una habitación.
        """
        try:
            h = int(input("Ingrese el número de la habitación que desea bloquear: "))
            p = int(input("Ingrese el número del piso: "))
            if 1 <= p <= self.building.n_floors and 1 <= h <= self.building.n_rooms:
                room = self.building.floors[-p].rooms[h - 1]
                if room.zombies > 0:
                    print_error("No puedes bloquear una habitación con zombies")
                else:
                    room.blocked = True
                    self.special_actions[1][1] = True
                    print_success(f"Habitación {h} del piso {p} bloqueada")
            else:
                print_error("Habitación o piso inválidos")
        except ValueError:
            print_error("Opción inválida. Ingrese un número.")

    def initialize_first_round(self):
        """
        Inicializa la primera ronda del juego, colocando zombies y al jugador.
        """
        first_floor = self.building.floors[-1]
        for room in first_floor.rooms:
            room.zombies = random.randint(0, 5)
            room.sensor = "Alerta" if room.zombies > 0 else "Normal"
        player_room = self.building.floors[self.player_position[0]].rooms[self.player_position[1]]
        player_room.player_in_room = True

    def show_building_state(self):
        """
        Muestra el estado actual del edificio, incluyendo zombies, sensores y habitaciones bloqueadas.
        """
        for f, floor in enumerate(self.building.floors):
            for r, room in enumerate(floor.rooms):
                print(f"Piso: {f + 1}, Habitación: {r + 1}, Zombies: {room.zombies}, Sensor: {room.sensor}, Bloqueada: {room.blocked}")

    def load_saved_game(self):
        """
        Carga un juego guardado desde un archivo.
        """
        loaded_data = load_game()
        if loaded_data:
            self.building, self.player_position, self.round, self.special_actions = loaded_data
            print_success("Juego cargado correctamente.")