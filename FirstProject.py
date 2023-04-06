from datetime import datetime, timedelta


class Book:
    def __init__(self, title, author, condition):
        self.title = title
        self.author = author
        self.status = 'On Shelf'
        self.condition = condition
        self.due_date = None
        self.return_count = 0

    def __str__(self):
        return f'{self.title} by {self.author} ({self.status})'

    def check_out(self):
        if self.status == 'Checked Out':
            print(f'The book "{self.title}" is already checked out.')
        else:
            self.status = 'Checked Out'
            self.due_date = datetime.today() + timedelta(days=14)
            self.condition -= 1
            print(f'The book "{self.title}" has been checked out. It is due on {self.due_date.date()}')

    def return_book(self):
        self.status = 'Returned'
        print(f'The book "{self.title}" has been returned.')


books = [
    Book('The Great Gatsby', 'F. Scott Fitzgerald', 10),
    Book('To Kill a Mockingbird', 'Harper Lee', 10),
    Book('1984', 'George Orwell', 10),
    Book('Pride and Prejudice', 'Jane Austen', 5),
    Book('The Catcher in the Rye', 'J.D. Salinger', 7),
    Book('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 6),
    Book('Brave New World', 'Aldous Huxley', 5),
    Book('Wuthering Heights', 'Emily Bronte', 8),
    Book('The Picture of Dorian Gray', 'Oscar Wilde', 9),
    Book('The Odyssey', 'Homer', 10),
    Book('The Divine Comedy', 'Dante Alighieri', 10),
    Book('Don Quixote', 'Miguel de Cervantes', 10)
]

returned_books = []
checked_out_books = []


def display_books():
    all_books = books + returned_books
    for i, book in enumerate(all_books):
        print(i + 1, book)


def search_by_author():
    found_author = False
    while not found_author:
        author = input('Enter the name of the author: ')
        found_books = [book for book in books if book.author == author]
        if found_books:
            for book in found_books:
                print(book)
            found_author = True
        else:
            print(f'No books by {author} found.')


def search_by_title():
    found_title = False
    while not found_title:
        keyword = input('Enter a keyword from the title: ')
        found_books = [book for book in books if keyword.lower() in book.title.lower()]
        if found_books:
            for book in found_books:
                print(book)
            found_title = True
        else:
            print(f'No books with "{keyword}" in the title found.')


def check_out_book():
    book_checked = False
    while not book_checked:
        title = input('Enter the title of the book you would like to check out: ')
        found_book = None
        for book in books:
            if book.title == title:
                found_book = book
                break
        if found_book:
            found_book.check_out()
            checked_out_books.append(found_book)
            book_checked = True
        else:
            print(f'The book "{title}" is not in our catalog.')


def return_book():
    title = input('Enter the title of the book you are returning: ')
    found_book = None
    for book in books:
        if book.title == title:
            found_book = book
            break
    if found_book:
        if found_book.status == 'Checked Out':
            found_book.return_book()
            returned_books.append(found_book)
            found_book.status = 'On Shelf'
            print('Return to the main menu to process book return.')
        else:
            print(f'The book "{title}" has not been checked out and cannot be returned.')
    else:
        print(f'The book "{title}" is not in our catalog.')


def process_returns():
    while returned_books:
        returned_book = returned_books.pop()
        if returned_book.condition < 1:
            print(f'The book "{returned_book.title}" has been recycled due to excessive wear and tear.')
            books.remove(returned_book)
        else:
            returned_book.status = 'On Shelf'
            print(
                f'The book "{returned_book.title}" is now back on the shelf. Current condition: {returned_book.condition}/10')

def main_menu():
    while True:
        print('1. Display all books')
        print('2. Search for a book by title')
        print('3. Search for a book by author')
        print('4. Check out a book')
        print('5. Return a book')
        print('6. Process returns')
        print('0. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            display_books()
            if check_out_prompt():
                check_out_book()
        elif choice == '2':
            search_by_title()
            if check_out_prompt():
                check_out_book()
        elif choice == '3':
            search_by_author()
            if check_out_prompt():
                check_out_book()
        elif choice == '4':
            check_out_book()
        elif choice == '5':
            return_book()
            continue
        elif choice == '6':
            process_returns()
        elif choice == '0':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 6 or 0 to exit.')

        go_to_main_menu()


def check_out_prompt():
    while True:
        response = input('Would you like to check out a book? (y or n) ').lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print('Invalid answer. You can only enter y or n.')


def go_to_main_menu():
    while True:
        response = input('Would you like to go back to the main menu? (y or n) ').lower()
        if response == 'y':
            break
        elif response == 'n':
            print('Goodbye!')
            exit()
        else:
            print('Invalid answer. You can only enter y or n.')


print('Welcome to the Library System')
print('Please choose an option from the following menu: ')
main_menu()
