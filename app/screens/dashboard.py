
from kivy.lang import Builder

# Import and register our reusable component
from app.components.balance_card import BalanceCard


DASHBOARD_KV = """
MDScreen:
    md_bg_color: app.colors.BACKGROUND

    MDBoxLayout:
        orientation: "vertical"
        padding: "20dp"
        spacing: "16dp"

        MDLabel:
            text: "My Budget"
            font_style: "Headline"
            role: "medium"
            adaptive_height: True
            theme_text_color: "Custom"
            text_color: app.colors.TEXT_PRIMARY

        MDLabel:
            text: "Manage your money easily"
            adaptive_height: True
            theme_text_color: "Custom"
            text_color: app.colors.TEXT_SECONDARY

        BalanceCard:
            balance_text: "2,450.000 TND"

        Widget:
"""


def load_dashboard():
    return Builder.load_string(DASHBOARD_KV)