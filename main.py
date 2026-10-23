
from pathlib import Path
from decimal import Decimal

from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText

from app.theme import AppColors
from app.screens.dashboard import load_dashboard
from app.services.database import Database
from app.services.book_manager import BookManager


class BudgetTrackerApp(MDApp):

    def build(self):
        self.title = "Open Budget"
        self.colors = AppColors

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"

        # Permanent storage in application data folder
        db_path = Path(self.user_data_dir) / "budget.db"

        self.manager = BookManager(Database(db_path))
        self.active_book_id = None

        return load_dashboard()

    def on_start(self):
        self.refresh_dashboard()

    def create_book(self):
        ids = self.root.ids

        name = ids.book_name.text
        currency = ids.book_currency.text
        opening_balance = ids.opening_balance.text

        try:
            book = self.manager.create_book(
                name=name,
                currency=currency,
                opening_balance=opening_balance or "0"
            )
        except ValueError as error:
            ids.status_label.text = str(error)
            return

        self.active_book_id = book.id

        ids.book_name.text = ""
        ids.opening_balance.text = "0"
        ids.status_label.text = "Book created successfully!"

        self.refresh_dashboard()

    def select_book(self, book_id):
        self.active_book_id = book_id
        self.root.ids.status_label.text = ""
        self.refresh_dashboard()

    def refresh_dashboard(self):
        ids = self.root.ids
        books = [
            book for book in self.manager.get_all_books()
            if not self.is_archived(book.id)
        ]

        book_list = ids.book_list
        book_list.clear_widgets()

        for book in books:
            selected = book.id == self.active_book_id

            button = MDButton(
                style="filled" if selected else "tonal",
                size_hint_x=1,
            )

            label = MDButtonText(
                text=f"{book.name} ({book.currency})"
            )

            button.add_widget(label)

            button.bind(
                on_release=lambda instance, book_id=book.id:
                self.select_book(book_id)
            )

            book_list.add_widget(button)

        active = self.manager.get_book(
            self.active_book_id
        ) if self.active_book_id is not None else None

        if active is None and books:
            active = books[0]
            self.active_book_id = active.id

        if active:
            ids.current_book.text = active.display_name
            ids.balance_card.balance_text = (
                f"{active.opening_balance:,.3f} "
                f"{active.currency}"
            )
        else:
            ids.current_book.text = "Create your first book"
            ids.balance_card.balance_text = "0.000"

    def is_archived(self, book_id):
        for row in self.manager.database.get_all_books():
            if row["id"] == book_id:
                return bool(row["is_archived"])

        return False


if __name__ == "__main__":
    BudgetTrackerApp().run()