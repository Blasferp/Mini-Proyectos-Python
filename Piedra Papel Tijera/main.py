import random

def piedra_papel_tijera():
    opciones = {
        1: 'Piedra',
        2: 'Papel',
        3: 'Tijera'
    }

    while True:
        puntaje_usuario = 0
        puntaje_pc = 0

        while puntaje_usuario < 3 and puntaje_pc < 3:
            # Eleccion aleatoria de los valores, luego de crearlos en una lista
            eleccion_pc = random.choice(list(opciones.values()))

            while True:
                eleccion_usuario = input('1- Piedra 🧊\n2- Papel 📃\n3- Tijera ✂\n¿Cuál es tu elección para jugar? (1, 2, 3): ')

                # Validar que la entrada sea un número
                if not eleccion_usuario.isdigit():
                    print('Debe ingresar un número.')
                    continue

                # Convertir la entrada a un entero
                eleccion_usuario = int(eleccion_usuario)

                # Verificar que el número esté dentro del rango permitido
                if eleccion_usuario < 1 or eleccion_usuario > 3:
                    print('Número fuera de las opciones. Debe ser 1, 2 o 3.')
                    continue

                break

            print(f'Tu elección: {opciones[eleccion_usuario]}')
            print(f'PC elección: {eleccion_pc}')

            # Eleccion del usuario en str
            opcion_usuario = opciones[eleccion_usuario]

            if eleccion_pc == opcion_usuario:
                print(f'Hay un empate de {eleccion_pc}, sigue intentando.')
                print(f'El marcador continua Pc: {puntaje_pc} vs Usuario: {puntaje_usuario}')

            elif (eleccion_pc == 'Tijera' and opcion_usuario == 'Papel') or (eleccion_pc == 'Papel' and opcion_usuario == 'Piedra') or (eleccion_pc == 'Piedra' and opcion_usuario == 'Tijera'):
                print('Gana Pc')
                puntaje_pc += 1  # Aumenta el puntaje de la PC
            else:
                print('Gana Usuario')
                puntaje_usuario += 1  # Aumenta el puntaje del usuario

            # Mostrar marcador actualizado
            print(f'Marcador actual: Pc: {puntaje_pc} vs Usuario: {puntaje_usuario}')

        if puntaje_pc == 3:
            print('Perdiste el Partido... Pc alcanzo los 3 puntos')
        elif puntaje_usuario == 3:
            print('Ganaste el Partido... alcanzaste los 3 puntos')

        # Preguntar si desea jugar de nuevo
        while True:
            jugar_otra_vez = input('¿Deseas jugar otra vez? (s/n): ').upper()
            if jugar_otra_vez == 'S':
                break
            elif jugar_otra_vez == 'N':
                print('Gracias por jugar. ¡Hasta la próxima!')
                return
            else:
                print('Error: Debes elegir entre "S" (sí) o "N" (no).')

if __name__ == '__main__':
    piedra_papel_tijera()
