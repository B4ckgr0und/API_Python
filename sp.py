from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

#TODO: crear na instancia de la aplicacion flask
app = Flask(__name__)

nombre_usuario = 'sa'
contrasena = 'InsDesktop1'
nombre_servidor = 'DDURAN\INSDESKTOP'
nombre_basededatos = 'Sistemas_Farz'
driver_obdc  = 'DRIVER=ODBC+Driver+18+for+SQL+Server'

#cadena_conexion = f'mssql+pyodbc://{nombre_usuario}:{contrasena}@{nombre_servidor}/{nombre_basededatos}?DRIVER={driver_obdc};'
cadena_conexion = f'mssql+pyodbc://{nombre_usuario}:{contrasena}@{nombre_servidor}/{nombre_basededatos}?Encrypt=no&TrustServerCertificate=yes&driver=ODBC+Driver+18+for+SQL+Server'

app.config['SQLALCHEMY_DATABASE_URI']=cadena_conexion
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/store_procedure')
def consulta_sql_directa():
    nombre_store_procedure = 'sp_lista_empleados_01'

    sql_query = text(f'exec {nombre_store_procedure}')
    resultados = db.session.execute(sql_query)
    usuarios_json = [dict(row._asdict()) for row in resultados]

    return jsonify({'usuarios':usuarios_json})


#TODO: iniciar la aplicacion si este script es ejecutado directamente
if __name__ == '__main__':
    #TODO: conconfiguracion para ejecutar la aplicacion en modo depuracion
    app.run(debug=True)