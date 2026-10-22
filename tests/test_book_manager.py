
from decimal import Decimal

from app.services.book_manager import BookManager


def test_create_books():
    manager = BookManager()

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

    assert personal.name == "Personal Budget"
    assert personal.opening_balance == Decimal("1000.000")

    assert travel.currency == "EUR"
    assert travel.opening_balance == Decimal("500.00")

    assert len(manager.get_all_books()) == 2

    assert manager.get_book(1) == personal
    assert manager.get_book(2) == travel
    assert manager.get_book(999) is None