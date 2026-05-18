# utilidades.py
# Módulo con funciones auxiliares para clasificar caracteres

def es_letra(caracter: str) -> bool:
    """
    Verifica si un caracter es una letra (a-z o A-Z) usando código ASCII
    
    Args:
        caracter: Un string de un solo caracter
        
    Returns:
        True si es letra, False en caso contrario
    """
    codigo = ord(caracter)
    # Mayúsculas: 65 a 90, minúsculas: 97 a 122
    return (65 <= codigo <= 90) or (97 <= codigo <= 122)


def es_numero(caracter: str) -> bool:
    """
    Verifica si un caracter es un número (0-9) usando código ASCII
    
    Args:
        caracter: Un string de un solo caracter
        
    Returns:
        True si es número, False en caso contrario
    """
    codigo = ord(caracter)
    # Números: 48 a 57
    return 48 <= codigo <= 57


def es_simbolo(caracter: str) -> bool:
    """
    Verifica si un caracter es un símbolo (no letra, no número, no espacio)
    
    Args:
        caracter: Un string de un solo caracter
        
    Returns:
        True si es símbolo, False en caso contrario
    """
    if caracter == ' ':
        return False
    return not (es_letra(caracter) or es_numero(caracter))


def invertir_string(texto: str) -> str:
    """
    Invierte un string sin usar slicing
    
    Args:
        texto: String a invertir
        
    Returns:
        String invertido
    """
    invertido = ""
    for i in range(len(texto) - 1, -1, -1):
        invertido = invertido + texto[i]
    return invertido


def contar_repetidos_consecutivos(texto: str) -> int:
    """
    Cuenta cuántas repeticiones consecutivas hay en un string
    
    Args:
        texto: String a analizar
        
    Returns:
        Cantidad de repeticiones consecutivas
    
    Ejemplo:
        "aaBB22!!" -> 4 repeticiones
    """
    if len(texto) <= 1:
        return 0
    
    repeticiones = 0
    i = 0
    
    while i < len(texto) - 1:
        if texto[i] == texto[i + 1]:
            repeticiones += 1
            # Saltar los caracteres repetidos
            while i < len(texto) - 1 and texto[i] == texto[i + 1]:
                i += 1
        else:
            i += 1
    
    return repeticiones


def ordenar_bubble_sort(lista: list, ascendente: bool) -> list:
    """
    Ordena una lista usando el algoritmo Bubble Sort
    
    Args:
        lista: Lista a ordenar
        ascendente: True para orden ascendente, False para descendente
        
    Returns:
        Nueva lista ordenada
    """
    n = len(lista)
    # Copiar la lista para no modificar la original
    lista_ordenada = lista[:]
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if ascendente:
                # Orden ascendente: menor primero
                if lista_ordenada[j] > lista_ordenada[j + 1]:
                    lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
            else:
                # Orden descendente: mayor primero
                if lista_ordenada[j] < lista_ordenada[j + 1]:
                    lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
    
    return lista_ordenada
   
def convertir_lista_posiciones_a_string(posiciones: list) -> str:
    """
    Convierte una lista de posiciones a un string separado por comas
    
    Args:
        posiciones: Lista de números enteros
        
    Returns:
        String con las posiciones separadas por comas
    """
    if len(posiciones) == 0:
        return ""
    
    resultado = ""
    for i in range(len(posiciones)):
        num = posiciones[i]
        
        if num == 0:
            num_str = "0"
        else:
            num_str = ""
            num_aux = num
            while num_aux > 0:
                num_str = chr(48 + (num_aux % 10)) + num_str
                num_aux = num_aux // 10
        
        if i > 0:
            resultado = resultado + "," + num_str
        else:
            resultado = resultado + num_str
    
    return resultado   
