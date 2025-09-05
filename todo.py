import sqlite3

# Conexion a la base de datos (se crea si no existe)
conexion = sqlite3.connect("tareas.db")
cursor = conexion.cursor()


# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL
)
 """)


# Funcion para agregar tarea
def agregar_tarea():
	nueva_tarea = input("Ingrese una tarea: ")
	cursor.execute("INSERT INTO tareas (descripcion) VALUES (?)", (nueva_tarea,))
	conexion.commit()
	print("Tarea agregada con exito.\n")


# Funcion para ver todas las tareas
def ver_tareas():
	cursor.execute("SELECT * FROM tareas")
	tareas = cursor.fetchall()
	print("\nLista de tareas:")
	if not tareas:
		print("No hay tareas registradas.")
	for tarea in tareas:
		print(f"{tarea[0]} - {tarea[1]}")
	print()


# Funcion para actualizar una tarea
def actualizar_tarea():
	ver_tareas()
	tarea_id = input("Ingrese el ID de la tarea a actualizar: ")
	nueva_desc = input("Ingrese la nueva descripcion: ")
	cursor.execute("UPDATE tareas SET descripcion = ? WHERE id = ?", (nueva_desc, tarea_id))
	conexion.commit()
	print("Tarea actualizada con exito. \n")


# Funcion para eliminar una tarea
def eliminar_tarea():
	ver_tareas()
	tarea_id = input("Ingrese el ID de la tarea a eliminar: ")
	cursor.execute("DELETE FROM tareas WHERE id = ?", (tarea_id))
	conexion.commit()
	print("Tarea eliminada con exito. \n")


# Menu principal
while True:
	print("=== Menu ToDo App ===")
	print("1. Agregar tarea")
	print("2. Ver tareas")
	print("3. Actualizar tarea")
	print("4. Eliminar tarea")
	print("5. Salir")

	opcion = input("Elija una opcion: ")

	if opcion == "1":
		agregar_tarea()
	elif opcion == "2":
		ver_tareas()
	elif opcion == "3":
		actualizar_tarea()
	elif opcion == "4":
		eliminar_tarea()
	elif opcion == "5":
		print("Saliendo de la aplicacion...")
		break
	else:
		print("Opcion no valida,intente de nuevo.")


# Cerrar conexion
conexion.close()


