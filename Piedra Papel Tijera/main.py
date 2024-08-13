""" 
Este módulo implementa un juego de piedra, papel o tijera
donde el usuario juega contra la computadora.
"""
import random

def piedra_papel_tijera():
    """
    Juega al juego de Piedra, Papel o Tijera contra la computadora.
    
    El juego continúa hasta que uno de los jugadores (usuario o computadora) alcance 3 puntos.
    Después de cada partida, se pregunta al usuario si desea jugar nuevamente.
    """

    # Mensaje de bienvenida
    print('=============================================================================')
    print('                   ****** ¡Bienvenidos a Piedra, Papel o Tijera! ******\n')
    print('                -- Compite contra la computadora y alcanza 3 puntos --')
    print('=============================================================================\n')
    # Opciones del juego
    opciones = {
        1: 'Piedra',
        2: 'Papel',
        3: 'Tijera'
    }

    while True:
        # Inicialización de los puntajes
        puntaje_usuario = 0
        puntaje_pc = 0

        # Ciclo del juego principal hasta que uno de los jugadores alcance 3 puntos
        while puntaje_usuario < 3 and puntaje_pc < 3:
            # Elección aleatoria de la PC
            eleccion_pc = random.choice(list(opciones.values()))

            while True:
                # Entrada del usuario
                print('Opciones:\n')
                print('1 - Piedra\n')
                print('2 - Papel\n')
                print('3 - Tijera\n')
                eleccion_usuario = input('¿Cuál es tu elección para jugar? (1, 2, 3): ')
                # Validar que la entrada sea un número
                if not eleccion_usuario.isdigit():
                    print('Debe ingresar un número.\n')
                    continue

                # Convertir la entrada a un entero
                eleccion_usuario = int(eleccion_usuario)

                # Verificar que el número esté dentro del rango permitido
                if eleccion_usuario < 1 or eleccion_usuario > 3:
                    print('Número fuera de las opciones. Debe ser 1, 2 o 3.\n')
                    continue

                break

            print(f'Tu elección: {opciones[eleccion_usuario]}')
            print(f'PC elección: {eleccion_pc}\n')

            # Elección del usuario en str
            opcion_usuario = opciones[eleccion_usuario]

            # Comparar las elecciones para determinar el ganador
            if eleccion_pc == opcion_usuario:
                print(f'Hay un empate de {eleccion_pc}, sigue intentando.\n')
                print(f'El marcador continúa Pc: {puntaje_pc} vs Usuario: {puntaje_usuario}\n')

            elif (
                (eleccion_pc == 'Tijera' and opcion_usuario == 'Papel') or
                (eleccion_pc == 'Papel' and opcion_usuario == 'Piedra') or
                (eleccion_pc == 'Piedra' and opcion_usuario == 'Tijera')
            ):
                print('Gana Pc\n')
                puntaje_pc += 1  # Aumenta el puntaje de la PC
            else:
                print('Gana Usuario\n')
                puntaje_usuario += 1  # Aumenta el puntaje del usuario

            # Mostrar marcador actualizado
            print(f'Marcador actual: Pc: {puntaje_pc} vs Usuario: {puntaje_usuario}\n')
            print('=============================================================================\n')

        # Mostrar mensaje de resultado final
        if puntaje_pc == 3:
            print('Perdiste el Partido... Pc alcanzó los 3 puntos')
        elif puntaje_usuario == 3:
            print('Ganaste el Partido... alcanzaste los 3 puntos')

        # Preguntar si desea jugar de nuevo
        while True:
            # Solicita la respuesta del usuario y la convierte a mayúsculas
            jugar_otra_vez = input('¿Deseas jugar otra vez? (s/n): ').upper()
            # Si el usuario desea jugar de nuevo, se sale del bucle
            if jugar_otra_vez == 'S':
                break
            # Si el usuario no desea jugar más, se imprime un mensaje y termina la función
            if jugar_otra_vez == 'N':
                print('Gracias por jugar. ¡Hasta la próxima!')
                return
            # Si la entrada es inválida, se muestra un mensaje de error y se repite la pregunta
            else:
                print('Error: Debes elegir entre "S" (sí) o "N" (no).\n')

if __name__ == '__main__':
    piedra_papel_tijera()
