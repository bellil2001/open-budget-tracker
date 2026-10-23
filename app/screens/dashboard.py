
from kivy.lang import Builder

from app.components.balance_card import BalanceCard


DASHBOARD_KV = """
MDScreen:
    md_bg_color: app.colors.BACKGROUND

    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "14dp"

        MDLabel:
            text: "Open Budget"
            font_style: "Headline"
            role: "medium"
            adaptive_height: True
            color: app.colors.TEXT_PRIMARY

        MDLabel:
            id: current_book
            text: "No book selected"
            adaptive_height: True

        BalanceCard:
            id: balance_card
            balance_text: "0.000 TND"

        MDLabel:
            text: "Your Books"
            adaptive_height: True
            font_style: "Title"
            role: "large"

        ScrollView:
            size_hint_y: 1

            MDBoxLayout:
                id: book_list
                orientation: "vertical"
                adaptive_height: True
                spacing: "8dp"

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
            hint_text: "Currency (TND, EUR, USD)"
            multiline: False
            size_hint_y: None
            height: "48dp"

        TextInput:
            id: opening_balance
            text: "0"
            hint_text: "Opening balance"
            multiline: False
            input_filter: "float"
            size_hint_y: None
            height: "48dp"

        MDLabel:
            id: status_label
            text: ""
            adaptive_height: True

        MDButton:
            style: "filled"
            pos_hint: {"center_x": 0.5}
            on_release: app.create_book()

            MDButtonText:
                text: "Create Book"
"""


def load_dashboard():
    return Builder.load_string(DASHBOARD_KV)