import pyodbc 
#TODO: Configuracion de la conexcion sql server
server = "DDURAN\INSDESKTOP"
database = 'Sistemas_Farz'
username = 'sa'
password = 'InsDesktop1'

#TODO: Crear la cadena de conexion
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID{username};PWD={password}'

#TODO: establecer la conexion
conn = pyodbc.connect(conn_str)

#TODO: crear cursor
cursor = conn.cursor()

try:
    #TODO: Llamar al query
    cursor.execute("SELECT TOP (1000) [id_usuario],[emp],[password],[estado] FROM [Sistemas_Farz].[dbo].[Usuarios]")
    #TODO: Obtener Resultados
    rows = cursor.fetchall()
    #TODO: mostrar los resultados en consola
    for row  in rows:
        print(row)
except Exception as e:
    print(f"Error:{str(e)}")

finally:
    cursor.close
    conn.close