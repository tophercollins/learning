from flask import Blueprint, render_template, redirect, url_for
from dndwithtoph import db
from dndwithtoph.models import Testimonial
from dndwithtoph.testimonials.forms import AddForm, EditForm

testimonials_blueprint = Blueprint('testimonials', __name__, template_folder='templates/testimonials')

@testimonials_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        person = form.person.data
        quote = form.quote.data
        # Add new Testimonial to database
        new_testimonial = Testimonial(person, quote)
        db.session.add(new_testimonial)
        db.session.commit()

        return redirect(url_for('testimonials.view'))
    return render_template('addt.html', form=form)

@testimonials_blueprint.route('/view')
def view():

    # Grab a list of Testimonials from database.
    testimonials = Testimonial.query.all()

    return render_template('viewt.html', testimonials=testimonials)

@testimonials_blueprint.route('/edit', methods=['GET', 'POST'])
def edit():

    form = EditForm()

    if form.validate_on_submit():
        id = form.id.data
        person = form.person.data
        quote = form.quote.data
        # Edit aT estimonial to database
        testimonial = Testimonial.query.get(id)
        testimonial.person = person
        testimonial.quote = quote
        db.session.commit()
        
        return redirect(url_for('testimonials.view'))
    return render_template('editt.html', form=form)

