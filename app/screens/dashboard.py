
from kivy.lang import Builder

# Register our reusable component
from app.components.balance_card import BalanceCard


DASHBOARD_KV = """
MDScreen:
    md_bg_color: app.colors.BACKGROUND

    MDBoxLayout:
        orientation: "vertical"
        spacing: "0dp"

        ScrollView:
            do_scroll_x: False

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: "20dp"
                spacing: "18dp"

                MDLabel:
                    text: "Open Budget"
                    font_style: "Headline"
                    role: "medium"
                    adaptive_height: True
                    color: app.colors.TEXT_PRIMARY

                MDButton:
                    style: "text"
                    on_release: app.toggle_books()

                    MDButtonText:
                        id: current_book
                        text: "Select a book"

                BalanceCard:
                    id: balance_card
                    balance_text: "0.000 TND"

                MDLabel:
                    text: "Your Books"
                    font_style: "Title"
                    role: "large"
                    adaptive_height: True

                MDBoxLayout:
                    id: books_section
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: "12dp"
                    size_hint_y: None
                    height: self.minimum_height if not self.disabled else 0
                    disabled: True
                    opacity: 0

                    MDBoxLayout:
                        id: book_list
                        orientation: "vertical"
                        adaptive_height: True
                        spacing: "8dp"

                    MDButton:
                        style: "tonal"
                        on_release: app.toggle_create_form()

                        MDButtonText:
                            text: "+ Create New Book"

                MDBoxLayout:
                    id: create_section
                    orientation: "vertical"
                    adaptive_height: True
                    spacing: "12dp"
                    opacity: 0
                    disabled: True
                    size_hint_y: None
                    height: 0
                    size_hint_y: None
                    height: self.minimum_height if not self.disabled else 0

                    MDLabel:
                        text: "Create New Book"
                        adaptive_height: True
                        font_style: "Title"
                        role: "medium"

                    TextInput:
                        id: book_name
                        hint_text: "Book name"
                        multiline: False
                        size_hint_y: None
                        height: "48dp"

                    TextInput:
                        id: book_currency
                        text: "TND"
                        hint_text: "Currency"
                        multiline: False
                        size_hint_y: None
                        height: "48dp"

                    TextInput:
                        id: opening_balance
                        text: "0"
                        hint_text: "Opening balance"
                        multiline: False
                        size_hint_y: None
                        height: "48dp"

                    MDLabel:
                        id: status_label
                        text: ""
                        adaptive_height: True

                    MDButton:
                        style: "filled"
                        on_release: app.create_book()

                        MDButtonText:
                            text: "Save Book"

        MDBoxLayout:
            size_hint_y: None
            height: "60dp"
            padding: "12dp"
            spacing: "8dp"
            md_bg_color: app.colors.SURFACE

            MDButton:
                style: "text"
                on_release: app.show_home()

                MDButtonText:
                    text: "Home"

            MDButton:
                style: "text"
                on_release: app.show_books()

                MDButtonText:
                    text: "Books"
"""


def load_dashboard():
    return Builder.load_string(DASHBOARD_KV)
