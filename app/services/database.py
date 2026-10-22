
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
