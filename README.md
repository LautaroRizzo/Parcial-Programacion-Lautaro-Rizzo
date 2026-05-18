👨‍💻 Autor Lautaro Rizzo
Estudiante de Tecnicatura en Programación
Materia: Programación 1

# 🔐 Sistema de Procesamiento de Contraseñas

## 📌 Descripción del Proyecto

Este proyecto es un programa desarrollado en Python que permite analizar y validar contraseñas ingresadas por usuarios. Fue realizado como parte de un examen parcial de la materia **Programación 1**, aplicando los conceptos fundamentales de programación estructurada.

El sistema ofrece múltiples funcionalidades, como la validación de contraseñas según criterios de seguridad, conteo de tipos de caracteres, búsqueda de caracteres específicos, inversión de cadenas, generación de reportes estadísticos, verificación de palíndromos y ordenamiento de caracteres utilizando algoritmos implementados manualmente.

---

## 🎯 Objetivo

El objetivo principal del programa es brindar una herramienta interactiva que permita al usuario:

- Ingresar una contraseña cumpliendo con validaciones específicas.
- Analizar el nivel de seguridad de la contraseña (Débil, Media o Fuerte).
- Obtener estadísticas detalladas sobre la composición de la contraseña.
- Realizar operaciones avanzadas como búsqueda, inversión, ordenamiento y verificación de palíndromos.

---

## 🧱 Estructura del Proyecto

El proyecto está organizado en múltiples módulos para garantizar una correcta modularización y separación de responsabilidades.

---

## ⚙️ Funcionalidades

### 1. Ingresar contraseña

Permite al usuario ingresar una contraseña. Se aplican las siguientes validaciones obligatorias:

- La contraseña no puede estar vacía.
- Debe tener al menos 8 caracteres.
- No puede comenzar con espacios.
- Debe contener al menos una letra.

### 2. Validar nivel de seguridad

Analiza la contraseña y la clasifica según los siguientes criterios:

| Nivel | Criterios |
|-------|-----------|
| 🔴 Débil | Entre 8 y 9 caracteres, solo letras |
| 🟡 Media | Contiene letras y números |
| 🟢 Fuerte | Contiene letras, números y símbolos, y tiene al menos 12 caracteres |

### 3. Contar tipos de caracteres

Muestra la cantidad de:

- Letras
- Números
- Símbolos
- Espacios

### 4. Buscar carácter específico

Solicita un carácter al usuario y muestra:

- Cuántas veces aparece en la contraseña.
- Las posiciones exactas donde se encuentra.

### 5. Mostrar contraseña invertida

Muestra la contraseña original y su versión invertida (al revés).

### 6. Generar reporte estadístico

Muestra un reporte completo con:

- Longitud total de la contraseña.
- Porcentaje de letras, números y símbolos.
- Cantidad de caracteres repetidos consecutivos (ejemplo: "aaBB22!!" tiene 4 repeticiones).

### 7. Verificar si es palíndromo

Determina si la contraseña se lee igual de izquierda a derecha que de derecha a izquierda (ejemplo: "radar").

### 8. Ordenar caracteres de la contraseña

Permite ordenar los caracteres de la contraseña según su valor en la tabla ASCII.

El usuario puede elegir entre:

- Orden ascendente (de menor a mayor código ASCII).
- Orden descendente (de mayor a menor código ASCII).

### 9. Salir

Finaliza la ejecución del programa.

---

## 🛠️ Tecnologías y Conceptos Utilizados

- **Lenguaje:** Python 3
- **Estructuras de control:** Condicionales (`if-elif-else`), bucles (`for`, `while`)
- **Funciones:** Uso de funciones con docstrings y type hints
- **Modularización:** División del código en múltiples módulos
- **Manejo de cadenas:** Recorrido manual de caracteres sin usar métodos avanzados
- **Algoritmos de ordenamiento:** Implementación manual de **Bubble Sort**
- **Código ASCII:** Clasificación de caracteres mediante valores ASCII

---

## 🚫 Restricciones Cumplidas

El programa respeta todas las restricciones indicadas en la consigna:

- ❌ No se utilizan métodos de cadenas (`.upper()`, `.isalpha()`, etc.).
- ❌ No se utilizan métodos de listas avanzados (`.sort()`, `.reverse()`).
- ❌ No se utiliza el operador `in`.
- ❌ No se utiliza slicing (`[::-1]`, `[1:3]`).
- ❌ No se utilizan funciones avanzadas como `sorted()`.
- ✅ Solo se utilizan: `len()`, `input()`, `print()`, `int()`, `float()`, `str()`, `range()`, `ord()`.

---

## ▶️ Cómo Ejecutar el Programa

1. **Clonar o descargar** el repositorio en tu computadora.
2. Asegurarse de tener todos los archivos en la misma carpeta:
   - `programa terminado.py`
   - `validaciones.py`
   - `analisis.py`
   - `estadistica.py`
   - `utilidades.py`
3. Abrir una terminal en la ubicación del proyecto.

📋 Ejemplo de Uso

   🔐 SISTEMA DE PROCESAMIENTO DE CONTRASEÑAS


   1. 📝 Ingresar contraseña
   2. 🔒 Validar nivel de seguridad
   3. 🔢 Contar tipos de caracteres
   4. 🔍 Buscar carácter específico
   5. 🔄 Mostrar contraseña invertida
   6. 📊 Generar reporte estadístico
   7. 🔁 Verificar si es palíndromo
   8. 📋 Ordenar caracteres
   9. 🚪 Salir

Ingrese su opción: 1
Ingrese la contraseña: Aaaaaaaa12@@@@@

✓ Contraseña guardada correctamente

   ¿Qué desea hacer?
   1. 🔄 Continuar (volver al menú)
   2. 🚪 Salir del programa

Ingrese su opción: 1

Ingrese su opción: 2

🔒 NIVEL DE SEGURIDAD: Contraseña Fuerte 🟢
