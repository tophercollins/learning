import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # This is for the migration of the database

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the application object

app = Flask(__name__)

# Configurations

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This is just to supress a warning message

db = SQLAlchemy(app)

Migrate(app, db)

class Puppy(db.Model):

    # Manually set the table name
    __tablename__ = 'puppies'

    # Create the columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
            
            # This is the string representation of a puppy in the model
            return "Puppy {0} is {1} year/s old {2}".format(self.name, self.age, self.breed)
    
