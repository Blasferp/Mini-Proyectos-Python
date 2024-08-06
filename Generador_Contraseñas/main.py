import random
import string

def generador_contraseña(longitud, mayusculas, digitos, especiales):
    """
    Genera una contraseña aleatoria con los requisitos especificados.

    Parámetros:
    longitud (int): La longitud total deseada para la contraseña.
    mayusculas (int): La cantidad de caracteres en mayúsculas que debe tener la contraseña.
    digitos (int): La cantidad de dígitos numéricos que debe tener la contraseña.
    especiales (int): La cantidad de caracteres especiales que debe tener la contraseña.

    Retorna:
    str: La contraseña generada que cumple con los requisitos dados.

    Excepciones:
    ValueError: Si la suma de mayúsculas, dígitos y caracteres especiales supera la longitud total menos 1,
                o si la longitud total es menor que la suma de estos caracteres más al menos una minúscula.
    """
    
    # Verificar que la suma de mayúsculas, dígitos y caracteres especiales no exceda la longitud menos 1,
    # para permitir al menos un carácter en minúsculas.
    if mayusculas + digitos + especiales > (longitud - 1):
        raise ValueError("La suma de mayúsculas, dígitos y caracteres especiales no puede ser mayor que la longitud total menos 1.")
    
    # Definir los conjuntos de caracteres disponibles
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    caracteres_digitos = string.digits
    caracteres_especiales = string.punctuation
    
    # Crear una lista de caracteres para la contraseña
    contraseña = (
        random.choices(letras_mayusculas, k=mayusculas) +  # Seleccionar caracteres en mayúsculas
        random.choices(caracteres_digitos, k=digitos) +  # Seleccionar dígitos numéricos
        random.choices(caracteres_especiales, k=especiales) +  # Seleccionar caracteres especiales
        random.choices(letras_minusculas, k=(longitud - (mayusculas + digitos + especiales)))  # Rellenar con minúsculas restantes
    )
    
    # Mezclar la lista de caracteres para asegurar que la contraseña sea aleatoria
    random.shuffle(contraseña)
    
    # Convertir la lista de caracteres en una cadena de texto
    contraseña = ''.join(contraseña)
    
    return contraseña

def main():
    """
    Función principal para ejecutar el programa que genera una contraseña basada en
    los criterios ingresados por el usuario. Solicita al usuario la longitud total
    de la contraseña y las cantidades de letras mayúsculas, dígitos y caracteres 
    especiales, asegurándose de que los valores sean válidos.
    """
    # Mensaje de bienvenida
    print('=============================================================================')
    print('             ****** ¡Bienvenidos al Generador de Contraseñas! ******\n')
    print('          -- Elige la longitud, mayúsculas, dígitos y caracteres especiales. --')
    print('=============================================================================\n')
    
    try:
        # Solicitar longitud total
        while True:
            try:
                longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8): "))
                if longitud < 8:
                    print("La longitud de la contraseña debe ser al menos 8 caracteres.")
                else:
                    print(f"La longitud elegida es de {longitud} caracteres.")
                    print('=============================================================================\n')
                    break
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido para la longitud.")
        
        # Solicitar cantidad de letras mayúsculas
        while True:
            try:
                mayusculas = int(input("Ingrese la cantidad de letras mayúsculas que tendrá la contraseña: "))
                if mayusculas < 1:
                    print("La contraseña debe tener al menos una letra mayúscula.")
                elif mayusculas >= longitud:
                    print(f"La cantidad de mayúsculas ({mayusculas}) no puede ser mayor o igual a la longitud total ({longitud}).")
                else:
                    print(f"{mayusculas} letras mayúsculas establecidas.")
                    print(f"Quedan {longitud - mayusculas} caracteres por asignar.")
                    print('=============================================================================\n')
                    break
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido para la cantidad de mayúsculas.")
                
        # Solicitar cantidad de dígitos
        while True:
            try:
                digitos = int(input("Ingrese la cantidad de dígitos que tendrá la contraseña: "))
                if digitos < 0:
                    print("La cantidad de dígitos debe ser igual o mayor a 0.")
                elif (mayusculas + digitos) >= longitud:
                    print(f"La cantidad combinada de mayúsculas y dígitos ({mayusculas + digitos}) no puede ser mayor o igual a la longitud total ({longitud -1}).")
                else:
                    print(f"{digitos} dígitos establecidos.")
                    print(f"Quedan {longitud - (mayusculas + digitos)} caracteres por asignar.")
                    print('=============================================================================\n')
                    break
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido para la cantidad de dígitos.")
                
        # Solicitar cantidad de caracteres especiales
        while True:
            try:
                especiales = int(input("Ingrese la cantidad de caracteres especiales que tendrá la contraseña: "))
                if especiales < 1:
                    print("La contraseña debe tener al menos un carácter especial.")
                elif (mayusculas + digitos + especiales) >= longitud:
                    print(f"La cantidad combinada de mayúsculas, dígitos y caracteres especiales ({mayusculas + digitos + especiales}) no puede ser mayor o igual a la longitud total ({longitud -1}).")
                else:
                    print(f"{especiales} caracteres especiales establecidos.")
                    print(f"Quedan {longitud - (mayusculas + digitos + especiales)} caracteres por asignar.")
                    print(f"Los caracteres restantes ({longitud - (mayusculas + digitos + especiales)}) serán minúsculas.")
                    print('=============================================================================\n')
                    break
            except ValueError:
                print("Error: Por favor, ingrese un número entero válido para la cantidad de caracteres especiales.")
        
        # Generar y mostrar la contraseña
        contraseña_generada = generador_contraseña(longitud, mayusculas, digitos, especiales)
        print(f"Contraseña generada: {contraseña_generada}")
     
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
        