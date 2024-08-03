import random

from palabras import leer_archivo_lst
from dibujo import dibujo_ahorcadito


def ahorcadito():
    while True:
        # Leer palabras desde el archivo
        archivo_palabras = 'listado-general-palabras.txt'
        palabras = leer_archivo_lst(archivo_palabras)

        # Mensaje de bienvenida
        print('=============================================================================')
        print('             ****** ¡Bienvenidos al Ahorcadito! ******\n')
        print('       -- Intenta adivinar entre más de 86000 palabras en español --')
        print('=============================================================================')

        # Inicialización de variables del juego
        vidas = 7
        palabra_adivinar = random.choice(palabras).upper()
        cantidad_letras = len(palabra_adivinar)
        cantidad_guiones = '-' * cantidad_letras
        palabras_ingresadas = []

        # Mostrar la longitud de la palabra a adivinar
        print(f'La palabra que tienes que adivinar tiene: "{cantidad_letras}" letras\n')

        # Bucle principal del juego
        while vidas > 0:
            print(f'\n                 {" ".join(cantidad_guiones)}\n')
            print('=============================================================================')
            letra_elegida = input('Elige una letra: ').upper()

            # Validar que solo se ingrese una letra y no sea un número
            if len(letra_elegida) != 1 or not letra_elegida.isalpha():
                if letra_elegida.isdigit():
                    print('Por favor, no ingreses números. Ingresa una sola letra válida.\n')
                else:
                    print('Por favor, ingresa una sola letra válida.\n')
                continue

            print(f'\nLa letra elegida es: "{letra_elegida}"\n')

            if letra_elegida not in palabras_ingresadas:
                palabras_ingresadas.append(letra_elegida)

                if letra_elegida in palabra_adivinar:
                    print('¡Excelente! Continúa para descifrar la palabra.\n')

                    # Reemplazar guiones con las letras acertadas
                    cantidad_guiones_lista = list(cantidad_guiones)
                    for i, e in enumerate(palabra_adivinar):
                        if e == letra_elegida:
                            cantidad_guiones_lista[i] = letra_elegida
                    cantidad_guiones = ''.join(cantidad_guiones_lista)

                    print(f'                 {" ".join(cantidad_guiones)}\n')

                    # Comprobar si se ha adivinado la palabra completa
                    if '-' not in cantidad_guiones:
                        print('¡¡¡Has ganado!!! ¡Felicitaciones! 😊')
                        break
                else:
                    vidas -= 1
                    print(f'La letra "{letra_elegida}" no se encuentra en la palabra.')
                    print(f'Ahora te quedan: {vidas} intentos para adivinar la palabra.\n')
                    print(f'{dibujo_ahorcadito[vidas]}')
            else:
                print(f'La letra "{letra_elegida}" ya fue elegida... Intenta con otra letra.')
                print(f'Sigues con: {vidas} intentos para adivinar la palabra.\n')

        # Mensaje de derrota si se quedan sin vidas
        if vidas == 0:
            print('=============================================================================')
            print('Perdiste... Ya no quedan más intentos. 😞')
            print(f'La palabra era: "{palabra_adivinar}"')
            print('=============================================================================')

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
    ahorcadito()
