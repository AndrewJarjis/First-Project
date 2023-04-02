from datetime import datetime, timedelta


class Book:
    def __init__(self, title, author, condition=10):
        self.title = title
        self.author = author
        self.status = 'On Shelf'
        self.condition = condition
        self.due_date = None

    def __str__(self):
        return f'{self.title} by {self.author} ({self.status})'

    def check_out(self):
        if self.status == 'Checked Out':
            print(f'The book "{self.title}" is already checked out.')
        else:
            self.status = 'Checked Out'
            self.due_date = datetime.today() + timedelta(days=14)
            self.condition -= 1
            print(f'The book "{self.title}" has been checked out.')

    def return_book(self):
        self.status = 'Returned'
        print(f'The book "{self.title}" has been returned.')


books = [
    Book('The Great Gatsby', 'F. Scott Fitzgerald'),
    Book('To Kill a Mockingbird', 'Harper Lee'),
    Book('1984', 'George Orwell'),
    Book('Pride and Prejudice', 'Jane Austen'),
    Book('The Catcher in the Rye', 'J.D. Salinger'),
    Book('One Hundred Years of Solitude', 'Gabriel Garcia Marquez'),
    Book('Brave New World', 'Aldous Huxley'),
    Book('Wuthering Heights', 'Emily Bronte'),
    Book('The Picture of Dorian Gray', 'Oscar Wilde'),
    Book('The Odyssey', 'Homer'),
    Book('The Divine Comedy', 'Dante Alighieri'),
    Book('Don Quixote', 'Miguel de Cervantes')
]

returned_books = []


def display_books():
    for book in books:
        print(book)


def search_by_author():
    author = input('Enter the name of the author: ')
    found_books = [book for book in books if book.author == author]
    if found_books:
        for book in found_books:
            print(book)
    else:
        print(f'No books by {author} found.')


def search_by_title():
    keyword = input('Enter a keyword from the title: ')
    found_books = [book for book in books if keyword.lower() in book.title.lower()]
    if found_books:
        for book in found_books:
            print(book)
    else:
        print(f'No books with "{keyword}" in the title found.')


def check_out_book():
    title = input('Enter the title of the book you would like to check out: ')
    found_book = None
    for book in books:
        if book.title == title:
            found_book = book
            break
    if found_book:
        found_book.check_out()
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
        found_book.return_book()
        returned_books.append(found_book)
        books.remove(found_book)
    else:
        print(f'The book "{title}" is not in our catalog.')


def process_returns():
    while returned_books:
        returned_book = returned_books.pop()
        if returned_book.condition < 5:
            print(f'The book "{returned_book.title}" has been recycled due to excessive wear and tear.')
        else:
            returned_book.status = 'On Shelf'


def main_menu():
    while True:
        print('Welcome to the library system!')
        print('Please choose an option from the following menu:')
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
        elif choice == '2':
            search_by_title()
        elif choice == '3':
            search_by_author()
        elif choice == '4':
            check_out_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            process_returns()
        elif choice == '0':
            print('Thank you for using the library system!')
            break
        else:
            print('Invalid choice. Please try again.')
main_menu()



