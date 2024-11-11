"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Character,People,Planet,Starship
#from models import Person
import re
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex,email) is not None

@app.route('/user', methods=['POST'])
def register_user():
    user_data=  request.json

    errors={}

    if 'email'not in user_data or not is_valid_email(user_data['email']):
        errors['email']="El formato del email es invalido"
    if 'password' not in user_data or len(user_data['password'])<8:
        errors['password']="La contraseña no se ingreso o no tiene 8 caracteres"

    if errors:
        return jsonify({"errors",errors}),400

    password_hash= generate_password_hash(user_data['password'])

    new_user= User(email= user_data['email'],password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message":"Usuario registrado correctamente"}), 200

@app.route('/user', methods=['POST'])
def login_user():
    
    user_login=  request.json

    errors={}

    if 'email'not in user_login or not is_valid_email(user_login['email']):
        errors['email']="El formato del email es invalido"
    if 'password' not in user_login or len(user_login['password'])<8:
        errors['password']="La contraseña no se ingreso o no tiene 8 caracteres"

    if errors:
        return jsonify({"errors",errors}),400

    data_login= User.query.filter.by(email=user_login['email']).first()

    if data_login is None or not check_password_hash(data_login.password,user_login['password']):
        return jsonify({"message":"No se encuentra el usuario o el password es incorrecto"}),400
    
    return jsonify({"message":"Usuario registrado correctamente"}), 200
############################METHODS GET###############################################
@app.route('/people', methods=[GET,POST,PUT,DELETE])
def get_people():
   
    if request.method== 'GET':

        peoples=People.query.all()

        if peoples is None:
            return jsonify({"message":"lo siento, no sé encontro ningun personaje"}), 400
      
        people_list= [
                    {  
                        "name":people.name,
                        "url_img_people":People.url_img_people,
                        "force_syde":People.force_side
                    }for people in peoples
                 ]
        return jsonify({"peoples":people_list}),200 
    
    elif request.method== 'POST':

        data_people= request.json
        
        errors={}
        
        if data_people['name']  is None:
            errors['name']= "Debe ingresar un nombre"
        if data_people['url_image_people'] is None:
            errors['url_image_people'] = "Debe ingresar una url para obtener una imagen del personaje"   
        if data_people['description_people'] is None:
            errors['description_people'] ="Debe ingresar una descripcion para el personaje"
    
    elif request.method == 'PUT':
       data_people = request.json
       id_people = data_people.get('id')
       people_find= People.query.filter_by(id=id_people).first()

    if people_find is None:
        ({"message": "lo siento, no se encuentra el personaje al que quiere modificar"}),400

        errors={}

        if not data_people.get('name'):
            errors['name'] = " Debe ingresar un nombre válido"
        if data_people['url_image_people'] is None:
            errors['url_image_people'] = "Debe ingresar una url para obtener una imagen del personaje"
        if data_people['description_people'] is None:
            errors['description_people'] = " Debe ingresar una descripcion del personaje"
    
        if errors:
            return jsonify({"errors":errors})
    
        people_find.name= data_people['name']
        people_find.url_image_people= data_people['url_image_people']
        people_find.description_people= data_people['description_people']

        db.session.commit()

        return jsonify({
            "message": "personaje actualizado correctamente",
            "Personaje":{
                "name": people_find.name,
                "url_image_people": people_find.url_image_people,
                "description_people": people_find.description_people
            }
        }),200

    elif request.method == 'DELETE':   

        data_people= request.json
        id_people= data_people.get('id')
        people_remove= People.query.filter_by(id=id_people).first()

        if people_remove is None:
            return jsonify({"message": "El personaje que intenta eliminar, no se encuentra en nuestro sistema"}),400     

        db.session.delete(people_remove)
        db.session.commit()

        return jsonify({"message": "Personaje eliminado satisfactoriamente"}),200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
