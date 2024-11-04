from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email, self.is_active

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_people = db.Column(db.Integer, unique=True, nullable=False)
    id_planet = db.Column(db.Integer, unique=True, nullable=False)
    id_starship = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<Character %r>' % self.id, self.id_people,self.id_planet,self.id_starship

    def serialize(self):
        return {
            "id": self.id,
            "id_character": self.id_character,
            "id_people": self.id_people,
            "id_planet": self.id_planet,
            "id_starship": self.id_starship,

            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    name= db.Column(db.String(30),nullable=False)
    url_img_people= db.Column(db.String(200),nullable=False)
    description_people= db.Column(db.String(1000),nullable=False)
    film_people=db.Column(db.String(500),nullable=False)
    url_img_starship_people= db.Column(db.String(200),nullable=False)
    force_side = db.Column(db.String(20), unique=True, nullable=False)
    type_warrior = db.Column(db.Integer, unique=True, nullable=False)
    parents = db.Column(db.Boolean(), unique=True, nullable=False)
    teacher = db.Column(db.Boolean(), unique=True, nullable=False)
    age = db.Column(db.Integer, unique=True, nullable=False)
    
    
    def __repr__(self):
        return '<People %r>' % self.id, self.name,

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url_img_people": self.url_img_people,
            "description_people": self.description_people,
            "film_people": self.film_people,
            "url_img_starship_people": self.url_img_starship_people,
            "force_side": self.force_side,
            "type_warrior": self.type_warrior,
            "parents": self.parents,
            "teacher": self.teacher,
            "age": self.age,

            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    url_planet = db.Column(db.String(200), nullable=False)
    description_planet=db.Column(db.String(1000),nullable=False)
    climate= db.Column(db.String(50),nullable=False)
    population = db.Column(db.Integer, nullable=False)
    diameter = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.id,self.name 

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url_planet": self.url_planet,
            "description_planet": self.description_planet,
            "climate": self.climate,
            "population": self.population,
            "diameter": self.diameter,
            # do not serialize the password, its a security breach
        }

class Starship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True, nullable=False)
    url_starship = db.Column(db.Integer, unique=True, nullable=False)
    description_starship = db.Column(db.Boolean(), unique=True, nullable=False)
    model = db.Column(db.String(50), nullable=False)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)

    
    def __repr__(self):
        return '<Starship %r>' % self.id, self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url_starship": self.url_starship,
            "description_starship": self.description_starship,
            "model": self.model,
            "cargo_capacity": self.cargo_capacity,
            "speed": self.speed,
            # do not serialize the password, its a security breach
        }