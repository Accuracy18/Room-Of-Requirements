from textual.app import App
from textual.widgets import Header, Footer, Static

class Room_Of_Requirements(App):
    CSS_PATH = "style.tcss"  # Optional CSS file

    def compose(self):
        yield Header("My Textual App")
        yield Static("Hello, Textual!", id="greeting")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#greeting").update("Welcome to the TUI world!")

Room_Of_Requirements().run()
