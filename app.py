# Import Models
from models import (Base, session,
                    Book, engine)

import datetime
import csv

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
def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return datetime.date(year, month, day)

def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)

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