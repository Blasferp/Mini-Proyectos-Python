def cambiar_turno(jugador):
    """Cambia el turno del jugador actual."""
    return 'O' if jugador == 'X' else 'X'

def verificar_victoria(tablero, jugador):
    """
    Verifica si el jugador ha ganado.

    Args:
        tablero (list): Lista que representa el tablero.
        jugador (str): Símbolo del jugador ('X' o 'O').

    Returns:
        bool: True si el jugador ha ganado, False en caso contrario.
    """
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columnas
        [0, 4, 8], [2, 4, 6]              # diagonales
    ]
    for combinacion in combinaciones_ganadoras:
        if all(tablero[i] == jugador for i in combinacion):
            return True
    return False

def verificar_empate(tablero):
    """
    Verifica si el juego ha terminado en empate.

    Args:
        tablero (list): Lista que representa el tablero.

    Returns:
        bool: True si el juego ha terminado en empate, False en caso contrario.
    """
    return '-' not in tablero

def mostrar_tablero(tablero):
    """
    Muestra el estado actual del tablero.

    Args:
        tablero (list): Lista que representa el tablero.
    """
    print(f'{tablero[0]} | {tablero[1]} | {tablero[2]}')
    print('---------')
    print(f'{tablero[3]} | {tablero[4]} | {tablero[5]}')
    print('---------')
    print(f'{tablero[6]} | {tablero[7]} | {tablero[8]}')

def jugar(tablero, jugador):
    """
    Gestiona el flujo del juego de Tic-Tac-Toe.

    Args:
        tablero (list): Lista que representa el tablero.
        jugador (str): Símbolo del jugador actual ('X' o 'O').
    """
    while True:
        mostrar_tablero(tablero)
        
        # Solicitar movimiento del jugador
        while True:
            try:
                seleccion_casilla = int(input(f'Turno del jugador {jugador}. Elige la casilla que desees (1-9): '))
                if seleccion_casilla < 1 or seleccion_casilla > 9:
                    print("Número fuera de rango. Intenta de nuevo.")
                elif tablero[seleccion_casilla - 1] != '-':
                    print("Casilla ya ocupada. Intenta de nuevo.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")
        
        # Actualizar el tablero
        tablero[seleccion_casilla - 1] = jugador
        
        # Verificar si hay un ganador
        if verificar_victoria(tablero, jugador):
            mostrar_tablero(tablero)
            print(f"¡El jugador {jugador} ha ganado!")
            break
        
        # Verificar si hay empate
        if verificar_empate(tablero):
            mostrar_tablero(tablero)
            print("¡Es un empate!")
            break
        
        # Cambiar al otro jugador
        jugador = cambiar_turno(jugador)

def main():
    """Función principal para inicializar y comenzar el juego."""
    tablero = ['-' for _ in range(9)]
    jugador = 'X'  # El juego comienza con el jugador 'X'
    jugar(tablero, jugador)

if __name__ == '__main__':
    main()
