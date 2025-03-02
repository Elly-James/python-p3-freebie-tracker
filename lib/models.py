#The Models file
# defines the database schema and models for the application. It uses SQLAlchemy to create classes that represent database tables.
# Company: Represents a company with a name, founding year, and a relationship to Freebie and Dev.
# Dev: Represents a developer with a name and a relationship to Freebie and Company.
# Freebie: Represents an item given by a company to a developer, with attributes like item_name, value, and relationships to Dev and Company.

#Relationships:
# Defines how the models (Company, Dev, and Freebie) are connected through SQLAlchemy relationships. 
# For example, a Company can have many Freebie objects, and a Dev can own many Freebie objects.
# Methods:
# Provides methods for business logic, such as giving freebies (give_freebie), checking if a developer received an item (received_one), or transferring ownership of a freebie (give_away).

#The models.py file is imported in both seed.py and debug.py to access the database structure and manipulate data.
#Defines the foundational structure for the SQLite database used in the programme.






# again here starting with the imports

# Importing necessary functions and classes from SQLAlchemy:
# - ForeignKey: To define foreign key relationships between tables.
# - Column: To define columns in the database tables.
# - Integer and String: To specify the data types of table columns.
# - MetaData: To define metadata for the database, including naming conventions.

from sqlalchemy import ForeignKey, Column, Integer, String, MetaData

# Importing tools for ORM relationships:
# - relationship: To define relationships between tables.
# - backref: To create a reverse relationship that allows access from related objects.

from sqlalchemy.orm import relationship, backref

# Importing the base class generator for defining ORM models.
# declarative_base provides a foundation for creating ORM models (tables).

from sqlalchemy.ext.declarative import declarative_base

# Defining a naming convention for foreign keys in the database.
# This ensures consistent naming for constraints, improving database management.

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

# Creating the declarative base class with the defined metadata.
# All ORM models will inherit from this base class.

Base = declarative_base(metadata=metadata)

# Defining the Company class, representing the 'companies' table in the database.

class Company(Base):
    __tablename__ = 'companies'  # The name of the table in the database.

    # Defining columns in the 'companies' table:
    # - id: Primary key, unique identifier for each company.
    # - name: The company's name (string).
    # - founding_year: The year the company was founded (integer).

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    # Defining relationships:
    # - freebies: A one-to-many relationship with the Freebie table.
    #   The backref 'company' allows accessing the related Company object from a Freebie.
    # - devs: A many-to-many relationship with the Dev table via the Freebie table.
    #   The secondary argument 'freebies' specifies the association table between Dev and Freebie.
    #   The secondary argument 'companies' specifies the association table between Dev and Company.
    #   The cascade argument specifies how changes in the Freebie table will affect the related Dev and Company objects.


    freebies = relationship('Freebie', backref='company', cascade='all, delete-orphan')
    devs = relationship('Dev', secondary='freebies', back_populates='companies')

    # A method to create a new Freebie object for a given developer.
    def give_freebie(self, dev, item_name, value):
        return Freebie(item_name=item_name, value=value, dev=dev, company=self)

    # A class method to return the oldest company based on founding_year.
    # It uses a session query to fetch the first company ordered by founding_year.

    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()

    # A string representation of the Company object for debugging and display purposes.
    def __repr__(self):
        return f'<Company {self.name}>'

# Defining the Dev class, representing the 'devs' table in the database.
class Dev(Base):
    __tablename__ = 'devs'  # The name of the table in the database.

    # Defining columns in the 'devs' table:
    # - id: Primary key, unique identifier for each developer.
    # - name: The developer's name (string).

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    # Defining relationships:
    # - freebies: A one-to-many relationship with the Freebie table.
    # - companies: A many-to-many relationship with the Company table via the Freebie table.

    freebies = relationship('Freebie', backref='dev', cascade='all, delete-orphan')
    companies = relationship('Company', secondary='freebies', back_populates='devs')

    # A method to check if the developer has received a freebie with a specific item name.
    def received_one(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)

    # A method to transfer a freebie to another developer, if the freebie belongs to the current developer.
    def give_away(self, dev, freebie):
        if freebie in self.freebies:
            freebie.dev = dev

    # A string representation of the Dev object for debugging and display purposes.
    def __repr__(self):
        return f'<Dev {self.name}>'

# Defining the Freebie class, representing the 'freebies' table in the database.
class Freebie(Base):
    __tablename__ = 'freebies'  # The name of the table in the database.

    # Defining columns in the 'freebies' table:
    # - id: Primary key, unique identifier for each freebie.
    # - item_name: The name of the freebie item (string).
    # - value: The monetary value of the freebie (integer).
    # - dev_id: Foreign key referencing the id column in the 'devs' table.
    # - company_id: Foreign key referencing the id column in the 'companies' table.
    
    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))

    # A method to print details about the freebie, including the owner and the company.
    def print_details(self):
        return f'{self.dev.name} owns a {self.item_name} from {self.company.name}'

    # A string representation of the Freebie object for debugging and display purposes.
    def __repr__(self):
        return f'<Freebie {self.item_name} (Value: {self.value})>'
