# analisis, modulo con funcion de analizar las contraseñas
from utilidades import es_letra, es_numero, es_simbolo, invertir_string

def nivel_seguridad(contra: str)-> str:
  """
    Determina el nivel de seguridad de la contraseña
    
    criterios:
     Débil: entre 8-9 caracteres, solo letras
     Media: letras y números
     Fuerte: letras, números, símbolos y al menos 12 caracteres
    
    args:
    contra: Contraseña a analizar
        
    returns:
    String con el nivel de seguridad
    """
  largo = len (contra)
  tiene_letra = False
  tiene_numero = False
  tiene_simnbolo = False

  #recorrer la contraseña
  for i in range (largo):
    if es_letra(contra[i]):
      tiene_letra = True

    elif es_numero (contra[i]):
      tiene_numero = True

    elif es_simbolo(contra[i]):
      tiene_simnbolo = True 
    #evaluacion de nivel
    if 8 <= largo <=9 and tiene_letra and not tiene_numero and not tiene_simnbolo:
        return "Contraseña Debil 🔴"
    
    elif tiene_letra and tiene_numero and not tiene_simnbolo:
      return "Contraseña Media 🟨" 
    
    elif tiene_simnbolo and tiene_numero and tiene_simnbolo:
      return "Contraseña Fuerte 💚"
    


def contar_caracteres (contra: str) -> tuple:
    """
    Cuenta letras, números, símbolos y espacios en la contraseña
    
    Args:
        contra: Contraseña a analizar
        
    Returns:
        Tupla con (letras, numeros, simbolos, espacios)
    """
    letras = 0
    numeros = 0
    simbolos = 0
    espacios = 0

    for i in range(len(contra)):
        if contra[i] == ' ':
            espacios += 1

        elif es_letra(contra[i]):
            letras +=1

        elif es_numero(contra[i]):
           numeros +=1

        elif es_simbolo(contra[i]):
           simbolos +=1

    return (letras, numeros, simbolos, espacios)



def buscar_caracter(contra: str, caracter: str) -> tuple:
    """
    Busca un caracter específico en la contraseña
    
    Args:
        contra: Contraseña donde buscar
        caracter: Caracter a buscar
        
    Returns:
        Tupla con (cantidad, lista_de_posiciones)
    """
    cantidad = 0
    
    for i in range(len(contra)):
        if contra[i] == caracter:
            cantidad += 1
    
    posiciones = [0] * cantidad
    indice = 0
    
    for i in range(len(contra)):
        if contra[i] == caracter:
            posiciones[indice] = i
            indice += 1
    
    return (cantidad, posiciones)

def ordenar_contraseña(contra: str, opcion: str) -> str:
    """
    Ordena los caracteres de la contraseña usando Bubble Sort
    
    Args:
        contra: Contraseña a ordenar
        opcion: "1" para ascendente, "2" para descendente
        
    Returns:
        String con los caracteres ordenados
    """
    from utilidades import ordenar_bubble_sort
    
    lista_caracteres = [0] * len(contra)
    for i in range(len(contra)):
        lista_caracteres[i] = contra[i]
    
    if opcion == "1":
        lista_ordenada = ordenar_bubble_sort(lista_caracteres, True)
    else:
        lista_ordenada = ordenar_bubble_sort(lista_caracteres, False)
    
    resultado = ""
    for i in range(len(lista_ordenada)):
        resultado = resultado + lista_ordenada[i]
    
    return resultado

def es_palindromo(contra: str)-> bool:
  """
    Verifica si la contraseña es un palíndromo
    
    Args:
        contra: Contraseña a verificar
        
    Returns:
        True si es palíndromo, False en caso contrario
    """
  invertida = invertir_string
  return contra == invertida 