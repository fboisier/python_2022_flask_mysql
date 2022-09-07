from flask_crud import app
from flask_crud.controllers import paises, core
from flask import render_template

if __name__ == "__main__":
    app.run(debug=True)