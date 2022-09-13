from flask_crud import app
from flask_crud.models.ciudades import Ciudad
from flask_crud.models.direcciones import Direccion
from flask import render_template, flash, redirect, request
from flask_crud.models.tipodirecciones import TipoDireccion

@app.route("/direcciones")
def direcciones():
    return render_template("direcciones/direcciones.html", direcciones=Direccion.get_all())

@app.route("/direcciones/crear")
def direcciones_agregar():
    return render_template("direcciones/direcciones_add.html", ciudades=Ciudad.get_all(), tipos=TipoDireccion.get_all())   

@app.route("/direcciones/detalle/<id>")
def direcciones_detalle(id):

    return render_template("direcciones/direcciones_detalle.html", direccion=Direccion.get_by_id(id),  ciudades=Ciudad.get_all(), tipos=TipoDireccion.get_all())     

@app.route("/direcciones/agregar/procesar", methods=["POST"])
def direcciones_agregar_procesar():
    
    data = {
        'nombre' : request.form['nombre'],
        'numero' : request.form['numero'],
        'ciudad_id' : request.form['ciudad_id'],
        'tipodireccion_id' : request.form['tipodireccion_id'],
    }

    Direccion.save(data)
    flash(f"Exito al agregar la dirección {data['nombre']}","success")
    return redirect("/direcciones")

@app.route("/direcciones/eliminar/<id>")
def direcciones_eliminar_procesar(id):
    
    Direccion.delete(id)

    flash(f"Exito al eliminar la dirección","success")
    return redirect("/direcciones")    


@app.route("/direcciones/actualizar/<id>", methods=["POST"])
def direcciones_actualizar_procesar(id):
    
    data = {
        'nombre' : request.form['nombre'],
        'numero' : request.form['numero'],
        'ciudad_id' : request.form['ciudad_id'],
        'tipodireccion_id' : request.form['tipodireccion_id'],
        'id' : id
    }

    print("DATA----->>>>>>", data)

    resultado = Direccion.update(data)
    if resultado == False:
        flash(f"Error al actualizar la dirección {data['nombre']}","error")    
    else:
        flash(f"Exito al actualizar la dirección {data['nombre']}","success")

    return redirect("/direcciones")    
