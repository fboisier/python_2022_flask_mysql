from flask import Flask, render_template, flash, redirect, request
from pais import Pais
app = Flask(__name__)
app.secret_key = 'loquesea'



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/paises")
def paises():
    return render_template("paises.html", paises=Pais.get_all())

@app.route("/paises/detalle/<id>")
def paises_detalle(id):

    return render_template("paises_detalle.html", pais=Pais.get_by_id(id))

@app.route("/paises/crear")
def paises_agregar():
    return render_template("paises_add.html")

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

if __name__ == "__main__":
    app.run(debug=True)


