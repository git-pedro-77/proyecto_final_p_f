# coding:utf-8
'''
Created on 24/1/2015

@author: Programacion
'''
from app import app
from ec.edu.itsae.dao import trabajadorDao
from flask import render_template, request, redirect, url_for


@app.route("/maintrabajador")# para entar a la pagina por main
def maintrabajador():
    objt=trabajadorDao.TrabajadorDao().reportarTrabajador()#llamar al reporte
    return render_template("trabajador.html", data=objt)#enviando al archivo html y ahi organizarlo

@app.route("/addTrabajador", methods=['POST'])
def addTrabajador():
    usuario=request.form.get('usuario', type=str)
    clave=request.form.get('clave', type=str)
    estado=request.form.get('estado', type=int)
    fecha_acceso=request.form.get('fecha_Ingreso', type=str)
    idTipoTrabajador=request.form.get('tipoid', type=int)
    
    trabajadorDao.TrabajadorDao().insertarTrabajador(usuario, clave, estado, fecha_acceso, idTipoTrabajador)
    return redirect(url_for('maintrabajador'))

@app.route("/buscarautopt")# para entar a la pagina por main persona al metodo
def buscarTrabajadorAuto():
    nombre=str(request.args.get('term'))
    objt=trabajadorDao.TrabajadorDao().buscarTrabajadorNombre(nombre)#llamar al reporte
    # print objR  #solo es para provar las impresiones
    return objt #enviando al archivo html y ahi organizarlo

@app.route("/eliminardatoT")# para entar a la pagina por main persona al metodo
def eliminarTrabajadorDato():
    datoeli=request.args.get('idpersona')
    trabajadorDao.TrabajadorDao().eliminarTrabajador(datoeli)
    return redirect(url_for('maintrabajador'))


@app.route("/buscardatoT")# para entar a la pagina por main persona al metodo
def buscarTrabajadorDato():
    nombre=str(request.args.get('bnombre'))
    objt=trabajadorDao.TrabajadorDao().buscarTrabajadorDato(nombre)
    return render_template("trabajador.html", data=objt)




