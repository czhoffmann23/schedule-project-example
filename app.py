from bottle import route, run, template,static_file,error,post, request, redirect, url
import sys
sys.path.append('./controllers/')
from asigController import *

@error(404)
def error404(error):
    return '<h1> TE EQUIVOCASTE OE ERROR 404 </h1>'
@route('/')
def index():
    return template('index')

@route('/login')
def login():
    return '<h1> CACACA POTO </h1>'
#===========  Visualizar  ===========
@route('/ProfesoresAll')
def profesores():
    return '<h1>Profesores Pagina!</h1>'

@route('/AsignaturaAll')
def asignaturas():
    resultado=AsignaturasAll()
    return template('AsignaturaAll',rows=resultado)
#===========  Detalle     ===========
@route('/Profesor/Detalle/<id>')
def profesorDetalle(id):
    return '<h1>Profesor Detalle Pagina!</h1>'

@route('/Asignatura/Detalle/<id>')
def asginaturaDetalle(id):
    return '<h1>Asginatura Detalle Pagina!</h1>'

#===========  Modificar   ===========
@route('/Profesor/Modificar/<id>')
def profesorModificar(id):
    return '<h1>Profesor Modificar Pagina!</h1>'

@route('/Asignatura/Modificar/<id>')
def asignaturaModificar(id):
    return '<h1>Asginatura Modificar Pagina!</h1>'

#===========  Eliminar    ===========
@route('/Profesor/Eliminar/<id>')
def profesorEliminar(id):
    return '<h1>Profesor Eliminar Pagina!</h1>'

@route('/Asignatura/Eliminar/<id>')
def asignaturaEliminar(id):
    return '<h1>Asginatura Eliminar Pagina aaaa  '+id+'!</h1>'

#===========    Crear     ===========
@route('/Profesor/Nuevo')
def profesoresCrear():
    return '<h1>Profesores Crear Pagina!</h1>'

@route('/Asignatura/Nueva')
def asignaturaCrear():
    return template('AsignaturaNueva')

@route('/', method="POST")
def process():
    obj=[]
    nombre = request.forms.get('nombre')
    semestre = request.forms.get('semestre')
    carrera = request.forms.get('carrera')
    nrc = request.forms.get('nrc')
    obj.append(nrc)
    obj.append(nombre)
    obj.append(carrera)
    obj.append(semestre)
  
    opcion=AsignaturaCreate(obj)
    if opcion==1: #exito
        redirect(url('/Asignatura/Nueva') + '#exito')
    if opcion == 2:          #error en ingreso
        redirect(url('/Asignatura/Nueva') + '#error')
    if opcion ==3:  #error de nrc
        redirect(url('/Asignatura/Nueva') + '#errornrc')
    
    return template('AsignaturaNueva')

#===========    Buscar    ===========
@route('/Profesor/Buscar')
def profesoresBuscar():
    return '<h1>Profesores Buscar Pagina!</h1>'

@route('/Asignatura/Buscar')
def asignaturaBuscar():
    return '<h1>Asginatura Buscar Paginaa!</h1>'

#===========   Rutas Estaticas   ===========
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename,root='./img')
@route('/staticjs/<filename>')
def server_static(filename):
    return static_file(filename,root='./js')
@route('/staticss/<filename>')
def server_static(filename):
    return static_file(filename,root='./css')


if __name__== '__main__':
    run(debug=True, reloader=True)