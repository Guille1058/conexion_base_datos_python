# 🗄️ Gestor de Bases de Datos en Python (DBMS CLI)

Este proyecto es una aplicación de línea de comandos (CLI) desarrollada en Python que permite gestionar bases de datos MySQL de forma interactiva. Incluye funcionalidades completas de administración como inserción, consulta, actualización y eliminación de datos, así como la creación y eliminación de bases de datos y tablas.

---

## 🚀 Características

* 📥 Insertar datos en tablas
* 📊 Mostrar datos en formato tabla
* ✏️ Actualizar registros existentes
* 🗑️ Borrar tablas o columnas
* 🏗️ Crear nuevas tablas dinámicamente
* 🧱 Crear y eliminar bases de datos
* 💻 Ejecutar consultas SQL personalizadas
* ⛔ Salida de emergencia con tecla `ESC`
* 🔐 Requiere permisos de administrador/root

---

## 🧰 Tecnologías utilizadas

* Python 3
* MySQL
* Librerías:

  * `pymysql`
  * `pandas`
  * `tabulate`
  * `keyboard`
  * `ctypes`
  * `platform`

---

## 📦 Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

2. Instala las dependencias necesarias:

```bash
pip install pymysql pandas tabulate keyboard
```

3. Asegúrate de tener MySQL en ejecución.

---

## ⚙️ Configuración

Edita los parámetros de conexión en el código si es necesario:

```python
conexion = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    port=3306
)
```

---

## ▶️ Uso

Ejecuta el script como administrador/root:

```bash
python nombre_del_script.py
```

Al iniciar, verás un menú interactivo con las siguientes opciones:

```
1.- Insertar datos
2.- Mostrar datos
3.- Actualizar datos
4.- Borrar datos
5.- Crear tabla
6.- Crear base de datos
7.- Borrar base de datos
8.- Ejecutar SQL personalizado
9.- Salir
```

Puedes presionar `ESC` en cualquier momento para salir de forma segura.

---

## 🧪 Base de datos por defecto

El programa crea automáticamente:

* Base de datos: `eig_alumnos`
* Tabla: `Gente`

Estructura:

| id | nombre | apellidos | contraseña | perfil |
| -- | ------ | --------- | ---------- | ------ |

---

## ⚠️ Consideraciones importantes

* ⚡ Ejecutar como administrador o con `sudo`
* ⚠️ No hay validación contra inyección SQL en entradas personalizadas
* 🔒 Uso recomendado en entornos de desarrollo o aprendizaje
* 💾 Asegúrate de tener backups si trabajas con datos reales

---

## 🛠️ Posibles mejoras

* Interfaz gráfica (GUI)
* Validación de entradas más robusta
* Soporte para múltiples usuarios
* Logs de operaciones
* ORM (como SQLAlchemy)

---

## 📄 Licencia

Este proyecto es de uso libre para fines educativos.

---

## 👨‍💻 Autor

Desarrollado como proyecto de aprendizaje en gestión de bases de datos con Python y MySQL.
