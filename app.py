# Import Models
from models import (Base, session,
                    Book, engine)

# Main Menu - Add, Search, Analysis, Exit, View

# Add Books to the Database

# Edit Books

# Delete Books

# Search Books

# Data Cleaning

# Loop Runs Program

if __name__ == '__main__':
    Base.metadata.create_all(engine)