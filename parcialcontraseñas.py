# Sistema de Procesamiento de Contraseñas
# Estudiante: [Tu nombre]
# Fecha: [Fecha actual]

def es_letra(caracter: str) -> bool:
    """Verifica si un caracter es una letra (a-z o A-Z) usando ASCII"""
    codigo = ord(caracter)
    # Mayúsculas: 65 a 90, minúsculas: 97 a 122
    return (65 <= codigo <= 90) or (97 <= codigo <= 122)


def es_numero(caracter: str) -> bool:
    """Verifica si un caracter es un número (0-9) usando ASCII"""
    codigo = ord(caracter)
    return 48 <= codigo <= 57


def es_simbolo(caracter: str) -> bool:
    """Verifica si es símbolo (no letra, no número, no espacio)"""
    if caracter == ' ':
        return False
    return not (es_letra(caracter) or es_numero(caracter))


def validar_contraseña(contra: str) -> bool:
    """
    Valida que la contraseña cumpla con:
    - no vacía
    - al menos 8 caracteres
    - no comienza con espacio
    - al menos una letra
    """
    # Validar no vacía
    if len(contra) == 0:
        print("Error: La contraseña no puede estar vacía")
        return False
    
    #validar 8 caracteres
    if len(contra) < 8:
        print("Error, Su contraseña debe tener al manos 8 caracteres")
        return False
    

    #validar que no comienze con espacio
    if contra[0] == ' ':
        print("Error: La contraseña no debe comenzar con un espacio")
        return False
    
    tiene_letra = False
    for i in range(len(contra)):
        if es_letra(contra[i]):
            tiene_letra = True
            break

        if not tiene_letra:
            print("Error: Su contraseña debe contener al menos una letra")
            return False           
        return True
    
def nivel_seguridad(contra: str) -> str:
    """
    Determina si la contraseña es Débil, Media o Fuerte
    Recorre manualmente la cadena para contar letras, números y símbolos
    """
    largo = len(contra)
    tiene_letras = False
    tiene_numeros = False
    tiene_simbolos = False

    #recorrer manualmente la contraseña
    for i in range(largo):
        if es_letra(contra[i]):
            tiene_letras = True
        elif es_numero(contra[i]):
            tiene_numeros = True    
        elif es_simbolo(contra[i]):
            tiene_simbolos = True

    #evaluando nivel
    if 8 <=largo <= 9 and tiene_letras and not tiene_numeros and not tiene_simbolos:
        return "Contraseña Debil"
    elif tiene_letras and tiene_numeros and not tiene_simbolos:
        return "Contraseña Media" 
    elif tiene_letras and tiene_numeros and tiene_simbolos:
        return "Contraseña Fuerta como patada de canguro"
    else:
        return "No tiene los criterios necesitados"