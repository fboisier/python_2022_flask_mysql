from flask_crud import app
from flask_crud.models.pais import Pais
from flask_crud.models.ciudades import Ciudad
from flask import render_template, flash, redirect, request

@app.route("/ciudades")
def ciudades():
    return render_template("ciudades/ciudades.html", ciudades=Ciudad.get_all())

@app.route("/ciudades/crear")
def ciudades_agregar():
    return render_template("ciudades/ciudades_add.html", paises=Pais.get_all())   

@app.route("/ciudades/detalle/<id>")
def ciudades_detalle(id):

    return render_template("ciudades/ciudades_detalle.html", ciudad=Ciudad.get_by_id(id), paises=Pais.get_all())     

@app.route("/ciudades/agregar/procesar", methods=["POST"])
def ciudades_agregar_procesar():
    
    data = {
        'nombre' : request.form['nombre'],
        'pais_id' : request.form['pais_id'],
    }

    Ciudad.save(data)
    flash(f"Exito al agregar la ciudad {data['nombre']}","success")
    return redirect("/ciudades")

@app.route("/ciudades/eliminar/<id>")
def ciudades_eliminar_procesar(id):
    
    Ciudad.delete(id)

    flash(f"Exito al eliminar la ciudad","success")
    return redirect("/ciudades")    


@app.route("/ciudades/actualizar/<id>", methods=["POST"])
def ciudades_actualizar_procesar(id):
    
    data = {
        'nombre' : request.form['nombre'],
        'pais_id' : request.form['pais_id'],
        'id' : id
    }

    print("DATA----->>>>>>", data)

    resultado = Ciudad.update(data)
    if resultado == False:
        flash(f"Error al actualizar la ciudad {data['nombre']}","error")    
    else:
        flash(f"Exito al actualizar la ciudad {data['nombre']}","success")

    return redirect("/ciudades")    
