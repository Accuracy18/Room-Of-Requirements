import os, argparse
parser = argparse.ArgumentParser()
parser.add_argument('--install', action=argparse.BooleanOptionalAction, default=False)
args = parser.parse_args()

from textual.app import App
from textual.widgets import Header, Footer, Static

if args.install:
    os.system("sudo apt update; sh feels_like_home.sh")
    
class Room_Of_Requirements(App):
    CSS_PATH = "style.tcss"  # Optional CSS file

    def compose(self):
        yield Header("My Textual App")
        yield Static("Hello, Textual!", id="greeting")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#greeting").update("Welcome to the TUI world!")

Room_Of_Requirements().run()
