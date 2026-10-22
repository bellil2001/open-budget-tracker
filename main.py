
from kivymd.app import MDApp

from app.screens.dashboard import load_dashboard
from app.theme import AppColors


class BudgetTrackerApp(MDApp):

    def build(self):
        self.title = "Open Budget"

        # Material Design theme
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.colors = AppColors

        # Load our dashboard
        return load_dashboard()


if __name__ == "__main__":
    BudgetTrackerApp().run()