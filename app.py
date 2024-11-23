from flask import Flask,jsonify,request

#TODO: crear na instancia de la aplicacion flask
app = Flask(__name__)

 #datos de ejemplo usuarios
usuarios = [{'id':1,'nombre':'alexa'},{'id':2,'nombre':'Juan Carlos'},{'id':3,'nombre':'XXX'}]

#TODO: definir una ruta para la pagina principal
@app.route('/')
def hola_mundo():
    return 'Hola mundo'

#definir una ruta para obtener la lista de usuarios
@app.route('/usuarios')
def obtener_usuarios():
   
    #convertir la lista de usuarios a formato json y devolverlos como respuesta
    return jsonify({'usuarios':usuarios})

#TODO: Definir una rita para obtener un usuario por su ID
@app.route('/usuario/<int:id_usuario>')
def obtener_usuario(id_usuario):
    #TODO: Buscar el usuario por ID  en la lista de Usuarios
    usuario = next((user for user in usuarios if user['id']==id_usuario),None)
    #TODO: verficiar si se encotro el usuario y devolverlo
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'Mensaje':'Usuario no encontrado'}),404
@app.route('/buscar')
def buscar_usuario():
    nombre = request.args.get('nombre')
    usuarios_encontrados = [user for user in usuarios if nombre.lower() in user['nombre'].lower()]
    if usuarios_encontrados:
        return jsonify({'usuarios':usuarios_encontrados})
    else:
        return jsonify({'Mensaje':'Usuario no encontrado'}),404
    

#TODO: iniciar la aplicacion si este script es ejecutado directamente
if __name__ == '__main__':
    #TODO: conconfiguracion para ejecutar la aplicacion en modo depuracion
    app.run(debug=True)