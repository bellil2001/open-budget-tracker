
from decimal import Decimal, InvalidOperation

from app.models.book import Book
from app.services.database import Database


class BookManager:
    def __init__(self, database: Database):
        self.database = database
        self.database.initialize()

    def create_book(
        self,
        name: str,
        currency: str,
        opening_balance="0"
    ) -> Book:

        name = name.strip()
        currency = currency.strip().upper()

        if not name:
            raise ValueError("Book name cannot be empty.")

        if len(currency) != 3 or not currency.isalpha():
            raise ValueError(
                "Currency must be a 3-letter code."
            )

        try:
            balance = Decimal(str(opening_balance))
        except (InvalidOperation, ValueError):
            raise ValueError(
                "Invalid opening balance."
            ) from None

        if not balance.is_finite():
            raise ValueError(
                "Opening balance must be finite."
            )

        book_id = self.database.save_book(
            name=name,
            currency=currency,
            opening_balance=balance
        )

        return Book(
            id=book_id,
            name=name,
            currency=currency,
            opening_balance=balance
        )

    def get_all_books(self) -> list[Book]:

        rows = self.database.get_all_books()

        return [
            Book(
                id=row["id"],
                name=row["name"],
                currency=row["currency"],
                opening_balance=Decimal(
                    row["opening_balance"]
                )
            )
            for row in rows
        ]

    def get_book(self, book_id: int):

        for book in self.get_all_books():
            if book.id == book_id:
                return book

        return None
    
    
    def update_book(self, book_id, name, currency):

        name = name.strip()
        currency = currency.strip().upper()

        if not name:
            raise ValueError("Book name cannot be empty.")

        if len(currency) != 3 or not currency.isalpha():
            raise ValueError("Invalid currency code.")

        return self.database.update_book(
            book_id, name, currency
        )

    def archive_book(self, book_id):
        return self.database.set_book_archived(
            book_id, True
        )

    def restore_book(self, book_id):
        return self.database.set_book_archived(
            book_id, False
        )

    def delete_book(self, book_id):
        return self.database.delete_book(book_id)
    
    
    def rename_book(self, book_id: int, new_name: str):
        """Rename a book without changing its currency."""

        book = self.get_book(book_id)

        if book is None:
            return False

        new_name = new_name.strip()

        if not new_name:
            raise ValueError("Book name cannot be empty.")

        return self.database.update_book(
            book_id,
            new_name,
            book.currency
        )


