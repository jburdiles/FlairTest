import json
from building import Building, Floor, Room
from colorama import Fore, Style

def save_game(simulation, filename="save_game.json"):
    game_state = {
        "player_position": simulation.player_position,
        "building": {
            "n_floors": simulation.building.n_floors,
            "n_rooms": simulation.building.n_rooms,
            "floors": [
                {
                    "rooms": [
                        {"zombies": room.zombies, "blocked": room.blocked, "player_in_room": room.player_in_room}
                        for room in floor.rooms
                    ]
                }
                for floor in simulation.building.floors
            ]
        },
        "round": simulation.round,
        "special_actions": simulation.special_actions
    }
    with open(filename, "w") as file:
        json.dump(game_state, file, indent=4)
    print(Fore.GREEN + "Juego guardado correctamente." + Style.RESET_ALL)

def load_game(filename="save_game.json"):
    try:
        with open(filename, "r") as file:
            game_state = json.load(file)
        
        building = Building(game_state["building"]["n_floors"], game_state["building"]["n_rooms"])
        for f, floor_state in enumerate(game_state["building"]["floors"]):
            for r, room_state in enumerate(floor_state["rooms"]):
                room = building.floors[f].rooms[r]
                room.zombies = room_state["zombies"]
                room.blocked = room_state["blocked"]
                room.player_in_room = room_state["player_in_room"]
        
        return building, game_state["player_position"], game_state["round"], game_state["special_actions"]
    except FileNotFoundError:
        print("No se encontró un archivo de guardado.")
        return None
    except Exception as e:
        print(f"Error al cargar el juego: {e}")
        return None