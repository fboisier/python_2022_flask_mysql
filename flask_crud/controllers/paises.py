from flask_crud import app
from flask_crud.models.pais import Pais
from flask import render_template, flash, redirect, request


@app.route("/paises")
def paises():
    return render_template("paises/paises.html", paises=Pais.get_all())

@app.route("/paises/detalle/<id>")
def paises_detalle(id):

    return render_template("paises/paises_detalle.html", pais=Pais.get_by_id(id))

@app.route("/paises/crear")
def paises_agregar():
    return render_template("paises/paises_add.html")

@app.route("/paises/agregar/procesar", methods=["POST"])
def paises_agregar_procesar():
    
    data = {
        'id' : request.form['id'],
        'nombre' : request.form['nombre'],
    }

    Pais.save(data)
    flash(f"Exito al agregar el pais {data['nombre']}","success")
    return redirect("/paises")

@app.route("/paises/actualizar/<id>", methods=["POST"])
def paises_actualizar_procesar(id):
    
    data = {
        'nombre' : request.form['nombre'],
        'id' : id
    }

    Pais.update(data)

    flash(f"Exito al actualizar el pais {data['nombre']}","success")
    return redirect("/paises")    

@app.route("/paises/eliminar/<id>")
def paises_eliminar_procesar(id):
    
    Pais.delete(id)

    flash(f"Exito al eliminar el pais","success")
    return redirect("/paises")    
