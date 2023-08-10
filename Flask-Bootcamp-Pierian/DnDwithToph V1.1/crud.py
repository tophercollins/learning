from basic import db, Puppy, app
from sqlalchemy.orm import Session

session = Session()

with app.app_context():

    ## CREATE ##
    my_puppy = Puppy('Rufus', 5)
    db.session.add(my_puppy)
    db.session.commit()

    ## READ ##

    all_puppies = db.session.select()
    print(all_puppies)

    # SELECT BY ID

    puppy_one = db.select(1)
    print(puppy_one.name)

    # FILTERS

    puppy_frankie = db.select.filter_by(name='Frankie') 
    print(puppy_frankie.all())

    ## UPDATE ##

    first_puppy = db.select(1)
    first_puppy.age = 10
    db.session.add(first_puppy)
    db.session.commit()

    ## DELETE ##

    second_pup = session.get(2)
    db.session.delete(second_pup)
    db.session.commit()

    all_puppies = db.select.all() 
    print(all_puppies)

if __name__ == '__main__':
    app.run(debug=True)
