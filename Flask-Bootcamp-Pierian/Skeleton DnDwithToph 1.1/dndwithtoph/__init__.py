import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)


# Configs

app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

Migrate(app,db)

# Login Configs

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Blueprints

from dndwithtoph.adventures.views import adventures_blueprint
from dndwithtoph.testimonials.views import testimonials_blueprint

app.register_blueprint(adventures_blueprint, url_prefix='/adventures/')
app.register_blueprint(testimonials_blueprint, url_prefix='/testimonials/')