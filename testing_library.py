import unittest
from datetime import datetime, timedelta
import FirstProject


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = FirstProject.Book('The Great Gatsby', 'F. Scott Fitzgerald', 10)

    def test_init(self):
        self.assertEqual(self.book.title, 'The Great Gatsby')
        self.assertEqual(self.book.author, 'F. Scott Fitzgerald')
        self.assertEqual(self.book.status, 'On Shelf')
        self.assertEqual(self.book.condition, 10)
        self.assertIsNone(self.book.due_date)
        self.assertEqual(self.book.return_count, 0)

    def test_check_out(self):
        self.book.check_out()
        self.assertEqual(self.book.status, 'Checked Out')
        self.assertEqual(self.book.due_date, datetime.today() + timedelta(days=14))
        self.assertEqual(self.book.condition, 9)

    def test_check_out_already_checked_out(self):
        self.book.status = 'Checked Out'
        with self.assertRaisesRegex(ValueError, 'The book "The Great Gatsby" is already checked out.'):
            self.book.check_out()

    def test_return_book(self):
        self.book.status = 'Checked Out'
        self.book.return_book()
        self.assertEqual(self.book.status, 'Returned')

    def test_str(self):
        self.assertEqual(str(self.book), 'The Great Gatsby by F. Scott Fitzgerald (On Shelf)')


if __name__ == '__main__':
    unittest.main()
