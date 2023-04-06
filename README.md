# First-Project
**Library Terminal**
This is a Python program for managing a library system. It allows users to display all books, search for a book by title or author, check out a book, return a book, and process returns.

**How to Run Program** 
To use this program, simply run the main_menu() function in the code. This will display a menu with several options for interacting with the library system.

**Display Books**
Choosing the "Display all books" option will print out a list of all books in the library system. The user will then be prompted to check out a book.

**Search For a Book by Title or Author**
Choosing the "Search for a book by title" or "Search for a book by author" option will prompt the user to enter a keyword or author name, respectively. The program will then search the library system for any books that match the entered keyword or author name, and print out a list of any matching books.

**Check Out a Book**
Choosing the "Check out a book" option will prompt the user to enter the title of the book they wish to check out. The program will then check if the book is available, and if so, it will check out the book and print out the due date.

**Return a Book**
Choosing the "Return a book" option will prompt the user to enter the title of the book they wish to return. The program will then search for the book and mark it as returned.

**Process Returns**
Choosing the "Process returns" option will process all returned books that are waiting to be processed. If a book has been returned 10 times, it will be recycled. Otherwise, the book will be marked as "On Shelf" and returned to the library system.

**Book Class**
The Book class is used to create book objects with the following attributes:

* title: the title of the book
* author: the author of the book
* status: the status of the book, either "On Shelf", "Checked Out", or "Returned"
* condition: the condition of the book, on a scale of 1-10
* due_date: the due date for the book, if it has been checked out

![image](https://user-images.githubusercontent.com/125928129/229922077-b94ed488-7ec5-41d1-b35f-81cde1786e8f.png)

