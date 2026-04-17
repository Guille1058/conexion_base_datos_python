import pymysql
import keyboard
import os
import pandas
from tabulate import tabulate 
import ctypes
import platform

def main_loop(cursor, conexion):
    while True:
        flujo = int(input("Selecciona una opción de entre las siguientes para continuar:\n 1.- Insertar datos en una tabla. \n 2.- Mostrar datos de una tabla. \n 3.- Actualizar datos de una tabla. \n 4.- Borrar datos de una tabla. \n 5.- Crear una nueva tabla. \n 6.- Salir. \n->"))
        if flujo < 1 or flujo > 6:
            print("¡¡ERROR!! (VALOR NO VALIDO) -- Selecciona una opción de entre las siguientes para continuar:\n 1.- Insertar datos en una tabla. \n 2.- Mostrar datos de una tabla. \n 3.- Actualizar datos de una tabla. \n 4.- Borrar datos de una tabla. \n 5.- Crear una nueva tabla. \n 6.- Salir.")
        else:
            menu_principal(flujo, cursor, conexion)

def menu_principal(opcion, cursor, conexion):
    print("Presiona 'ESC' en cualquier momento para salir del programa de forma segura.")
    prompt = input("Seleccione la base de datos a usar -> ")
    cursor.execute(f"USE {prompt}")
    match opcion:
        case 1:
            repite = True
            while repite:
                nombre_tabla = input("Introduce el nombre de la tabla a insertar datos -> ")
                clave = input("Posicionate sobre el campo afectado -> ")
                valor = input("Introduce el valor del campo a insertar -> ")
                cursor.execute(f"INSERT INTO {nombre_tabla} ({clave}) VALUES (%s)",(valor,))
                conexion.commit()
                output = input("¿Desea insertar otro campo? (S/N) -> ")
                if output.upper() == "N":
                    repite = False
            return
        case 2:
            repite = True
            while repite:
                nombre_tabla = input("Introduce el nombre de la tabla a mostrar -> ")
                dataframe = pandas.read_sql(f"SELECT * FROM {nombre_tabla}", conexion)
                print(tabulate(dataframe, headers='keys', tablefmt='grid'))
                output = input("¿Desea mostrar otra tabla? (S/N) -> ")
                if output.upper() == "N":
                    repite = False
            return
        case 3:
            repite = True
            while repite:
                nombre_tabla = input("Introduce el nombre de la tabla a actualizar -> ")
                clave = input("Introduce el nombre del campo a actualizar -> ")
                valor = input("Introduce el nuevo valor del campo a actualizar -> ")
                cursor.execute(f"UPDATE {nombre_tabla} SET {clave} = {valor}")
                conexion.commit()
                output = input("¿Desea actualizar otro campo? (S/N) -> ")
                if output.upper() == "N":
                    repite = False
            return
        case 4:
            repite = True
            while repite:
                prompt = int(input("Qué quieres borrar en específico? (1.- Borrar toda la tabla / 2.- Borrar una columna completa / 3.- Borrar una base de datos completa)"))
                match prompt:
                    case 1:
                        nombre_tabla = input("Introduce el nombre de la tabla a borrar -> ")
                        cursor.execute(f"DELETE FROM {nombre_tabla}")
                    case 2:
                        nombre_tabla = input("Introduce el nombre de la tabla afectada -> ")
                        clave = input("Introduce el nombre de la columna a borrar -> ")
                        cursor.execute(f"ALTER TABLE {nombre_tabla} DROP COLUMN {clave}")
                    case 3:
                        nombre_bbdd = input("Introduce el nombre de la base de datos a borrar -> ")
                        cursor.execute(f"DROP DATABASE IF EXISTS {nombre_bbdd}")
                conexion.commit()
                output = input("¿Desea borrar otro campo? (S/N) -> ")
                if output.upper() == "N":
                    repite = False
            return
        case 5:
            # Crear y usar la base de datos
            repite = True
            while repite:
                nombre_bbdd = input("Introduce el nombre de la base de datos a crear -> ")
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_bbdd}")
                cursor.execute(f"USE {nombre_bbdd}")
                i = 0
                num_tablas = int(input("¿Cuántas tablas deseas crear en la base de datos? (Deben ser entre 1 y 10) -> "))
                while num_tablas < 0 or num_tablas > 10:
                    num_tablas = int(input("¡¡ERROR!! (VALOR NO VALIDO) -- ¿Cuántas tablas deseas crear en la base de datos? (Deben ser entre 1 y 10) -> "))
                while i < num_tablas:
                    nombre_tabla = input("Introduce el nombre de la tabla a crear -> ")
                    cursor.execute(f"CREATE TABLE IF NOT EXISTS {nombre_tabla} (id INT AUTO_INCREMENT PRIMARY KEY)")
                    i += 1
                num_registros = int(input("¿Cuántos registros deseas insertar en la tabla? (Deben ser entre 1 y 100)-> "))
                while num_registros < 0 or num_registros > 50:
                    num_registros = int(input("¡¡ERROR!! (VALOR NO VALIDO) -- ¿Cuántos registros deseas insertar en la tabla? (Deben ser entre 1 y 100)-> "))
                i = 0
                while i < num_registros:
                    clave = input("Introduce el nombre del campo a insertar -> ")
                    cursor.execute(f"ALTER TABLE {nombre_tabla} ADD {clave} VARCHAR(255)")
                    i += 1
                conexion.commit()
                output = input("¿Desea crear otra base de datos? (S/N) -> ")
                if output.upper() == "N":
                    repite = False
            return
        case 6:
            print("Saliendo del programa...")
            conexion.close()
            print("Conexión cerrada")
            os._exit(0)
        

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
    return os._exit(0) # Fuerza la salida inmediata del proceso

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
    cursor.execute("CREATE DATABASE IF NOT EXISTS eig_alumnos")
    cursor.execute("USE eig_alumnos")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Gente (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(50) DEFAULT 'Sin nombre',
                        apellidos VARCHAR(50) DEFAULT 'Sin apellidos',
                        contraseña VARCHAR(10) DEFAULT 'Sin contraseña',
                        perfil VARCHAR(30) DEFAULT 'Sin perfil'
                    )""")
    print("Base de datos por defecto creada y seleccionada correctamente -- /eig_alumnos/ --")

    # MOSTRAMOS LOS DETALLES DE LA TABLA POR DEFECTO
    dataframe = pandas.read_sql("SELECT * FROM Gente", conexion)
    print(tabulate(dataframe, headers='keys', tablefmt='grid'))
    main_loop(cursor, conexion)


except Exception as err:
    print("Error:", err)