# coding:utf-8
'''
Created on 24/1/2015

@author: Programacion
'''

from ec.edu.itsae.conn import DBcon
import json 


class TrabajadorDao(DBcon.DBcon):#heredando
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass#sirve cuando no hay implementacion en el metodo
    
    
    def reportarTrabajador(self):
        con=self.conexion().connect().cursor()  #capturando de la clase DBcon
        con.execute(" select * from trabajador ")
        reporte=con.fetchall()
        return reporte #despues del return no se debe colocar nada

    def insertarTrabajador(self, usuario, clave, estado, fecha_acceso, idTipoTrabajador):
        con=self.conexion().connect()
        sql= """insert into trabajador(usuario, clave, estado, fecha_acceso, idTipoTrabajador)
                             values ('%s', '%s', %i, '%s', %i)
                             """ %(usuario, clave, estado, fecha_acceso, idTipoTrabajador) 
        print sql   # Para imprimir nuestra consulta para poder ver        
        with con:
            cursor=con.cursor()
            cursor.execute(sql)#aqui debe estar sql para que se ejecute el insert
    
        #deber actualizar y eliminar
    def eliminarTrabajador(self,datoelim):
        con=self.conexion().connect()
        sql= """ delete from trabajador where idpersona= %i """ %int(datoelim)
        #print sql    Para imprimir nuestra consulta para poder ver        
        with con:
            cursor=con.cursor()
            cursor.execute(sql)#aqui debe estar sql para que se ejecute el insert
    
    def buscarTrabajadorNombre(self, datobusca):
        con=self.conexion().connect().cursor()  #capturando de la clase DBcon
        con.execute(""" select CONCAT (usuario) as value, idpersona as id from trabajador where upper(CONCAT (usuario)) like upper('%s') """ %("%"+datobusca+"%") )
        reporte=con.fetchall()
        columna=('value', 'id')
        lista=[]
        print con.execute
        for row in reporte:
            lista.append(dict(zip(columna,row))) #dict = diccionario, zip = para unir las las dos columnas
        return json.dumps(lista, indent=2) 
    
    def buscarTrabajadorDato(self, datobuscado):
        con=self.conexion().connect().cursor() 
        sql=""" select * from trabajador where upper(CONCAT (usuario)) like upper('%s') """ %("%"+datobuscado+"%")
        print sql
        con.execute(sql)
        reporte=con.fetchall() 
        return reporte 
    
    
    '''
    def validarUsuario(self, usuario,clave):
        con=self.conexion().connect().cursor() 
        con.execute(""" select * from trabajador where usuario='%s' and clave='%s' """ %(usuario, clave))
        reporte=con.fetchall() 
        return reporte '''

    
    