
import sqlite3
from pathlib import Path


class Database:
    def __init__(self, db_path):
        self.db_path = Path(db_path)

    def initialize(self):
        # Create the database directory if necessary
        self.db_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with sqlite3.connect(self.db_path) as connection:
            connection.execute("PRAGMA foreign_keys = ON")

            connection.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    currency TEXT NOT NULL,
                    opening_balance TEXT NOT NULL DEFAULT '0',
                    is_archived INTEGER NOT NULL DEFAULT 0,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            connection.commit()

    
    def save_book(self, name, currency, opening_balance):
        # Validate book information
        name = name.strip()
        currency = currency.strip().upper()

        if not name:
            raise ValueError("Book name cannot be empty.")

        if not currency:
            raise ValueError("Currency cannot be empty.")

        # Store the book in SQLite
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.execute(
                """
                INSERT INTO books
                    (name, currency, opening_balance)
                VALUES (?, ?, ?)
                """,
                (name, currency, str(opening_balance))
            )

            connection.commit()

            return cursor.lastrowid

    
    def get_all_books(self):
        """Retrieve all financial books from SQLite."""

        with sqlite3.connect(self.db_path) as connection:
            connection.row_factory = sqlite3.Row

            cursor = connection.execute(
                """
                SELECT
                    id,
                    name,
                    currency,
                    opening_balance,
                    is_archived,
                    created_at
                FROM books
                ORDER BY id ASC
                """
            )

            return [
                dict(row)
                for row in cursor.fetchall()
            ]


            
