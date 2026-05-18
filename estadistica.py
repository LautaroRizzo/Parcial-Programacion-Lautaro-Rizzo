# Módulo con funciones para generar estadísticas
from analisis import contar_caracteres
from utilidades import contar_repetidos_consecutivos

def calcular_porcentajes(contra: str) -> tuple:
    """
    Calcula los porcentajes de letras, números y símbolos
    
    args:
    contra: Contraseña a analizar
        
    returns:
    tupla con (porcentaje_letras, porcentaje_numeros, porcentaje_simbolos)
    """
    largo = len(contra)
    letras, numeros, simbolos, espacios = contar_caracteres(contra)

    if largo == 0:
        return (0.0, 0.0, 0.0)
    
    porcentaje_letras = (letras * 100) / largo
    porcentaje_numeros = (numeros * 100) / largo
    porcentaje_simbolos = (simbolos * 100) / largo

def generar_report(contra: str) -> None:
    """
    Genera y muestra un reporte estadístico completo de la contraseña
    
    Args:
        contra: Contraseña a analizar
    """ 
    largo = len(contra)
    letras, numeros, simbolos, espacios = contar_caracteres(contra)
    porcentaje_letras, porcentaje_numeros, porcentaje_simbolos = calcular_porcentajes(contra)
    repetido = contar_repetidos_consecutivos(contra)

    print("REPORTE ESTASDISTICO 📢⚠️ ")
    
    print(f"Longitud total: {largo} caracteres")

    print("Cantidades: ")

    print(f"  - Letras: {letras}")

    print(f"  - Números: {numeros}")

    print(f"  - Símbolos: {simbolos}")

    print(f"  - Espacios: {espacios}")

    print("Porcentajes:")

    print(f"  - Letras: {porcentaje_numeros} %")

    print(f"  - Números: {porcentaje_numeros} %")

    print(f"  - Símbolos: {porcentaje_simbolos} %")

    print(f"Caracteres repetidos consecutivos: {repetido}")