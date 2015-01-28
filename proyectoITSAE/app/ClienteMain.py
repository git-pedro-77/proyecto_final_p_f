# coding:utf-8
'''
Created on 19/1/2015

@author: Programacion
'''
from app import app
from ec.edu.itsae.dao import ClienteDao 
from flask import render_template, request, redirect, url_for




@app.route("/maincliente")# para entar a la pagina por main persona al metodo
def maincliente():
    objR=ClienteDao.ClienteDao().reportarCliente()#llamar al reporte
    return render_template("cliente.html", data=objR)#enviando al archivo html y ahi organizarlo


@app.route("/addCliente", methods=['POST'])
def addCliente():
    dni_cliente=request.form.get('Cedula', type=str)
    nombre=request.form.get('nombre', type=str)
    apellido=request.form.get('apellido', type=str)
    celular=request.form.get('celular', type=str)
    direccion=request.form.get('direccion', type=str)
    correo=request.form.get('correo', type=str)
    sexo=request.form.get('sexo', type=str)
    telefono=request.form.get('telefono', type=str)
    estado=request.form.get('estado', type=int)
    
    ClienteDao.ClienteDao().insertarCliente(dni_cliente, nombre, apellido, celular, direccion, correo, sexo, telefono, estado)
    return redirect(url_for('maincliente'))

@app.route("/buscarautoc")# para entar a la pagina por main persona al metodo
def buscarPersonaAuto():
    nombre=str(request.args.get('term'))
    objR=ClienteDao.ClienteDao().buscarClienteNombre(nombre)#llamar al reporte
    # print objR  #solo es para provar las impresiones
    return objR #enviando al archivo html y ahi organizarlo

@app.route("/eliminardatoc")# para entar a la pagina por main persona al metodo
def eliminarPersonaDato():
    datoeli=request.args.get('id_cliente')
    ClienteDao.ClienteDao().eliminarCliente(datoeli)
    return redirect(url_for('maincliente'))


@app.route("/buscardatoc")# para entar a la pagina por main persona al metodo
def buscarPersonaDato():
    nombre=str(request.args.get('bnombre'))
    objR=ClienteDao.ClienteDao().buscarClienteDato(nombre)
    return render_template("cliente.html", data=objR)

@app.route("/buscardatoc")# para entar a la pagina por main persona al metodo
def buscarDatot():
    nombre=str(request.args.get('nombret'))
    objR=ClienteDao.ClienteDao().validartrabajador(nombre)
    return render_template("cliente.html", data=objR)


