import sqlite3

from app.services.database import Database


def test_database_initialization(tmp_path):
    # Create a temporary test database
    db_path = tmp_path / "test_budget.db"

    database = Database(db_path)
    database.initialize()

    # Verify that the database file exists
    assert db_path.exists()

    # Verify that the books table exists
    with sqlite3.connect(db_path) as connection:
        result = connection.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table' AND name = 'books'
            """
        ).fetchone()

        assert result is not None
        assert result[0] == "books"


def test_book_persistence(tmp_path):
    # Create a temporary database
    db_path = tmp_path / "budget.db"

    database = Database(db_path)
    database.initialize()

    # Save a financial book
    book_id = database.save_book(
        name="Personal Budget",
        currency="TND",
        opening_balance="1000.000"
    )

    # Check that an ID was generated
    assert book_id == 1

    # Close and reopen the database
    with sqlite3.connect(db_path) as connection:
        saved_book = connection.execute(
            """
            SELECT id, name, currency, opening_balance
            FROM books
            WHERE id = ?
            """,
            (book_id,)
        ).fetchone()

    # Verify that the information was saved
    assert saved_book is not None
    assert saved_book[0] == 1
    assert saved_book[1] == "Personal Budget"
    assert saved_book[2] == "TND"
    assert saved_book[3] == "1000.000"


def test_get_all_books(tmp_path):
    # Create a temporary database
    db_path = tmp_path / "budget.db"

    database = Database(db_path)
    database.initialize()

    # Create three different financial books
    database.save_book(
        name="Personal Budget",
        currency="TND",
        opening_balance="1000.000"
    )

    database.save_book(
        name="Travel Budget",
        currency="EUR",
        opening_balance="500.00"
    )

    database.save_book(
        name="Business Budget",
        currency="USD",
        opening_balance="2500.00"
    )

    # Create a new database object to simulate reopening
    reopened_database = Database(db_path)

    # Retrieve saved books
    books = reopened_database.get_all_books()

    # Check the number of books
    assert len(books) == 3

    # Check book names
    assert books[0]["name"] == "Personal Budget"
    assert books[1]["name"] == "Travel Budget"
    assert books[2]["name"] == "Business Budget"

    # Check currencies and opening balances
    assert books[0]["currency"] == "TND"
    assert books[0]["opening_balance"] == "1000.000"

    assert books[1]["currency"] == "EUR"
    assert books[1]["opening_balance"] == "500.00"

    assert books[2]["currency"] == "USD"
    assert books[2]["opening_balance"] == "2500.00"

    # Verify that each book has a unique ID
    assert len({book["id"] for book in books}) == 3
