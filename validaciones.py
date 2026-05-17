# validaciones.py
# Módulo con funciones para validar contraseñas

from utilidades import es_letra

def validar_contraseña(contra: str) -> bool:
    """
    Valida que la contraseña cumpla con los requisitos:
     No vacía
     Al menos 8 caracteres
     No comienza con espacio
     Al menos una letra
    
    Args:
        contra: Contraseña a validar
        
    Returns:
        True si cumple todas las validaciones, False en caso contrario
    """
    #validar cuando esté vacia
    if len(contra) == 0:
        print("Error: La contraseña no debe estar vacia")
        return False
    
    
    #validacion de al menos 8 caracteres
    if len(contra)< 8:
        print("Error: La contraseña debe tener al menos 8 caracteres")
        return False
    
    #validacion para que no comienze con espacio
    if contra[0] == ' ':
        print("Error: La contraseña no puede comenzar con un espacio")
        return False
    
    #validacion de al menos una letra
    tiene_letra = False
    for i in range(len(contra)):
        if es_letra(contra[i]):
            tiene_letra = True
            break

    if not tiene_letra:
        print("Error: la contraseña dene tener al menos una letra")
        return False            
    
    return True

def validar_caracter_unico(caracter: str)-> bool:
    """
    valida que el usuario haya ingresado un solo caracter
    
    args:
        caracter: String ingresado por el usuario
        
    returns:
        True si es un solo caracter, False en caso contrario
    """

    if len(caracter) != 1:
        print("Error: Tiene que ingresar con un solo caracter")
    return False
    return True

def validar_opcion_menu(opcion: str, min_valor: int, max_valor: int) -> bool:
    """
    Valida que la opción del menú sea un número dentro del rango

    Args:
        opcion: String ingresado por el usuario
        min_valor: Valor mínimo permitido
        max_valor: Valor máximo permitido

    Returns:
        True si es válida, False en caso contrario
    """
    for c in opcion:
        codigo = ord(c)
        if codigo < 48 or codigo > 57:
            return False

    numero = 0
    for c in opcion:
        numero = numero * 10 + (ord(c) - 48)

    return min_valor <= numero <= max_valor