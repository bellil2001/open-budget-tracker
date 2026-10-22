
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Book:
    id: int
    name: str
    currency: str
    opening_balance: Decimal

    @property
    def display_name(self) -> str:
        return f"{self.name} ({self.currency})"
