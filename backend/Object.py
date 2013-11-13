from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from Design import *

# Creates a session to interact with the database
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

# Dummy data
user = []
user.append(User(first_name='Ed1', surname='Jones', password='edspassword', student=True, lecturer=False, tutor=False))
user.append(User(first_name='Ed2', surname='Jones', password='edspassword', student=True, lecturer=False, tutor=False))

# Commits dummy data to database
session.add_all(user)
session.commit()

# Test if data was inserted
our_user = session.query(User).filter_by(first_name='ed').first() 
our_user