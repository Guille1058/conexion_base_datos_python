import pymysql

conexion = None

try:
    conexion = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="base_de_datos",
        port=3306
    )
    print("Conexión correcta")

    cursor = conexion.cursor()

    # Crear tabla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50),
            email VARCHAR(50)
        )
    """)

    # Insertar datos (columnas correctas)
    
    sql = "INSERT INTO usuarios (nombre, email, telefono, dni) VALUES (%s, %s, %s, %s)"
    valores = ("Guillermo", "gcu25gr016@student.esgerencia.com", "658281840", "78112397G")

    cursor.execute(sql, valores)
    conexion.commit()

    print("Datos insertados correctamente")

except Exception as err:
    print("Error:", err)

finally:
    if conexion:
        conexion.close()
        print("Conexión cerrada")