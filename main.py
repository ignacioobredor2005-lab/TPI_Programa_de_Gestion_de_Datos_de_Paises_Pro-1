import csv
import os

# Constante que define el nombre del archivo CSV con el que trabajará la aplicación
RUTA_CSV = "paises.csv"

# FUNCIONES DEL MANEJO DEL ARCHIVO
def cargar_paises(ruta):
    paises = []
    # Verifica si el archivo existe, si no, avisa y retorna lista vacía
    if not os.path.exists(ruta):
        print(f"Archivo {ruta} inexistente. Creando archivo vacio...")
        return paises
    try:
        # Abre el archivo en modo lectura con codificación utf-8
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    # Convierte cada fila del CSV en un diccionario con tipos de datos correctos
                    pais = {
                        "Nombre": fila['Nombre'].strip(),
                        "Población": int(fila['Población'].strip()),
                        "Superficie": int(fila['Superficie'].strip()),
                        "Continente": fila['Continente'].strip()
                    }
                    paises.append(pais)
                except ValueError:
                    # Controla errores de conversión numérica en el CSV
                    print("Error de formato.")
    except Exception as e:
        print(f"Error al leer archivo CSV: {e}")
    return paises

def guardar_paises(ruta, paises):
    try:
        with open(ruta, mode="w", encoding="utf-8", newline="") as archivo:
            CAMPOS = ["Nombre", "Población", "Superficie", "Continente"]
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
            escritor.writeheader() # Escribe los encabezados
            for pais in paises:
                escritor.writerow(pais) # Escribe cada país registro por registro
        return True
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        return False

# FUNCIONES DE APOYO Y VALIDACIÓN
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("ERROR: No puede ingresar un valor vacío.")
        elif texto.isdigit():
            print("ERROR: No puede ingresar solo números.")
        else:
            return texto

def pedir_entero(mensaje, minimo=1):
    while True:
        texto = input(mensaje).strip()
        try:
            numero = int(texto)
        except ValueError:
            print("ERROR: Debes ingresar un número entero.")
            continue
        if numero < minimo:
            print(f"ERROR: Debe ingresar un valor mayor o igual a {minimo}.")
        else:
            return numero

def pedir_rango():
    while True:
        minimo = pedir_entero("Ingrese el valor mínimo: ", 0)
        maximo = pedir_entero("Ingrese el valor maximo: ", 0)
        if minimo > maximo:
            print("ERROR: El valor mínimo no puede mayor que el máximo.")
        else:
            return minimo, maximo

def buscar_por_nombre(paises, texto):
    encontrados = []
    for pais in paises:
        if texto.lower() in pais["Nombre"].lower():
            encontrados.append(pais)
    return encontrados

def alinear_columna(dato, ancho):
    texto = str(dato)
    while len(texto) < ancho:
        texto += " "
    return texto

def mostrar_paises(paises):
    if len(paises) == 0:
        print("No hay paises para mostrar.\n")
        return
    print(
        alinear_columna("Nombre", 20) + " | " +
        alinear_columna("Población", 15) + " | " +
        alinear_columna("Superficie", 15) + " | " +
        alinear_columna("Continente", 15)
        )
    print("-" * 75)
    for pais in paises:
        print(
            alinear_columna(pais["Nombre"], 20) + " | " +
            alinear_columna(pais["Población"], 15) + " | " +
            alinear_columna(pais["Superficie"], 15) + " | " +
            alinear_columna(pais["Continente"], 15)
        )
    print()

# OPCIONES DEL MENÚ PRINCIPAL
def agregar_pais(paises, ruta):
    nombre = pedir_texto("Ingrese nuevo país: ").capitalize()

    # Valida si el país ya existe en la lista
    for pais in paises:
        if pais["Nombre"].lower() == nombre.lower():
            print("\nEse país ya se encuentra registrado.\n")
            return
    poblacion = pedir_entero("Ingrese su cantidad de población: ")
    superficie = pedir_entero("Ingrese su superficie en km^2: ")
    continente = pedir_texto("Ingrese continente al que pertenece: ").capitalize()
    nuevo_pais = {
        "Nombre": nombre,
        "Población": poblacion,
        "Superficie": superficie,
        "Continente": continente
    }
    paises.append(nuevo_pais)
    if guardar_paises(ruta, paises):
        print("\n-------- PAÍS AGREGADO CORRECTAMENTE --------")
    print()

def actualizar_pais(paises, ruta):
    nombre = pedir_texto("País a actualizar: ").capitalize()
    buscar = buscar_por_nombre(paises, nombre)
    if not buscar:
        print("País no encontrado.")
        return
    encontrado = buscar[0]
    print(f"País: {encontrado['Nombre']} | Población: {encontrado['Población']} | Superficie: {encontrado['Superficie']}")

    # Bucle para validar respuesta estricta S o N en Población
    while True:
        actualizar_poblacion = input("¿Actualizar población? (S/N): ").strip().upper()
        if actualizar_poblacion in ["S", "N"]:
            break
        print("ERROR: Debe ingresar S (Sí) o N (No).")
    if actualizar_poblacion == "S":
        encontrado["Población"] = pedir_entero("Población: ")

    # Bucle para validar respuesta estricta S o N en Superficie
    while True:
        actualizar_superficie = input("¿Actualizar superficie? (S/N): ").strip().upper()
        if actualizar_superficie in ["S", "N"]:
            break
        print("ERROR: Debe ingresar S (Sí) o N (No).")
    if actualizar_superficie == "S":
        encontrado["Superficie"] = pedir_entero("Superficie: ")
    # Guarda los cambios en el archivo
    if guardar_paises(ruta, paises):
        print("\n--- ACTUALIZACIÓN REALIZADA CORRECTAMENTE ---")
    print()

