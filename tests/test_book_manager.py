
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


def test_update_book(manager):

    book = manager.create_book(
        "Old Name", "TND", "100"
    )

    result = manager.update_book(
        book.id, "New Name", "EUR"
    )

    assert result is True

    updated = manager.get_book(book.id)

    assert updated.name == "New Name"
    assert updated.currency == "EUR"


def test_archive_restore_book(manager):

    book = manager.create_book(
        "Savings", "EUR", "500"
    )

    assert manager.archive_book(book.id) is True

    archived = manager.database.get_all_books()
    assert archived[0]["is_archived"] == 1

    assert manager.restore_book(book.id) is True

    restored = manager.database.get_all_books()
    assert restored[0]["is_archived"] == 0


def test_delete_book(manager):

    book = manager.create_book(
        "Temporary", "USD", "100"
    )

    assert manager.delete_book(book.id) is True
    assert manager.get_book(book.id) is None


def test_nonexistent_book_operations(manager):

    assert manager.update_book(
        999, "Missing", "EUR"
    ) is False

    assert manager.archive_book(999) is False
    assert manager.restore_book(999) is False
    assert manager.delete_book(999) is False