"""Genera palabras en Pig Latin (jeringoso en inglés)."""


def main():
    """
    Modifica las palabras: si comienzan con vocal, agrega 'way';
    si comienzan con consonante, mueve la primera letra al final y
    agrega 'ay'.
    """
    print('Bienvenido a Pig Latin')
    # Definimos una lista con las vocales.
    vocales = ['a', 'e', 'i', 'o', 'u']
    while True:
        try:
            # Se crea variable ingresada por el usuario en minúsculas.
            palabra = input('Elige una palabra para transformar: ').lower()
            # Verificar si la entrada está vacía.
            if not palabra:
                raise ValueError('La entrada no puede estar vacía')
            # Verificar si todos los caracteres en la entrada son letras.
            if not palabra.isalpha():
                raise ValueError('La entrada debe contener solo letras')
            break
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")
    if palabra[0] in vocales:
        palabra_pig_latin = palabra + 'way'
    else:
        palabra_pig_latin = palabra[1:] + palabra[0] + 'ay'
    print(f'La palabra "{palabra}" en Pig Latin es: {palabra_pig_latin}')


if __name__ == "__main__":
    main()
