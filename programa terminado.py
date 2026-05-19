# Programa principal del Sistema de Procesamiento de Contraseñas

from validaciones import validar_contraseña
from analisis import nivel_seguridad, contar_caracteres, buscar_caracter, es_palindromo, ordenar_contraseña
from estadistica import generar_report
from utilidades import invertir_string


# MENÚS

def mostrar_menu() -> None:
    """Muestra el menú principal del sistema"""
    print("=" * 50)
    print("   🔐 SISTEMA DE PROCESAMIENTO DE CONTRASEÑAS")
    print("=" * 50)
    print("")
    print("   1. 📝 Ingresar contraseña")
    print("   2. 🔒 Validar nivel de seguridad")
    print("   3. 🔢 Contar tipos de caracteres")
    print("   4. 🔍 Buscar carácter específico")
    print("   5. 🔄 Mostrar contraseña invertida")
    print("   6. 📊 Generar reporte estadístico")
    print("   7. 🔁 Verificar si es palíndromo")
    print("   8. 📋 Ordenar caracteres")
    print("   9. 🚪 Salir")
    print("")
    print("=" * 50)


def mostrar_menu_ordenamiento() -> None:
    """Muestra el submenú para ordenar la contraseña"""
    print("   ┌────────────────────────────────────────────┐")
    print("   │  📋 ORDENAR CARACTERES                     │")
    print("   ├────────────────────────────────────────────┤")
    print("   │  ⬆️  1.  Orden ascendente (ASCII)          │")
    print("   │  ⬇️  2.  Orden descendente (ASCII)         │")
    print("   └────────────────────────────────────────────┘")


# FUNCIONES AUXILIARES

def mostrar_resultado_busqueda(cantidad: int, posiciones: list, caracter: str) -> None:
    """Muestra los resultados de la búsqueda de un carácter"""
    print("--- RESULTADO DE BÚSQUEDA ---")
    print(f"El carácter '{caracter}' aparece {cantidad} vez/veces")
    
    if cantidad > 0:
        texto = ""
        for i in range(len(posiciones)):
            if i > 0:
                texto = texto + ", "
            texto = texto + str(posiciones[i])
        print(f"Posiciones: {texto}")


def preguntar_continuar() -> bool:
    """Pregunta al usuario si quiere continuar o salir"""
    print("-" * 40)
    print("   ¿Qué desea hacer?")
    print("   1. 🔄 Continuar (volver al menú)")
    print("   2. 🚪 Salir del programa")
    print("-" * 40)
    
    opcion_valida = False
    while not opcion_valida:
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            return True
        elif opcion == "2":
            return False
        else:
            print("Opción inválida. Ingrese 1 para continuar o 2 para salir.")


def validar_que_haya_contraseña(contrasenia: str) -> bool:
    """Verifica que exista una contraseña ingresada"""
    if contrasenia == "":
        print("⚠️ Primero debe ingresar una contraseña (opción 1)")
        return False
    return True


# OPCIONES DEL MENÚ

def opcion_ingresar(contrasenia: str) -> str:
    """Opción 1: Ingresar contraseña"""
    nueva = input("Ingrese la contraseña: ")
    if validar_contraseña(nueva):
        print("✓ Contraseña guardada correctamente")
        return nueva
    else:
        print("✗ La contraseña no cumple las validaciones")
        return contrasenia


def opcion_validar_seguridad(contrasenia: str) -> None:
    """Opción 2: Validar nivel de seguridad"""
    if not validar_que_haya_contraseña(contrasenia):
        return
    nivel = nivel_seguridad(contrasenia)
    print(f"🔒 NIVEL DE SEGURIDAD: {nivel}")


def opcion_contar_tipos(contrasenia: str) -> None:
    """Opción 3: Contar tipos de caracteres"""
    if not validar_que_haya_contraseña(contrasenia):
        return
    letras, numeros, simbolos, espacios = contar_caracteres(contrasenia)
    print("🔢 CANTIDAD DE CARACTERES")
    print("-" * 30)
    print(f"   Letras:   {letras}")
    print(f"   Números:  {numeros}")
    print(f"   Símbolos: {simbolos}")
    print(f"   Espacios: {espacios}")
    print("-" * 30)


