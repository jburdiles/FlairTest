from building import Building
from simulation import Simulation

def get_integer_input(prompt, min_value=1):
    """
    Solicita al usuario un valor entero y valida que sea mayor o igual a min_value.
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"El valor debe ser mayor o igual a {min_value}. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

def get_player_position(n_floors, n_rooms):
    """
    Solicita al usuario la posición inicial del jugador.
    """
    while True:
        try:
            floor = int(input(f"Ingresa el piso inicial del jugador (1 a {n_floors}): "))
            room = int(input(f"Ingresa la habitación inicial del jugador (1 a {n_rooms}): "))
            if 1 <= floor <= n_floors and 1 <= room <= n_rooms:
                return [-floor, room - 1]  # Convertir a índices negativos y base 0
            else:
                print(f"Posición inválida. El piso debe estar entre 1 y {n_floors}, y la habitación entre 1 y {n_rooms}.")
        except ValueError:
            print("Entrada inválida. Ingresa números enteros.")

def main():
    """
    Función principal que inicia la simulación.
    """
    print("¡Bienvenido a la Simulación de Zombies!")

    # Solicitar la cantidad de pisos y habitaciones
    n_floors = get_integer_input("Ingresa la cantidad de pisos del edificio: ")
    n_rooms = get_integer_input("Ingresa la cantidad de habitaciones por piso: ")

    # Solicitar la posición inicial del jugador
    print("\nConfiguración de la posición inicial del jugador:")
    player_position = get_player_position(n_floors, n_rooms)

    # Crear el edificio
    building = Building(n_floors, n_rooms)

    # Iniciar la simulación
    simulation = Simulation(building, player_position)

if __name__ == "__main__":
    main()