"""Modelling the GUI of the programm for a better user experience with the use of the popular third party library named Tkinter, aswell as customtkinter for a smoother design"""

from artists import Artists
import tkinter as tk
from tkinter import StringVar
from tkinter import ttk
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

        self.output_artist_var = StringVar() #stets the StringVar in which we can store out output and print it later
        self.output_headliner_var = StringVar()
        self.time_var = StringVar()

        self.artists_instance = Artists()
    
#------------------------------GUI LOGIC AND FUNCTIONS---------------------------------------------#

    def start(self):
        """Methode for executing the code"""
        self.root.mainloop() #starts the loop
    
    def exit(self):
        """The logic behind the exit button"""
        self.root.quit()
    
    def go_button_artist(self):
        """The logic behind the GO button (artist search)."""
        current_entry = self.artist_entry.get() #if go is pressed, the current input is saved in current_entry
        for i in current_entry: #the entry gets deleted
            self.artist_entry.delete(0)
        #self.artists_instance = Artists() #instantiates the Artists class, yes not pretty but it works
        output = self.artists_instance.search_artist(user_input = current_entry) #executes the 'search_artists' method from Artists
        self.output_artist_var.set(output) # sets the output_var to the output (result of the search)

    def go_button_headliner(self):
        """The logic behind the GO button (headliner search)."""
        result = self.artists_instance.search_headliner()
        self.output_headliner_var.set(result)

    def go_button_time(self):
        """The logic behind the GO button (time search)."""

        current_time = self.combobox.get()
        for i in current_time: #the entry gets deleted
            self.artist_entry.delete(0)
        time = self.artists_instance.search_time(user_input=current_time)
        self.time_var.set(time)

#------------------------------GUI RANDOM---------------------------------------------#


    def quit_button(self):
        """The button element of the exit function
        Created with custom Tkinter"""
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

#------------------------------GUI SEARCH ARTIST---------------------------------------------#


    def textbox_1(self):
        """Shows what the user should input in the entry field below
        Created with custom Tkinter"""
        textbox = ctk.CTkTextbox(self.root,
                         width = 140,
                         height = 40,
                         corner_radius= 10,
                         border_width= 1,
                         border_color= "white",
                         fg_color= "#8b3ed7",
                         bg_color= "#8b3ed7",
                         text_color="white",
                         activate_scrollbars= False,
                         )
        textbox.place(relx = 0.1,rely= 0.18)
        textbox.insert("0.0", "Search your artist:")  # insert at line 0 character 0
        textbox.configure(state = "disabled") #makes the textbox read only

    def entry_1(self):
        """Entry field for the user. You can input the name of your desired artist
        Created with custom Tkinter"""
        self.artist_entry = ctk.CTkEntry(self.root, 
                     placeholder_text="Enter your search",
                     width = 180,
                     height= 40,
                     corner_radius = 10,
                     fg_color = "#8b3ed7",
                     bg_color="#8b3ed7",
                     border_width= 1,
                     border_color= "white",
                     text_color="white",
                     ) 
        self.artist_entry.place(relx = 0.41, rely = 0.18)

    def go_button_1(self):
        """The design of the GO button for the artist search, the logic can be found in the 'go_button_event'
        created with custom Tkinter"""
        go_button_1 = ctk.CTkButton(self.root, 
                       text="GO", 
                       width= 40,
                       height= 40,
                       corner_radius = 10,
                       fg_color = "#8b3ed7",
                       bg_color="#8b3ed7",
                       border_width= 1,
                       border_color= "white",
                       text_color="white",
                       hover_color="#8912e6",
                       command= self.go_button_artist
                       )
        go_button_1.place(relx = 0.8, rely = 0.18)

    def textbox_2(self):
        """Prints the results for of our artist search.
        Created with Tkinter becuase of the string var"""
        label = tk.Label(self.root, 
                         width=53,
                         height=2,
                         fg="white",
                         relief="ridge",
                         bg = "#a27de2",
                         anchor="w",
                         textvariable=self.output_artist_var
                        ) 
        label.place(relx= 0.1, rely= 0.26)

#------------------------------GUI SEARCH HEADLINER---------------------------------------------#

    def go_button_2(self):
        """The design of the GO button for the headliner search, the logic can be found in the 'go_button_headliner'
        created with custom Tkinter"""
        go_button = ctk.CTkButton(self.root, 
                       text="Headliner", 
                       width= 40,
                       height= 40,
                       corner_radius = 10,
                       fg_color = "#8b3ed7",
                       bg_color="#a27de2",
                       border_width= 1,
                       border_color= "white",
                       text_color="white",
                       hover_color="#8912e6",
                       command= self.go_button_headliner
                       )
        go_button.place(relx = 0.18, rely = 0.33)
    
    def textbox_4(self):
        """Prints the results for of our headliner search.
        Created with Tkinter because of the string var"""
        label = tk.Label(self.root, 
                         width=30,
                         height=4,
                         fg="white",
                         relief="ridge",
                         bg = "#a27de2",
                         anchor="w",
                         textvariable=self.output_headliner_var
                        ) 
        label.place(relx= 0.03, rely= 0.41)

#------------------------------GUI DATE/TIME STAGE---------------------------------------------#

    def combobox(self):
        self.combobox = ctk.CTkComboBox(self.root,
                                width=120,
                                height=40,
                                corner_radius= 10,
                                values = self.artists_instance.time,
                                bg_color="#9651db",
                                fg_color="#8b3ed7",
                                border_color="white",
                                border_width=1,
                                button_color="#8b3ed7",
                                button_hover_color="#8912e6",
                                dropdown_fg_color = "#8b3ed7",
                                dropdown_hover_color = "#8912e6",
                                state = "readonly",
                                variable= self.time_var
                                )
        self.combobox.place(relx= 0.55, rely = 0.33)

    def go_button_3(self):
        """The design of the GO button for the artist search, the logic can be found in the 'go_button_event'
        created with custom Tkinter"""
        go_button_2 = ctk.CTkButton(self.root, 
                       text="GO", 
                       width= 40,
                       height= 40,
                       corner_radius = 10,
                       fg_color = "#8b3ed7",
                       bg_color="#8b3ed7",
                       border_width= 1,
                       border_color= "white",
                       text_color="white",
                       hover_color="#8912e6",
                       command= self.go_button_time
                       )
        go_button_2.place(relx = 0.8, rely = 0.33)

    def textbox_5(self):
        """Prints the results for of our time search.
        Created with Tkinter because of the string var"""
        label = tk.Label(self.root, 
                         width=30,
                         height=7,
                         fg="white",
                         relief="ridge",
                         bg = "#a27de2",
                         anchor="w",
                         justify="left",
                         textvariable=self.time_var
                        ) 
        label.place(relx= 0.5, rely= 0.41)



if __name__ == "__main__":
    app = App() #Add code to create widgets and configure the application logic
    app.textbox_1() # creates textbox_1 "search your artist"
    app.textbox_2() #creates textbox_2 result of search
    app.textbox_4() #creates textbox_4 result of search
    app.textbox_5() #creates textbox_5 result of search
    app.entry_1() # creates entry_1 "Enter your search"
    app.go_button_1() # creates go_button for Artist search
    app.go_button_2() #creates go_button for Headliner search
    app.go_button_3() # creates go_button for Time search
    app.quit_button() #creates the quit_button widget
    app.combobox() # creates a dropdown menu for the timespans
    app.start() #starts the main loop
    
