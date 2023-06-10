"""A Rolling Loud Munich organization library for visitors"""

__version__ = "0.2.4"
__authors__ = [
    "Tarek Al Ashraf",
    "Oktay Durururururururur",
    "Tom Plieninger",
    "Nico Peuser",
]

from rllib.artists import Artists
from rllib.app import App
from rllib.tickets import Tickets

if __name__ == "__main__":
    app = App()  # instantiates the App class
    app.textbox_1()  # creates textbox_1 "search your artist"
    app.textbox_2()  # creates textbox_2 result of search
    app.textbox_3()  # creates textbox_3 result of search
    app.textbox_4()  # creates textbox_4 result of search
    app.entry_1()  # creates entry_1 "Enter your search"
    app.go_button_1()  # creates go_button for Artist search
    app.go_button_2()  # creates go_button for Headliner search
    app.go_button_3()  # creates go_button for Time search
    app.quit_button()  # creates the quit_button widget
    app.combobox()  # creates a dropdown menu for the timespans
    app.find_perfect_ticket()  # creates method which has the command for toplevel window
    app.start()  # starts the main loop
