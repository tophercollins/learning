from sqlapp import app, db, Puppy

with app.app_context():



    db.create_all() # Creates all the tables modelled in the database

    sam = Puppy('Sammy', 3)
    frank = Puppy('Frankie', 4)

    db.session.add_all([sam, frank])

    db.session.commit()

    print(sam)
    print(frank)