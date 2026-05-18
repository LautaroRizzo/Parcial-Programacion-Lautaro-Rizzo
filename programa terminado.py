# Programa principal del sistema de procesamiento de contraseñas

from validaciones import validar_contraseña
from analisis import nivel_seguridad, contar_caracteres, buscar_caracter, es_palindromo, ordenar_contraseña
from estadistica import generar_report
from utilidades import invertir_string


def mostrar_menu() -> None:
    """Muestra el menú principal del sistema"""
    print("\n" + "="*50)
    print("   🔐 SISTEMA DE PROCESAMIENTO DE CONTRASEÑAS")
    print("="*50)
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
    print("="*50)


def mostrar_menu_ordenamiento() -> None:
    """Muestra el submenú para ordenar la contraseña"""
    print("\n   ┌────────────────────────────────────────────┐")
    print("   │  📋 ORDENAR CARACTERES                     │")
    print("   ├────────────────────────────────────────────┤")
    print("   │  ⬆️  1.  Orden ascendente (ASCII)          │")
    print("   │  ⬇️  2.  Orden descendente (ASCII)         │")
    print("   └────────────────────────────────────────────┘")


def mostrar_resultado_busqueda(cantidad: int, posiciones: list, caracter: str) -> None:
    """Muestra los resultados de la búsqueda de un carácter"""
    print("\n--- RESULTADO DE BÚSQUEDA ---")
    print(f"El carácter '{caracter}' aparece {cantidad} vez/veces")
    
    if cantidad > 0:
        texto = ""
        for i in range(len(posiciones)):
            if i > 0:
                texto = texto + ", "
            texto = texto + str(posiciones[i])
        print(f"Posiciones: {texto}")


def preguntar_continuar() -> bool:
    """
    Pregunta al usuario si quiere continuar o salir
    
    Returns:
        True si quiere continuar, False si quiere salir
    """
    print("\n" + "-"*40)
    print("   ¿Qué desea hacer?")
    print("   1. 🔄 Continuar (volver al menú)")
    print("   2. 🚪 Salir del programa")
    print("-"*40)
    
    while True:
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            return True
        elif opcion == "2":
            return False
        else:
            print("Opción inválida. Ingrese 1 para continuar o 2 para salir.")


def main() -> None:
    """Función principal del programa"""
    contrasenia = ""
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")
        
        # Opción 1: Ingresar contraseña
        if opcion == "1":
            nueva = input("Ingrese la contraseña: ")
            if validar_contraseña(nueva):
                contrasenia = nueva
                print("\n✓ Contraseña guardada correctamente")
            else:
                print("\n✗ La contraseña no cumple las validaciones")
        
        # Opción 2: Validar nivel de seguridad
        elif opcion == "2":
            if contrasenia == "":
                print("\n⚠️ Primero debe ingresar una contraseña (opción 1)")
            else:
                nivel = nivel_seguridad(contrasenia)
                print(f"\n🔒 NIVEL DE SEGURIDAD: {nivel}")
        
        # Opción 3: Contar tipos de caracteres
        elif opcion == "3":
            if contrasenia == "":
                print("\n⚠️ Primero debe ingresar una contraseña (opción 1)")
            else:
                letras, numeros, simbolos, espacios = contar_caracteres(contrasenia)
                print("\n🔢 CANTIDAD DE CARACTERES")
                print("─" * 30)
                print(f"   Letras:   {letras}")
                print(f"   Números:  {numeros}")
                print(f"   Símbolos: {simbolos}")
                print(f"   Espacios: {espacios}")
                print("─" * 30)
        
        # Opción 4: Buscar carácter específico
        elif opcion == "4":
            if contrasenia == "":
                print("\n⚠️ Primero debe ingresar una contraseña (opción 1)")
            else:
                caracter = input("Ingrese el carácter a buscar: ")
                if len(caracter) == 1:
                    cantidad, posiciones = buscar_caracter(contrasenia, caracter)
                    mostrar_resultado_busqueda(cantidad, posiciones, caracter)
                else:
                    print("\n❌ Debe ingresar UN SOLO caracter")
        
        # Opción 5: Mostrar contraseña invertida
        elif opcion == "5":
            if contrasenia == "":
                print("\n⚠️ Primero debe ingresar una contraseña (opción 1)")
            else:
                invertida = invertir_string(contrasenia)
                print("\n🔄 CONTRASEÑA INVERTIDA")
                print("─" * 30)
                print(f"   Original: {contrasenia}")
                print(f"   Invertida: {invertida}")
                print("─" * 30)
        
        # Opción 6: Generar reporte estadístico
        elif opcion == "6":
            if contrasenia == "":
                print("\n⚠️ Primero debe ingresar una contraseña (opción 1)")
            else:
                generar_report(contrasenia)
        
        # Opción 7: Verificar palíndromo
        elif opcion == "7":
            if contrasenia == "":
                print("\n⚠️ Primero debe ingresar una contraseña (opción 1)")
            else:
                if es_palindromo(contrasenia):
                    print("\n🔁 ✓ La contraseña ES palíndromo")
                else:
                    print("\n🔁 ✗ La contraseña NO es palíndromo")
        
        # Opción 8: Ordenar caracteres
        elif opcion == "8":
            if contrasenia == "":
                print("\n⚠️ Primero debe ingresar una contraseña (opción 1)")
            else:
                mostrar_menu_ordenamiento()
                subopcion = input("Elija una opción: ")
                
                if subopcion == "1" or subopcion == "2":
                    resultado = ordenar_contraseña(contrasenia, subopcion)
                    tipo = "ascendente" if subopcion == "1" else "descendente"
                    print(f"\n📋 ORDEN {tipo.upper()}")
                    print("─" * 30)
                    print(f"   Original: {contrasenia}")
                    print(f"   Ordenada: {resultado}")
                    print("─" * 30)
                else:
                    print("\n❌ Opción inválida. Elija 1 o 2")
        
        # Opción 9: Salir
        elif opcion == "9":
            print("\n👋 ¡Gracias por usar el sistema!")
            print("   Hasta luego!")
            break
        
        else:
            print("\n❌ Opción inválida. Ingrese un número del 1 al 9")
            continue
        
        # Después de cada operación (excepto salir), preguntar si continuar
        if opcion != "9":
            if not preguntar_continuar():
                print("\n👋 ¡Gracias por usar el sistema!")
                print("   Hasta luego!")
                break


if __name__ == "__main__":
    main()