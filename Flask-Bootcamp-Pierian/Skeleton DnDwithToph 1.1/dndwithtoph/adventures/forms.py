from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField

class AddForm(FlaskForm):
    title = StringField('Title of Adventure:')
    tagline = StringField('Tagline:')
    blurb = TextAreaField('Blurb:')
    description = TextAreaField('Description:')
    link = StringField('Link:')
    picture = StringField('Picture:')
    tier = SelectField('Tier:', choices=[('1', 'Tier 1'), ('2', 'Tier 2'), ('3', 'Tier 3')])
    submit = SubmitField('Add Adventure')

class EditForm(FlaskForm):

    # Will need to add a select field to choose which adventure to edit, for now just will use id input

    id = IntegerField('Adventure ID:')

    # Will also need form to auto update with current values of adventure of that adventure id

    title = StringField('Title of Adventure:')
    tagline = StringField('Tagline:')
    blurb = TextAreaField('Blurb:')
    description = TextAreaField('Description:')
    link = StringField('Link:')
    picture = StringField('Picture:')
    tier = SelectField('Tier:', choices=[('1', 'Tier 1'), ('2', 'Tier 2'), ('3', 'Tier 3')])
    submit = SubmitField('Edit Adventure')
    submit2 = SubmitField('Delete Adventure')