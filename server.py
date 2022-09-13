from flask_crud import app
from flask_crud.controllers import paises, core, ciudades, direcciones
from flask import render_template
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

passw = "12345"
pass_hash = b'$2b$12$jAqb.yT8BNxCXu.wE3Zo7.0r.iZnBklMIfiiclAnRUCisBYO7qqGG'

print(bcrypt.generate_password_hash(passw, 12))

print(bcrypt.check_password_hash(pass_hash, passw))

if __name__ == "__main__":
    app.run(debug=True)