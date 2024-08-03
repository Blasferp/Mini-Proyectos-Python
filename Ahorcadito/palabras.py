import unicodedata


def quitar_acentos(texto):
    """
    Elimina los acentos de un texto.

    Parámetros:
    texto (str): La cadena de texto de la cual se desean eliminar los acentos.

    Retorna:
    str: La cadena de texto sin acentos.
    """
    # Normalizar el texto a la forma de descomposición canónica (NFD)
    texto_normalizado = unicodedata.normalize('NFD', texto)
    # Eliminar los caracteres acentuados (diacríticos)
    texto_sin_acentos = ''.join(c for c in texto_normalizado if not unicodedata.combining(c))
    return texto_sin_acentos

def leer_archivo_lst(archivo):
    """
    Lee un archivo .lst, elimina los acentos de las palabras y devuelve una lista de palabras.

    Parámetros:
    archivo (str): La ruta al archivo .lst que se desea leer.

    Retorna:
    list: Una lista de cadenas de texto sin acentos, donde cada cadena es una línea del archivo después de haber
          sido limpiada de espacios en blanco.
    """
    with open(archivo, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    palabras = []

    for line in lines:
        # Eliminar espacios en blanco al principio y al final de la línea
        line = line.strip()
        # Eliminar acentos
        line = quitar_acentos(line)
        # Agregar la línea limpia a la lista de palabras
        palabras.append(line)
        
    return palabras


