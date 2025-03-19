"""
Este módulo contiene las clases que representan el edificio, pisos y habitaciones.
"""

class Room:
    """
    Representa una habitación en el edificio.

    Atributos:
        zombies (int): Cantidad de zombies en la habitación.
        sensor (str): Estado del sensor. Puede ser "Normal" o "Alerta".
        blocked (bool): Indica si la habitación está bloqueada.
        player_in_room (bool): Indica si el jugador está en la habitación.
    """

    def __init__(self):
        """
        Inicializa una habitación con valores predeterminados.
        - zombies: 0 (ningún zombie al inicio).
        - sensor: "Normal" (sin alerta al inicio).
        - blocked: False (habitación no bloqueada al inicio).
        - player_in_room: False (jugador no está en la habitación al inicio).
        """
        self.zombies = 0
        self.sensor = "Normal"
        self.blocked = False
        self.player_in_room = False

    def __str__(self):
        """
        Devuelve una representación en cadena de la habitación.

        Returns:
            str: Descripción de la habitación, incluyendo la cantidad de zombies,
                 el estado del sensor y si está bloqueada.
        """
        return f'Room with {self.zombies} zombies, sensor: {self.sensor}, blocked: {self.blocked}'


class Floor:
    """
    Representa un piso del edificio.

    Atributos:
        rooms (list): Lista de habitaciones en el piso.
    """

    def __init__(self, n_rooms):
        """
        Inicializa un piso con una cantidad específica de habitaciones.

        Parámetros:
            n_rooms (int): Número de habitaciones en el piso.
        """
        self.rooms = [Room() for _ in range(n_rooms)]

    def __str__(self):
        """
        Devuelve una representación en cadena del piso.

        Returns:
            str: Descripción del piso, incluyendo la cantidad de habitaciones.
        """
        return f'Floor with {len(self.rooms)} rooms'


class Building:
    """
    Representa el edificio completo.

    Atributos:
        floors (list): Lista de pisos en el edificio.
        n_floors (int): Número total de pisos.
        n_rooms (int): Número de habitaciones por piso.
    """

    def __init__(self, n_floors, n_rooms):
        """
        Inicializa un edificio con una cantidad específica de pisos y habitaciones por piso.

        Parámetros:
            n_floors (int): Número de pisos en el edificio.
            n_rooms (int): Número de habitaciones por piso.
        """
        self.floors = [Floor(n_rooms) for _ in range(n_floors)]
        self.n_floors = n_floors
        self.n_rooms = n_rooms

    def __str__(self):
        """
        Devuelve una representación en cadena del edificio.

        Returns:
            str: Descripción del edificio, incluyendo el número de pisos y habitaciones por piso.
        """
        return f'Building with {self.n_floors} floors and {self.n_rooms} rooms per floor'