def buscar_paises(paises):
    texto = pedir_texto("País a buscar: ").capitalize()
    encontrado = buscar_por_nombre(paises, texto)
    if encontrado:
        print()
        mostrar_paises(encontrado)
    else:
        print("\nNo se encontraron coincidencias.\n")

def filtrar_paises(paises):
    print("Filtrar por:")
    print("1. Continente")
    print("2. Población")
    print("3. Superficie")
    while True:
        opcion = input("Seleccione una opción: ").strip()
        if opcion in ["1", "2", "3"]:
            break
        print("Opción invalida. Ingrese el número 1, 2 o 3.")
    if opcion == "1":
        continente = pedir_texto("Continente: ").strip().lower()
        filtrado = [pais for pais in paises if pais["Continente"].lower() == continente]
        if filtrado:
            print()
            mostrar_paises(filtrado)
        else:
            print("\nNo se encontraron paises de ese continente.\n")
    elif opcion == "2":
        minimo, maximo = pedir_rango()
        filtrado = [pais for pais in paises if minimo <= pais["Población"] <= maximo]
        if filtrado:
            print()
            mostrar_paises(filtrado)
        else:
            print("\nNo se encontraron paises con ese rango de población.\n")
    elif opcion == "3":
        minimo, maximo = pedir_rango()
        filtrado = [pais for pais in paises if minimo <= pais["Superficie"] <= maximo]
        if filtrado:
            print()
            mostrar_paises(filtrado)
        else:
            print("\nNo se encontraron paises con ese rango de superficie.\n")

def ordenar_paises(paises):
    print("Ordenar por:")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    # Valida opción de criterio
    while True:
        opcion = input("Seleccione una opción: ").strip()
        if opcion in ["1", "2", "3"]:
            break
        print("Opción invalida. Ingrese el número 1, 2 o 3.")
    print("\nTipo de orden:")
    print("1. Ascendente")
    print("2. Descendiente")

    # Valida tipo de orden
    while True:
        orden = input("Seleccione una opción: ").strip()
        if orden in ["1", "2"]:
            break
        print("Opción invalida. Ingrese el número 1 o 2.")
    reverso = True if orden == "2" else False

    # Aplica el ordenamiento según la opción elegida
    if opcion == "1":
        ordenado = sorted(paises, key=lambda pais: pais["Nombre"].lower(), reverse=reverso)
    elif opcion == "2":
        ordenado = sorted(paises, key=lambda pais: pais["Población"], reverse=reverso)
    elif opcion == "3":
        ordenado = sorted(paises, key=lambda pais: pais["Superficie"], reverse=reverso)
    print("\nPAISES ORDENADOS:")
    mostrar_paises(ordenado)

def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay datos cargados.\n")
        return

    # Obtiene los extremos usando funciones integradas
    mayor = max(paises, key=lambda pais: pais["Población"])
    menor = min(paises, key=lambda pais: pais["Población"])
    total_poblacion = 0
    total_superficie = 0
    cantidad_continente = {}

    # Recorre la lista acumulando totales y agrupando por continente
    for pais in paises:
        total_poblacion += pais["Población"]
        total_superficie += pais["Superficie"]
        continente = pais["Continente"]
        cantidad_continente[continente] = cantidad_continente.get(continente, 0) + 1
    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)

    # Muestra los resultados formateados en consola
    print("ESTADISTICAS:")
    print(f"\nPaís con mayor poblacion: {mayor['Nombre']} (Habitantes: {mayor['Población']})")
    print(f"País con menor poblacion: {menor['Nombre']} (Habitantes: {menor['Población']})")
    print(f"\nPromedio de poblacion: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")
    print("\nCantidad de países por continente:")
    for continente, cantidad in cantidad_continente.items():
        print(f"- {continente}: {cantidad}")
    print()

# PROGRAMA PRINCIPAL
def mostrar_menu():
    print("=============================================")
    print("         GESTIÓN DE DATOS DE PAÍSES")
    print("=============================================")
    print("1. Agregar un país")
    print("2. Actualizar datos de Población y Superficie")
    print("3. Buscar un país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Mostrar todos los países")
    print("8. Salir")
    print("---------------------------------------------")

def main():
    paises = cargar_paises(RUTA_CSV)
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        print()
        if opcion == "1":
            agregar_pais(paises, RUTA_CSV)
        elif opcion == "2":
            actualizar_pais(paises, RUTA_CSV)
        elif opcion == "3":
            buscar_paises(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            mostrar_paises(paises)
        elif opcion == "8":
            print("Programa finalizado. Adios.")
            break
        else:
            print("Opcion invalida. Ingrese un número del 1 al 8.")

if __name__ == "__main__":
    main()