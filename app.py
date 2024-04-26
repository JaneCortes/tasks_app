# Importamos las funciones necesarias de Flask
from flask import Flask, render_template, request, redirect, url_for

# Creamos una nueva aplicación Flask
app = Flask(__name__)

# Inicializamos una lista vacía para almacenar las tareas
tareas = []

# Definimos la ruta principal ('/') de nuestra aplicación
@app.route('/')
def home():
    # Renderizamos la plantilla 'index.html' y le pasamos las tareas y la función enumerate
    return render_template('index.html', tareas=tareas, enumerate=enumerate)

# Definimos la ruta '/agregar' que responde a solicitudes POST
@app.route('/agregar', methods=['POST'])
def agregar():
    # Obtenemos la tarea del formulario enviado
    tarea = request.form.get('tarea')
    # Añadimos la tarea a nuestra lista de tareas
    tareas.append({"nombre": tarea, "completada": False})
    # Redirigimos al usuario a la página principal
    return redirect(url_for('home'))

# Definimos la ruta '/editar/<int:id>' que responde a solicitudes POST
@app.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    # Obtenemos la nueva tarea del formulario enviado
    nueva_tarea = request.form.get('tarea')
    # Actualizamos la tarea en nuestra lista de tareas
    tareas[id]["nombre"] = nueva_tarea
    # Redirigimos al usuario a la página principal
    return redirect(url_for('home'))

# Definimos la ruta '/borrar/<int:id>'
@app.route('/borrar/<int:id>')
def borrar(id):
    # Eliminamos la tarea de nuestra lista de tareas
    tareas.pop(id)
    # Redirigimos al usuario a la página principal
    return redirect(url_for('home'))

# Definimos la ruta '/completar/<int:id>'
@app.route('/completar/<int:id>')
def completar(id):
    # Marcamos la tarea como completada
    tareas[id]["completada"] = True
    # Redirigimos al usuario a la página principal
    return redirect(url_for('home'))

# Si este archivo es el punto de entrada principal, ejecutamos la aplicación
if __name__ == '__main__':
    app.run(debug=True)