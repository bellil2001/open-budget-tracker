
from decimal import Decimal

from app.models.book import Book


class BookManager:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def create_book(self, name, currency, opening_balance="0"):
        name = name.strip()
        currency = currency.strip().upper()

        if not name:
            raise ValueError("Book name cannot be empty.")

        if not currency:
            raise ValueError("Currency cannot be empty.")

        balance = Decimal(str(opening_balance))

        if not balance.is_finite():
            raise ValueError("Opening balance must be finite.")

        book = Book(
            id=self.next_id,
            name=name,
            currency=currency,
            opening_balance=balance,
        )

        self.books.append(book)
        self.next_id += 1

        return book

    def get_all_books(self):
        return list(self.books)

    def get_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book

        return None