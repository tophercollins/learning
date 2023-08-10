from sqlapp import app, db, Puppy

with app.app_context():

    ## CREATE ##
    my_puppy = Puppy('Rufus', 5)
    db.session.add(my_puppy)
    db.session.commit()

    ## READ ##

    all_puppies = db.session.query(Puppy).all() # List of all puppies in the table

    # Select by ID

    puppy_one = db.session.get(Puppy,1) # Selects the puppy with ID 1

    # Filters

    puppy_frankie = db.session.query(Puppy).filter(Puppy.name == 'Frankie').all() # Selects the puppy with name Frankie

    print(puppy_frankie)

    ## UPDATE ##

    first_puppy = db.session.get(Puppy,1) # Selects the puppy with ID 1
    first_puppy.age = 10 # Changes the age of the puppy with ID 1 to 10
    db.session.add(first_puppy) # Adds the puppy with ID 1 to the session
    db.session.commit() # Commits the changes to the database

    ## DELETE ##

    second_puppy = db.session.get(Puppy,2) # Selects the puppy with ID 2
    db.session.delete(second_puppy) # Deletes the puppy with ID 2
    db.session.commit() # Commits the changes to the database

    # Print all the puppies in the table

    all_puppies = db.session.query(Puppy).all() # List of all puppies in the table

    print(all_puppies)

    