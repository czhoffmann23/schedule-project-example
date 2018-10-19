
# -*- coding: utf-8 -*-
#!/usr/bin/env python
from mysql.connector import (connection)

def run_query(query=''): 
    conn = connection.MySQLConnection(user='root', password='',host='127.0.0.1',database='sistema')# Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 
    
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select
        
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos
        data = None 
 
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexión 
    
    
    return data

#==============  Get ================
def CallServiceGet(Tabla):
    query="SELECT * FROM "+str(Tabla)+""
    data = run_query(query)
    error=[]
    if data==error:
       return error

    else:
        return data

#==============  GetOne ================
def CallServiceGetOne(Tabla,id):
    query="SELECT * FROM "+str(Tabla)+" WHERE id ="+str(id)+""
    data = run_query(query)
    error=[]
    if data==error:
        print("No se encontro niuna wam")

    else:
        return data

