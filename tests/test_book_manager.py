
from decimal import Decimal

import pytest

from app.services.database import Database
from app.services.book_manager import BookManager


@pytest.fixture
def manager(tmp_path):
    database = Database(tmp_path / "budget.db")
    return BookManager(database)


def test_create_books(manager):

    personal = manager.create_book(
        name="Personal Budget",
        currency="TND",
        opening_balance="1000.000"
    )

    travel = manager.create_book(
        name="Travel Budget",
        currency="EUR",
        opening_balance="500.00"
    )

    assert personal.id == 1
    assert travel.id == 2

    assert len(manager.get_all_books()) == 2

    assert personal.opening_balance == Decimal(
        "1000.000"
    )

    assert travel.currency == "EUR"


def test_get_book(manager):

    book = manager.create_book(
        "Business",
        "USD",
        "2500.00"
    )

    saved_book = manager.get_book(book.id)

    assert saved_book is not None
    assert saved_book.name == "Business"
    assert saved_book.currency == "USD"

    assert manager.get_book(999) is None


def test_book_survives_restart(tmp_path):

    db_path = tmp_path / "persistent.db"

    first_manager = BookManager(Database(db_path))

    created = first_manager.create_book(
        "Savings",
        "EUR",
        "1500.00"
    )

    # Simulate restarting the application
    second_manager = BookManager(Database(db_path))

    restored = second_manager.get_book(created.id)

    assert restored is not None
    assert restored.name == "Savings"
    assert restored.opening_balance == Decimal(
        "1500.00"
    )


def test_invalid_books(manager):

    with pytest.raises(ValueError):
        manager.create_book("", "TND", "100")

    with pytest.raises(ValueError):
        manager.create_book("Test", "EU", "100")

    with pytest.raises(ValueError):
        manager.create_book("Test", "EUR", "abc")

    with pytest.raises(ValueError):
        manager.create_book("Test", "EUR", "NaN")