# Import Models
from models import (Base, session,
                    Book, engine)

# Main Menu - Add, Search, Analysis, Exit, View
def menu():
    while True:
        print('''
            \nPROGRAMMING BOOKS
            \r1) Add Book
            \r2) View all Books
            \r3) Search for a Book
            \r4) Book Analysis
            \r5) Exit
        ''')
        choice = input('What would you like to do? ')
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            input('''
                \rPlease choose one of the options above.
                \rA number from 1-5.
                \rPress enter to try again.
            ''')

# Add Books to the Database

# Edit Books

# Delete Books

# Search Books

# Data Cleaning

# Loop Runs Program


def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # Add Book
            pass
        elif choice == '2':
            # View Books
            pass
        elif choice == '3':
            # Search for a Book
            pass
        elif choice == '4':
            # Analysis
            pass
        else:
            print('Goodbye')
            app_running = False

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()