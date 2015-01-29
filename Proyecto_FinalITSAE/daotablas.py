# coding:utf-8
'''
Created on 19/1/2015

@author: PC30
'''

from ec.edu.itsae.dao import PersonaDao, trabajadorDao

'''vamos a crear un objeto de persona dao'''

obj=PersonaDao.PersonaDao()
print obj.reportarPersona()


objt=trabajadorDao.TrabajadorDao()
print objt.reportarTrabajador()