from dndwithtoph import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique = True, index = True)
    profile_image = db.Column(db.String(64), nullable = False, default = 'default_profile.png')
    email = db.Column(db.String(64), unique = True, index = True)
    password_hash = db.Column(db.String(128))
    blog_posts = db.relationship('BlogPost', backref = 'author', lazy = True)
    # comments = db.relationship('Comment', backref = 'author', lazy = True)
    # monsters = db.relationship('Monster', backref = 'author', lazy = True)
    # items = db.relationship('Item', backref = 'author', lazy = True)
    # spells = db.relationship('Spell', backref = 'author', lazy = True)
    # cities = db.relationship('City', backref = 'author', lazy = True)
    # npcs = db.relationship('NPC', backref = 'author', lazy = True)
    # encounters = db.relationship('Encounter', backref = 'author', lazy = True)
    # adventures = db.relationship('Adventure', backref = 'author', lazy = True)
    # campaigns = db.relationship('Campaign', backref = 'author', lazy = True)
    # worlds = db.relationship('World', backref = 'author', lazy = True)
    # deities = db.relationship('Deity', backref = 'author', lazy = True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Username: {self.username}"
    
    
class BlogPost(db.Model):

    __tablename__ = 'blog_posts'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    title = db.Column(db.String(140), nullable = False)
    text = db.Column(db.Text, nullable = False)
    # comments = db.relationship('Comment', backref = 'blog_post', lazy = True)
    # image = db.Column(db.String(64), nullable = True)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} -- Title: {self.title}"