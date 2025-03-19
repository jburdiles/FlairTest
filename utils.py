from colorama import Fore, Style

# Colores para el mapa
COLORS = {
    'P': Fore.GREEN,  # Jugador
    'B': Fore.RED,    # Habitación bloqueada
    'zombies': Fore.YELLOW  # Zombis
}

# Otras constantes y funciones útiles
def print_error(message):
    print(f"{Fore.RED}Error: {message}{Style.RESET_ALL}")

def print_success(message):
    print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")