
from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDLabel:
        text: "Welcome to Open Budget Tracker"
        halign: "center"
        font_style: "Headline"
        role: "small"
"""


class BudgetTrackerApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)


if __name__ == "__main__":
    BudgetTrackerApp().run()