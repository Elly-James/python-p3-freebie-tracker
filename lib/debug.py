#!/usr/bin/env python3

# This file provides an interactive debugging environment to test the functionality of the application and interact with the database.
# Database Connection: Connects to the same SQLite database as seed.py.
# Interactive Debugging: Launches an ipdb interactive session where you can:
# Query the database to fetch records.
# Test relationships and methods defined in models.py.
# Experiment with the data seeded in seed.py.


# Relies on models.py to provide the schema and methods for database interaction.
# Works with the data seeded by seed.py for testing and debugging.



# Importing the create_engine function from SQLAlchemy.
# It is used to create a connection to a database.
from sqlalchemy import create_engine

# Importing the Company and Dev classes from the models module.
# These classes represent the tables in the database and are used to interact with the data.
from models import Company, Dev

# This ensures that this script runs only when executed directly.
# It prevents the code from running if the file is imported as a module in another script.
if __name__ == '__main__':


    # Creating a database engine for connecting to the SQLite database named 'freebies.db'.
    # If the database does not exist, it will be created automatically.
    engine = create_engine('sqlite:///freebies.db')

    # Importing the ipdb library for debugging.
    # ipdb.set_trace() sets a breakpoint, allowing one to interact with the program state.
    # You can inspect variables, run queries, and test code interactively at this point.
    import ipdb; ipdb.set_trace()
