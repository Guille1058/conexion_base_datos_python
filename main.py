import pymysql
import keyboard
import os
import pandas
from tabulate import tabulate 
import ctypes
import platform

def es_administrador():
    try:
        # Para sistemas basados en Unix (Linux, macOS)
        if platform.system() != "Windows":
            return os.getuid() == 0
        
        # Para Windows
        else:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except AttributeError:
        return False

# Función para cerrar el programa inmediatamente

def salir_emergencia():
    print("\nSaliendo del programa de forma segura...")
    # Cerramos la conexión si existe antes de forzar el cierre
    if 'conexion' in globals() and conexion:
        conexion.close()
    os._exit(0) # Fuerza la salida inmediata del proceso

# Funciones input

def creacion_bbdd(cursor):
    # Crear y usar la base de datos
    cursor.execute("CREATE DATABASE IF NOT EXISTS alumnos_eig")
    cursor.execute("USE alumnos_eig")

    # Crear tabla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Gente(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            apellidos VARCHAR(50) NOT NULL,
            contraseña VARCHAR(10) NOT NULL,
            perfil VARCHAR(30) NOT NULL
        )
    """)

def introducir_datos():
    v1 = input("Introduce un nombre para el usuario -> ")
    while len(v1)< 1 or len(v1) > 50:
        v1 = input("¡¡ERROR!! (VALOR NO VALIDO) -- Introduce un nombre para el usuario\nLongitud de caracteres permitida 1-50 -> ")
    v2 = input("Introduce los apellidos para el usuario -> ")
    while len(v2) < 1 or len(v2) > 50:
        v2 = input("¡¡ERROR!! (VALOR NO VALIDO) -- Introduce apellidos para el usuario\nLongitud de caracteres permitida 1-50 -> ")
    v3 = input("Introduce la contraseña para el usuario -> ")
    while len(v3) < 1 or len(v3) > 10:
        v3 = input("¡¡ERROR!! (VALOR NO VALIDO) -- Introduce una contraseña para el usuario\nLongitud de caracteres permitida 1-10 -> ")
    v4 = input("Introduce el perfil para el usuario -> ")
    while len(v4) < 1 or len(v4) > 30:
        v4 = input("¡¡ERROR!! (VALOR NO VALIDO) -- Introduce un perfil para el usuario (ej: admin / editor / etc.)\nLongitud de caracteres permitida 1-30 -> ")
    return [v1, v2, v3, v4]

if not es_administrador():
    print("¡ERROR! - Debes ejecutar este programa como administrador o sudo, vuelve a intentarlo más tarde.")
    os._exit(0)

conexion = None
# Registramos el 'hotkey'. En cualquier momento que presiones la tecla -ESC-, se cerrará.
keyboard.add_hotkey('esc', salir_emergencia)

try:
    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        port=3306
    )
    print("Conexión correcta")
    cursor = conexion.cursor()
    creacion_bbdd(cursor) #Función para crear la base de datos.

    # Insertar datos (columnas correctas)
    sql = "INSERT INTO Gente (nombre, apellidos, contraseña, perfil) VALUES (%s, %s, %s, %s)"

    # Request al usuario
    i = int(input("INTRODUCE LA CANTIDAD DE USUARIOS A ALMACENAR EN LA BASE DE DATOS. -> "))
    contador = 0

    while contador < i:
        vector = introducir_datos()
        valores = (vector[0], vector[1], vector[2], vector[3])
        cursor.execute(sql, valores)
        conexion.commit()
        print("------------------------")
        print("*** Datos insertados correctamente ***")
        print("------------------------")
        dataframe = pandas.read_sql("SELECT * FROM Gente", conexion)
        print(tabulate(dataframe, headers='keys', tablefmt='grid'))
        contador+=1

except Exception as err:
    print("Error:", err)

finally:
    if conexion:
        conexion.close()
        print("Conexión cerrada")