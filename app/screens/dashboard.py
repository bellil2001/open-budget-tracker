
from kivy.lang import Builder

from app.components.balance_card import BalanceCard


DASHBOARD_KV = """
MDScreen:
    md_bg_color: app.colors.BACKGROUND

    MDBoxLayout:
        orientation: "vertical"

        # Main content
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

                # HOME VIEW
                MDBoxLayout:
                    id: home_view
                    orientation: "vertical"
                    spacing: "18dp"
                    size_hint_y: None
                    height: 0

                    MDButton:
                        style: "text"
                        on_release: app.show_books()

                        MDButtonText:
                            id: current_book
                            text: "Select a book"

                    BalanceCard:
                        id: balance_card
                        balance_text: "0.000 TND"

                    MDLabel:
                        text: "Recent activity"
                        font_style: "Title"
                        role: "large"
                        adaptive_height: True

                    MDCard:
                        style: "filled"
                        theme_bg_color: "Custom"
                        md_bg_color: app.colors.SURFACE
                        size_hint_y: None
                        height: "140dp"
                        radius: [20, 20, 20, 20]
                        padding: "16dp"

                        MDBoxLayout:
                            orientation: "vertical"
                            spacing: "8dp"

                            MDLabel:
                                text: "No transactions yet"
                                halign: "center"

                            MDLabel:
                                text: "Your activity will appear here"
                                halign: "center"

                # BOOKS VIEW
                MDBoxLayout:
                    id: books_view
                    orientation: "vertical"
                    spacing: "14dp"
                    opacity: 0
                    disabled: True
                    size_hint_y: None
                    height: 0

                    MDLabel:
                        text: "My Books"
                        font_style: "Title"
                        role: "large"
                        adaptive_height: True

                    MDLabel:
                        text: "Organize your money into books."
                        adaptive_height: True

                    MDBoxLayout:
                        id: book_list
                        orientation: "vertical"
                        adaptive_height: True
                        spacing: "10dp"

                    MDButton:
                        style: "filled"
                        on_release: app.toggle_create_form()

                        MDButtonText:
                            text: "+ Create New Book"

                    # CREATE FORM
                    MDBoxLayout:
                        id: create_section
                        orientation: "vertical"
                        spacing: "12dp"
                        opacity: 0
                        disabled: True
                        size_hint_y: None
                        height: 0

                        MDLabel:
                            text: "Create a financial book"
                            adaptive_height: True

                        MDTextField:
                            id: book_name
                            mode: "outlined"

                            MDTextFieldHintText:
                                text: "Book name"

                        MDTextField:
                            id: book_currency
                            mode: "outlined"
                            text: "TND"

                            MDTextFieldHintText:
                                text: "Currency (TND, EUR, USD)"

                        MDTextField:
                            id: opening_balance
                            mode: "outlined"
                            text: "0"

                            MDTextFieldHintText:
                                text: "Opening balance"

                        MDLabel:
                            id: status_label
                            text: ""
                            adaptive_height: True

                        MDButton:
                            style: "filled"
                            on_release: app.create_book()

                            MDButtonText:
                                text: "Save Book"

        # Bottom navigation
        MDBoxLayout:
            size_hint_y: None
            height: "72dp"
            padding: "12dp"
            spacing: "12dp"
            md_bg_color: app.colors.SURFACE

            MDButton:
                style: "text"
                size_hint_x: 0.5
                on_release: app.show_home()

                MDButtonText:
                    text: "Home"

            MDButton:
                style: "text"
                size_hint_x: 0.5
                on_release: app.show_books()

                MDButtonText:
                    text: "Books"
"""


def load_dashboard():
    return Builder.load_string(DASHBOARD_KV)