def opcion_buscar_caracter(contrasenia: str) -> None:
    """Opción 4: Buscar carácter específico"""
    if not validar_que_haya_contraseña(contrasenia):
        return
    
    caracter_valido = False
    while not caracter_valido:
        caracter = input("Ingrese el carácter a buscar: ")
        if len(caracter) == 1:
            cantidad, posiciones = buscar_caracter(contrasenia, caracter)
            mostrar_resultado_busqueda(cantidad, posiciones, caracter)
            caracter_valido = True
        else:
            print("⚠️ Debe ingresar UN SOLO caracter. Intente nuevamente.")


def opcion_mostrar_invertida(contrasenia: str) -> None:
    """Opción 5: Mostrar contraseña invertida"""
    if not validar_que_haya_contraseña(contrasenia):
        return
    invertida = invertir_string(contrasenia)
    print("🔄 CONTRASEÑA INVERTIDA")
    print("-" * 30)
    print(f"   Original: {contrasenia}")
    print(f"   Invertida: {invertida}")
    print("-" * 30)


def opcion_generar_reporte(contrasenia: str) -> None:
    """Opción 6: Generar reporte estadístico"""
    if not validar_que_haya_contraseña(contrasenia):
        return
    generar_report(contrasenia)


def opcion_verificar_palindromo(contrasenia: str) -> None:
    """Opción 7: Verificar si es palíndromo"""
    if not validar_que_haya_contraseña(contrasenia):
        return
    
    if es_palindromo(contrasenia):
        print("🔁 ✓ La contraseña ES palíndromo")
    else:
        print("🔁 ✗ La contraseña NO es palíndromo")


def opcion_ordenar_caracteres(contrasenia: str) -> None:
    """Opción 8: Ordenar caracteres"""
    if not validar_que_haya_contraseña(contrasenia):
        return
    
    opcion_valida = False
    while not opcion_valida:
        mostrar_menu_ordenamiento()
        subopcion = input("Elija una opción: ")
        
        if subopcion == "1":
            resultado = ordenar_contraseña(contrasenia, subopcion)
            print("📋 ORDEN ASCENDENTE")
            print("-" * 30)
            print(f"   Original: {contrasenia}")
            print(f"   Ordenada: {resultado}")
            print("-" * 30)
            opcion_valida = True
        elif subopcion == "2":
            resultado = ordenar_contraseña(contrasenia, subopcion)
            print("📋 ORDEN DESCENDENTE")
            print("-" * 30)
            print(f"   Original: {contrasenia}")
            print(f"   Ordenada: {resultado}")
            print("-" * 30)
            opcion_valida = True
        else:
            print("❌ Opción inválida. Elija 1 o 2. Intente nuevamente.")


# PROGRAMA PRINCIPAL


def main() -> None:
    """Función principal del programa"""
    contrasenia = ""

    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            contrasenia = opcion_ingresar(contrasenia)

        elif opcion == "2":
            opcion_validar_seguridad(contrasenia)

        elif opcion == "3":
            opcion_contar_tipos(contrasenia)

        elif opcion == "4":
            opcion_buscar_caracter(contrasenia)

        elif opcion == "5":
            opcion_mostrar_invertida(contrasenia)

        elif opcion == "6":
            opcion_generar_reporte(contrasenia)

        elif opcion == "7":
            opcion_verificar_palindromo(contrasenia)

        elif opcion == "8":
            opcion_ordenar_caracteres(contrasenia)

        elif opcion == "9":
            print("👋 ¡Gracias por usar el sistema!")
            print("   Hasta luego!")
            break

        else:
            print("❌ Opción inválida. Ingrese un número del 1 al 9")
            continue

        if not preguntar_continuar():
            print("👋 ¡Gracias por usar el sistema!")
            print("   Hasta luego!")
            break


if __name__ == "__main__":
    main()