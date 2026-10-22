
from kivy.lang import Builder
from kivymd.uix.card import MDCard

from app.theme import AppColors


Builder.load_string("""
<BalanceCard>:
    style: "filled"
    theme_bg_color: "Custom"
    md_bg_color: app.colors.PRIMARY

    size_hint_y: None
    height: "170dp"
    padding: "20dp"
    radius: [20, 20, 20, 20]

    orientation: "vertical"
    spacing: "12dp"

    MDLabel:
        text: "Total Balance"
        adaptive_height: True
        theme_text_color: "Custom"
        text_color: app.colors.ON_PRIMARY

    MDLabel:
        text: root.balance_text
        font_style: "Headline"
        role: "large"
        adaptive_height: True
        theme_text_color: "Custom"
        text_color: app.colors.ON_PRIMARY

    MDLabel:
        text: "Your available money"
        adaptive_height: True
        theme_text_color: "Custom"
        text_color: app.colors.ON_PRIMARY
""")


class BalanceCard(MDCard):
    from kivy.properties import StringProperty

    balance_text = StringProperty("0.000 TND")