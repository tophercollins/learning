from sqlapp import app, db, Puppy

with app.app_context():

    ## READ ##

    all_puppies = db.session.query(Puppy).all() # List of all puppies in the table

    print(all_puppies)

    db.session.delete(all_puppies[-1]) # Deletes the first puppy in the table

    db.session.commit() # Commits the changes to the database

    print(all_puppies)