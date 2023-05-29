"""Modelling the GUI of the programm for a better user experience with the use of the popular third party library named Tkinter, aswell as customtkinter for a smoother design"""

from artists import Artists
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class App:
    """Class of the GUI, modelled with TKinter.
    The logic behind the widgets will be provided from the other classes."""

    def __init__(self):
        """Initiates the basic GUI basics to make this app usable.
        Basic are things like: title, geometry, resizable(bool), path to important images and the background label"""

        self.root = tk.Tk() #sets a new tk instance named root
        self.root.title("Rolling Loud Munich App") # changes the title
        self.root.geometry("482x603") # defines the size of the window
        self.root.resizable(False, False) # defones that you cant maximize the window
        
        #Loading the background  image
        bg_image = Image.open(r"RL-Library-Project\rllib\gui_stuff\rl_germany.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        
        logo_image = tk.PhotoImage(file=r"RL-Library-Project\rllib\gui_stuff\rl_logo.png") # file path for logo image
        self.root.iconphoto(True, logo_image) # changes the logo
        background_label = tk.Label(self.root, bg="black", image = bg_photo) # creates a label for our bg photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1) # places the label at x = 0, y = 0
        background_label.image = bg_photo  #Set the background label as the root window's background

    
    def start(self):
        """Methode for executing the code"""
        self.root.mainloop() #starts the loop
    
    def exit(self):
        """The logic behind the exit button"""
        self.root.quit()
        
        
    def quit_button(self):
        """The button element of the exit function"""
        exit_button = ctk.CTkButton(self.root, 
                    text="Exit",
                    width=40,
                    height=40,
                    corner_radius = 10,
                    fg_color = "#8912e6",
                    bg_color="#8912e6",
                    border_width	= 1,
                    border_color= "white",
                    text_color="white",
                    hover_color="#985adc",
                    command=exit
                    )
        exit_button.place(relx = 0.91 , rely= 0.005)


if __name__ == "__main__":
    app = App() #Add code to create widgets and configure the application logic
    app.quit_button() #calls the quit_button widget
    app.start() #calls the start loop
    
