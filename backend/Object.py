from sqlalchemy.orm import sessionmaker

import Design

# Creates a session to interact with the database
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

# Dummy data
user[0] = User(name='student', fullname='Ed Jones', password='edspassword')
user[1] = User(name='student', fullname='Ed Jones', password='edspassword')

# Commits dummy data to database
session.add(user[0]) # session.add_all(user) # TODO: test
session.commit()

# Test if data was inserted
our_user = session.query(User).filter_by(name='ed').first() 
our_user