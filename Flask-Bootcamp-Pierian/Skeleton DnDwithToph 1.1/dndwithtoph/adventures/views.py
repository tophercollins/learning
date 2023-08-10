from flask import Blueprint, render_template, redirect, url_for
from dndwithtoph import db
from dndwithtoph.models import Adventure
from dndwithtoph.adventures.forms import AddForm, EditForm

adventures_blueprint = Blueprint('adventures', __name__, template_folder='templates/adventures')

@adventures_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        title = form.title.data
        tagline = form.tagline.data
        blurb = form.blurb.data
        description = form.description.data
        link = form.link.data
        picture = form.picture.data
        tier = form.tier.data
        # Add new Adventure to database
        new_adventure = Adventure(title, tagline, blurb, description, link, picture, tier)
        db.session.add(new_adventure)
        db.session.commit()

        return redirect(url_for('adventures.view'))
    return render_template('add.html', form=form)

@adventures_blueprint.route('/view')
def view():

    # Grab a list of Testimonials from database.
    adventures = Adventure.query.all()

    return render_template('view.html', adventures=adventures)

@adventures_blueprint.route('/edit', methods=['GET', 'POST'])
def edit():

    form = EditForm()

    if form.validate_on_submit():
        id = form.id.data
        title = form.title.data
        tagline = form.tagline.data
        blurb = form.blurb.data
        description = form.description.data
        link = form.link.data
        picture = form.picture.data
        tier = form.tier.data
        # Edit aT estimonial to database
        adventure = Adventure.query.get(id)
        adventure.title = title
        adventure.tagline = tagline
        adventure.blurb = blurb
        adventure.description = description
        adventure.link = link
        adventure.picture = picture
        adventure.tier = tier
        db.session.commit()
        
        return redirect(url_for('adventures.view'))
    return render_template('edit.html', form=form)
