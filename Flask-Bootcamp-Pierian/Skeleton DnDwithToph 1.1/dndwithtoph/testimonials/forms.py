from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

class AddForm(FlaskForm):
    person = StringField('Name:')
    quote = StringField('Quote:')
    submit = SubmitField('Add Testimonial')

class EditForm(FlaskForm):

    # Will need to add a select field to choose which testimonials to edit, for now just will use id input

    id = IntegerField('Testionial ID:')

    # Will also need form to auto update with current values of testionial of that testionial id

    person = StringField('Name:')
    quote = StringField('Quote:')
    submit = SubmitField('Edit Testimonial')
    submit2 = SubmitField('Delete Testimonial')