# Import db from the project - DnDwithToph
from dndwithtoph import db

# Create a class for each table in the database
# Currently base needs of the website, but later on we can add more tables
# Specifically the for users



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
