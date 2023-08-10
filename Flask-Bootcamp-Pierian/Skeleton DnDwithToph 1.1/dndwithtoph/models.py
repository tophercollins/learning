# Import db from the project - DnDwithToph
from dndwithtoph import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# User class

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(64),unique = True,index = True)
    username = db.Column(db.String(64),unique = True,index = True)
    password_hash = db.Column(db.String(128))
    
    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Adventure class

class Adventure(db.Model):

    __tablename__ = 'adventures'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.Text)
    tagline = db.Column(db.Text)
    blurb = db.Column(db.Text)
    description = db.Column(db.Text)
    link = db.Column(db.Text)
    pictures = db.Column(db.Text)
    tier = db.Column(db.Integer)

    def __init__(self,title,tagline,blurb,description,link,picture,tier):
        self.title = title
        self.tagline = tagline
        self.blurb = blurb
        self.description = description
        self.link = link
        self.picture = picture
        self.tier = tier

    def __repr__(self):
        return f"{self.title} is a tier {self.tier} adventure."
    

# Testimonial class
    
class Testimonial(db.Model):

    __tablename__ = 'testimonials'

    id = db.Column(db.Integer,primary_key = True)
    person = db.Column(db.Text)
    quote = db.Column(db.Text)

    def __init__(self,person,quote):
        self.person = person
        self.quote = quote

    def __repr__(self):
        return f'{self.person} said: "{self.quote}"'
