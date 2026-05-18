# Módulo con funciones para generar estadísticas
from analisis import contar_caracteres
from utilidades import contar_repetidos_consecutivos

def calcular_porcentajes(contra: str) -> tuple:
    """
    Calcula los porcentajes de letras, números y símbolos

    Args:
        contra: Contraseña a analizar

    Returns:
        Tupla con (porcentaje_letras, porcentaje_numeros, porcentaje_simbolos)
    """
    largo = len(contra)
    letras, numeros, simbolos, espacios = contar_caracteres(contra)

    if largo == 0:
        return (0.0, 0.0, 0.0)

    porcentaje_letras = (letras * 100) / largo
    porcentaje_numeros = (numeros * 100) / largo
    porcentaje_simbolos = (simbolos * 100) / largo

    return (porcentaje_letras, porcentaje_numeros, porcentaje_simbolos)


def generar_report(contra: str) -> None:
    """
    Genera y muestra un reporte estadístico completo de la contraseña
    
    Args:
        contra: Contraseña a analizar
    """ 
    largo = len(contra)
    letras, numeros, simbolos, espacios = contar_caracteres(contra)
    porc_letras, porc_numeros, porc_simbolos = calcular_porcentajes(contra)
    repetidos = contar_repetidos_consecutivos(contra)
    
    print("\n" + "="*50)
    print("📊 REPORTE ESTADÍSTICO")
    print("="*50)
    print(f"Longitud total: {largo} caracteres")
    print("\n📌 Cantidades:")
    print(f"   • Letras: {letras}")
    print(f"   • Números: {numeros}")
    print(f"   • Símbolos: {simbolos}")
    print(f"   • Espacios: {espacios}")
    print("\n📈 Porcentajes:")
    print(f"   • Letras: {porc_letras:.1f}%")
    print(f"   • Números: {porc_numeros:.1f}%")
    print(f"   • Símbolos: {porc_simbolos:.1f}%")
    print(f"\n🔄 Caracteres repetidos consecutivos: {repetidos}")
    print("="*50)