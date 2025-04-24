import os, argparse
parser = argparse.ArgumentParser()
parser.add_argument('--install', action=argparse.BooleanOptionalAction, default=False)
args = parser.parse_args()

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

if args.install:
    os.system("sudo apt update; sh feels_like_home.sh")
    
class Room_Of_Requirements(App):
    CSS_PATH = "style.tcss"

    # using the textual.app and textual.widgets, subdivide the page to give two widgets

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(id="navigations")
        yield Static("Xup", id="widget2")
        yield Footer()

    def on_mount(self) -> None:
        self.query_one("#navigations").update("Welcome to the Room of Requirements")
    
        
Room_Of_Requirements().run()
