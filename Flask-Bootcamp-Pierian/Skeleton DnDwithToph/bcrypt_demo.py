from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecretpassword'

hashed_password = bcrypt.generate_password_hash(password=password)

check = bcrypt.check_password_hash(hashed_password, password)

print(check)