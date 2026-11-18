# Gestión De Datos De Países En Python

*Tecnicatura Universitaria en Programación (UTN)*

**Trabajo Práctico Integrador de la materia de Programación I**

Es un programa de consola hecho en Python que maneja una lista de países, los cuales se pueden agregar, buscar, filtrar, ordenar y ver sus estadísticas. Los datos se guardan en un archivo CSV, por lo que no se pierden al cerrar el programa.

## ¿Qué hace el programa?

Gestiona 4 datos de cada país.

| DATO | TIPO | CONTENIDO |
|------|------|-----------|
| Nombre | Texto | Nombre del país |
| Población | Número entero | Cantidad de habitantes que posee |
| Superficie | Número entero | Cantidad km^2 que ocupa |
| Continente | Texto | Continente en el que se hubica |

### Opciones principales:

1. **Agregar un país:** Carga un país nuevo (sin campos vacíos ni repetidos).

2. **Actualizar datos de Población y Superficie:** Cambia esos datos de un país que ya existe.

3. **Buscar un país por nombre:** Sirve el nombre entero o solo un pedacito.

4. **Filtrar países:** Por continente, rango de población o rango de superficie.

5. **Ordenar países:** Por nombre, población o superficie, ascendente o descendente.

6. **Mostrar estadísticas:** Mayor y menor población, promedios y países por continente.

7. **Mostrar todos los países:** Muestra la lista completa en una tabla.

8. **Salir:** Cierra el programa.

## Registro del Archivo CSV

Tiene que estar guardado en UTF-8

```
Nombre,Población,Superficie,Continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

## Instrucciones de uso

Necesitas tener Python 3.

1. Descargar o clonar el repositorio y entrar a la carpeta desde la terminal.

2. Asegurarse de que paises.csv esté junto a main.py, o crear un nuevo archivo paises.csv ejecutando el codigo.

3. Ejecutar "python main.py".

4. Seleccionar una opción

## Ejemplos de entrada/salida

**Menú Principal**
```
=============================================
         GESTIÓN DE DATOS DE PAÍSES
=============================================
1. Agregar un país
2. Actualizar datos de Población y Superficie
3. Buscar un país por nombre
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. Mostrar todos los países
8. Salir
---------------------------------------------
Seleccione una opción:
```

**1. Agregar un país**

No importa si se escribe en minúscula, el programa pone la primera letra en mayúscula
```
Seleccione una opción: 1

Ingrese nuevo país: chile
Ingrese su cantidad de población: 19500000
Ingrese su superficie en km^2: 756102
Ingrese continente al que pertenece: américa

-------- PAÍS AGREGADO CORRECTAMENTE --------
```
Si el país que se ingresa ya estaba cargado se imprime en pantalla:
```
Ese país ya se encuentra registrado.
```

**2. Actualizar datos de Población y Superficie**
```
Seleccione una opción: 2

País a actualizar: argentina
País: Argentina | Población: 45376763 | Superficie: 2780400
¿Actualizar población? (S/N): s
Población: 46000000
¿Actualizar superficie? (S/N): n

--- ACTUALIZACIÓN REALIZADA CORRECTAMENTE ---
```

**3. Buscar un país por nombre**
```
Seleccione una opción: 3

País a buscar: arg

Nombre               | Población       | Superficie      | Continente
---------------------------------------------------------------------------
Argentina            | 45376763        | 2780400         | América
Alemania             | 83149300        | 357022          | Europa
```

**4. Filtrar países**
```
Seleccione una opción: 4

Filtrar por:
1. Continente
2. Población
3. Superficie
Seleccione una opción: 2
Ingrese el valor mínimo: 50000000
Ingrese el valor maximo: 150000000

Nombre               | Población       | Superficie      | Continente
---------------------------------------------------------------------------
Japón                | 125800000       | 377975          | Asia
Alemania             | 83149300        | 357022          | Europa
```

**5. Ordenar países**
```
Seleccione una opción: 5

Ordenar por:
1. Nombre
2. Población
3. Superficie
Seleccione una opción: 2

Tipo de orden:
1. Ascendente
2. Descendiente
Seleccione una opción: 2

PAISES ORDENADOS:
Nombre               | Población       | Superficie      | Continente
---------------------------------------------------------------------------
Brasil               | 213993437       | 8515767         | América
Japón                | 125800000       | 377975          | Asia
Alemania             | 83149300        | 357022          | Europa
Argentina            | 45376763        | 2780400         | América
```

**6. Mostrar estadísticas**
```
Seleccione una opción: 6

ESTADISTICAS:

País con mayor poblacion: Brasil (Habitantes: 213993437)
País con menor poblacion: Argentina (Habitantes: 45376763)

Promedio de poblacion: 117079875.00
Promedio de superficie: 3007791.00

Cantidad de países por continente:
- América: 2
- Asia: 1
- Europa: 1
```

**7. Mostrar todos los países**
```
Seleccione una opción: 7

Nombre               | Población       | Superficie      | Continente
---------------------------------------------------------------------------
Argentina            | 45376763        | 2780400         | América
Japón                | 125800000       | 377975          | Asia
Brasil               | 213993437       | 8515767         | América
Alemania             | 83149300        | 357022          | Europa
```

**8. Salir**
```
Programa finalizado. Adios.
```

## Contenido del Repositorio
```
├── main.py                         # Código principal
├── paises.csv                      # Base de datos en CSV
├── TPI_Documentación_Pro-1.pdf     # Informe teórico en PDF
└── README.md                       # Este archivo
```

## Cierre

### Links del resto del proyecto

Documentación en PDF: https://drive.google.com/file/d/1k-yP10-nIntCzIBxK3I2UCd7aXiqzWbG/view?usp=drive_link 

Video Demostrativo: https://drive.google.com/file/d/1s2ogeystc-drvDxTbSTuZ34kWUxXS32V/view?usp=drive_link 

Repositorio de GitHub: https://github.com/ignacioobredor2005-lab/TPI_Programa_de_Gestion_de_Datos_de_Paises_Pro-1.git 

### Alumno

Luis Ignacio Obredor Garcia

Legajo: 55248