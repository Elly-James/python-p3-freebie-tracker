#!/usr/bin/env python3

# Script goes here!

# This file populates the database with initial data (seeding) for testing or development purposes.
# Database Connection: Establishes a connection to the SQLite database using SQLAlchemy.

# Data Creation:
# Creates instances of Company, Dev, and Freebie.
# Adds these instances to the database using the session.add_all() method.
# Data Persistence: Commits the changes to the database with session.commit().
# Console Output: Prints a success message to confirm that the database has been seeded.


# Imports the models from models.py to create and store data based on the defined schema.
#  seeded data can then be accessed and manipulated in debug.py.






# starting with the imports
# Importing the create_engine function from SQLAlchemy.
# This is used to connect to the database.

from sqlalchemy import create_engine

# Importing the sessionmaker class from SQLAlchemy.
# This is used to create a session, which is a connection to the database that allows you to query and modify data.

from sqlalchemy.orm import sessionmaker

# Importing the Base class and the Company, Dev, and Freebie models from the models module.
# - `Base` is the declarative base used for setting up the ORM models.
# - `Company`, `Dev`, and `Freebie` are the models representing the database tables.

from models import Base, Company, Dev, Freebie

# Creating a database engine to connect to the SQLite database named 'freebies.db'.
# If the database does not exist, it will be created automatically.

engine = create_engine('sqlite:///freebies.db')

# Creating a sessionmaker instance, which will bind sessions to the database engine.
# A session is required to interact with the database, such as querying or committing changes.

Session = sessionmaker(bind=engine)

# Creating a new session instance for interacting with the database.
session = Session()

# Creating all tables defined in the models using the Base metadata.
# If the tables already exist, this command will do nothing.

Base.metadata.create_all(engine)

# Creating instances of the Company class to represent companies in the database.
# These objects will later be added to the session and saved to the database.

company1 = Company(name="TechCorp", founding_year=2000)
company2 = Company(name="Innovate Inc.", founding_year=1995)

# Creating instances of the Dev class to represent developers in the database.
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

# Creating instances of the Freebie class to represent freebies and their relationships with developers and companies.
freebie1 = Freebie(item_name="T-Shirt", value=10, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Mug", value=5, dev=dev2, company=company1)
freebie3 = Freebie(item_name="Sticker", value=2, dev=dev1, company=company2)

# Adding all the created objects (companies, developers, freebies) to the session.
# This stages the objects to be saved to the database.
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])

# Committing the session to save the staged objects to the database.
session.commit()

# Printing a message to indicate that the database has been successfully seeded with initial data.
print("Database seeded successfully!")
