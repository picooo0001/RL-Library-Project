"""Modelling the GUI of the app for a better user experience.
With the use of the popular third party library named Tkinter, aswell as customtkinter for a smoother design"""

from tickets import Tickets
from artists import Artists
import tkinter as tk
from tkinter import StringVar
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

class App:
    """Class of the GUI, modelled with TKinter.
    The design and logic behind the widgets is seperated in different methods most of the time"""

    def __init__(self):
        """Initializes the GUI basics to make this app usable.
        Basic are things like: instance, title, geometry, resizable(bool), path to important images, logo
        In this method, we also define all our StringVars and instances from other classes"""

        self.root = tk.Tk() #sets a new tk instance named root
        self.root.title("Rolling Loud Munich App") #changes the title
        self.root.geometry("482x603") #defines the size of the window
        self.root.resizable(False, False) #defines that you cant maximize the window
        
        #loads the background image
        bg_image = Image.open(r"RL-Library-Project\rllib\gui_stuff\rl_germany.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        
        logo_image = Image.open(r"RL-Library-Project\rllib\gui_stuff\rl_logo.png") #file path for logo image
        logo_width = 32
        logo_height = 32
        logo_image = logo_image.resize((logo_width, logo_height), Image.ANTIALIAS) #resizes the logo photo
        logo_image = ImageTk.PhotoImage(logo_image)
        self.root.iconphoto(True, logo_image) #changes the logo

        background_label = tk.Label(self.root, bg="black", image = bg_photo) #creates a label for our bg photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1) #places the label at x = 0, y = 0
        background_label.image = bg_photo  #sets the background label as the root window's background

        self.output_artist_var = StringVar() #creates a StringVar for the first search (artists)
        self.output_headliner_var = StringVar() #creates a StringVar for the second search (headliner)
        self.time_var = StringVar() #creates a StringVar for the third search (time)
        self.ticket_var = StringVar() #creates a StringVar for the first search in the toplevel window (ticket)

        self.day_check_var = ctk.StringVar(value="False") #creates more StringVars for all the different checkboxes in the toplevel window
        self.merch_check_var = ctk.StringVar(value="False")
        self.fastlane_check_var = ctk.StringVar(value="False")
        self.septoilets_check_var = ctk.StringVar(value="False")
        self.viparea_check_var = ctk.StringVar(value="False")
        self.below100_check_var = ctk.StringVar(value="False")
        self.below200_check_var = ctk.StringVar(value="False")
        self.below300_check_var = ctk.StringVar(value="False")

        self.artists_instance = Artists() #initializes Artists class
        self.tickets_instance = Tickets() #initializes Tickets class
    
#------------------------------GUI LOGIC AND FUNCTIONS---------------------------------------------#

    def start(self):
        """Method for executing the whole app"""
        self.root.mainloop() #starts the loop (indefinite time)
    
    def exit(self):
        """The logic behind the exit button"""
        self.root.destroy()
    
    def go_button_artist(self):
        """The logic behind the GO button (artist search)"""
        current_entry = self.artist_entry.get() #if go is pressed, the current input is saved in `current_entry`
        for i in current_entry: #the entry gets deleted
            self.artist_entry.delete(0)
        output = self.artists_instance.search_artist(user_input = current_entry) #executes the 'search_artists' method from Artists and saves the result in `output`
        self.output_artist_var.set(output) #sets the StringVar from above to `output` (result of the search)

    def go_button_headliner(self):
        """The logic behind the GO button (headliner search)"""
        result = self.artists_instance.search_headliner() #same thing as above
        self.output_headliner_var.set(result)

    def go_button_time(self):
        """The logic behind the GO button (time search)"""
        current_time = self.combobox.get() #same logic as above
        for i in current_time: 
            self.artist_entry.delete(0)
        time = self.artists_instance.search_time(user_input=current_time)
        self.time_var.set(time)

    def find_ticket_button(self):
        """The logic behind the SEARCH button (ticket search)"""
        single_day_bool = self.day_check_var.get() #when the search button (toplevel window) is pressed, this method gets if a checkbox is ticked or not
        incl_merch_bool = self.merch_check_var.get()
        fast_lane_bool = self.fastlane_check_var.get()
        sep_toilets_bool = self.septoilets_check_var.get()
        vip_area_bool = self.viparea_check_var.get()
        below_100_bool = self.below100_check_var.get()
        below_200_bool = self.below200_check_var.get()
        below_300_bool = self.below300_check_var.get()

        self.tickets_instance.catch_userinput( #this is the user input, f.e. True,False,True,...
            single_day_bool,
            incl_merch_bool,
            fast_lane_bool,
            sep_toilets_bool,
            vip_area_bool,
            below_100_bool,
            below_200_bool,
            below_300_bool
            )

        result = self.tickets_instance.search_tickets()
        self.ticket_var.set(result)      
        
#------------------------------GUI RANDOM---------------------------------------------#


    def quit_button(self): # design of the exit button
        """The button element of the exit function
        Created with custom Tkinter"""
        exit_button = ctk.CTkButton(self.root, #master
                    text="Exit",
                    width=40,
                    height=40,
                    corner_radius = 10, #round corner or not?
                    fg_color ="#8912e6",
                    bg_color="#8912e6",
                    border_width=1,
                    border_color= "white",
                    text_color="white",
                    hover_color="#985adc", #the color which appears if you hover over the button
                    command=exit
                    )
        exit_button.place(relx = 0.91 , rely= 0.005) #location of the element in GUI

    def find_perfect_ticket(self):
        """The button element of the find your perfect ticket buttton.
        Created with custom Tkinter"""
        suggest_button = ctk.CTkButton(self.root, 
                                       text="Find your perfect ticket",
                                       corner_radius=10,
                                       fg_color="#baa2dc",
                                       bg_color="#baa2dc",
                                       border_color="white",
                                       hover_color="#a27de2",
                                       command=self.second_window 
                                       )
        suggest_button.place(relx=0.13, rely= 0.55)

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
        textbox.insert("0.0", "Search your artist:")  #inserts text at line 0 character 0
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
        """The design of the GO button for the artist search, the logic can be found in the 'go_button_artists'
        Created with custom Tkinter"""
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
        """Prints the results of your artist search.
        Created with Tkinter"""
        label = tk.Label(self.root, 
                         width=53,
                         height=2,
                         fg="white",
                         relief="ridge",
                         bg = "#a27de2",
                         anchor="w",
                         textvariable=self.output_artist_var #StringVar
                        ) 
        label.place(relx= 0.1, rely= 0.26)

#------------------------------GUI SEARCH HEADLINER---------------------------------------------#

    def go_button_2(self):
        """The design of the GO button for the headliner search, the logic can be found in the 'go_button_headliner'
        Created with custom Tkinter"""
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
        Created with Tkinter"""
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

#------------------------------GUI TIME STAGE---------------------------------------------#

    def combobox(self):
        """Creates a combobox, where you can select the desired timespan.
        Created with custom Tkinter"""
        sorted_times = sorted(set(self.artists_instance.time))
        self.combobox = ctk.CTkComboBox(self.root,
                                width=120,
                                height=40,
                                corner_radius= 10,
                                values = sorted_times,
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
        """The design of the GO button for the time search, the logic can be found in the 'go_button_time'
        Created with custom Tkinter"""
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

    def textbox_3(self):
        """Prints the results for the selected timespan.
        Created with Tkinter"""
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

#------------------------------GUI TICKETS INFO---------------------------------------------#

    def second_window(self):
        """Creating a toplevel window, for the ticket selection. 
        This window is accessable through a button in the main window
        It is NOT devided in seperate metthods because this would not have worked out in the toplevel window (less features that in root window)"""
        self.second_window = tk.Toplevel(self.root) #creates a toplevel window
        self.second_window.title("Find your ticket") #gives it a title
        self.second_window.geometry("300x600") #sets geometry
        self.second_window.resizable(False, False) #not resizable
        toplevel_bg_image = Image.open(r"RL-Library-Project\rllib\gui_stuff\rl_germany.png")
        toplevel_bg_photo = ImageTk.PhotoImage(toplevel_bg_image)
        background_label = tk.Label(self.second_window, bg="black", image = toplevel_bg_photo) #creates a label for our bg photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1) #places the label at x = 0, y = 0
        background_label.image = toplevel_bg_photo  #sets the background label as the root window's background

        # 8 checkboxes will follow with the same structure, the only difference is the text and the textvariable (StringVar)
        day_checkbox = ctk.CTkCheckBox(self.second_window, 
                                   text="Single day?",
                                   height=40,
                                   border_color="white",
                                   border_width=1,
                                   bg_color="#8c40d7",
                                   fg_color="#8c42d7",
                                   hover_color="#a27de2",
                                   variable=self.day_check_var, 
                                   onvalue="True", 
                                   offvalue="False",
                                   corner_radius=10,
                                   )
        day_checkbox.place(relx= 0.1, rely=0.18)

        merch_checkbox = ctk.CTkCheckBox(self.second_window, 
                                   text= "Merch inclusive?",
                                   corner_radius=10,
                                   height=40,
                                   border_width=1,
                                   border_color="white",
                                   bg_color="#9559d9",
                                   fg_color="#9559d9",
                                   hover_color="#a27de2",
                                   variable=self.merch_check_var, 
                                   onvalue="True", 
                                   offvalue="False")
        merch_checkbox.place(relx= 0.1, rely=0.25)

        fastlane_checkbox = ctk.CTkCheckBox(self.second_window, 
                                   text="Fast lane?",
                                   corner_radius=10,
                                   height=40,
                                   border_width=1,
                                   border_color="white",
                                   bg_color="#9b69df",
                                   fg_color="#9b69df",
                                   hover_color="#a27de2",
                                   variable=self.fastlane_check_var, 
                                   onvalue="True", 
                                   offvalue="False")
        fastlane_checkbox.place(relx= 0.1, rely=0.32)

        septoilets_checkbox = ctk.CTkCheckBox(self.second_window, 
                                   text="Seperate toilets?",
                                   corner_radius=10,
                                   height=40,
                                   border_width=1,
                                   border_color="white",
                                   bg_color="#a884e3",
                                   fg_color="#a884e3",
                                   hover_color="#a27de2",
                                   variable=self.septoilets_check_var, 
                                   onvalue="True", 
                                   offvalue="False")
        septoilets_checkbox.place(relx= 0.1, rely=0.39)

        viparea_checkbox = ctk.CTkCheckBox(self.second_window, 
                                   text="Vip Area?",
                                   corner_radius=10,
                                   height=40,
                                   border_width=1,
                                   border_color="white",
                                   bg_color="#8c40d7",
                                   fg_color="#8c42d7",
                                   hover_color="#a27de2",
                                   variable=self.viparea_check_var, 
                                   onvalue="True", 
                                   offvalue="False")
        viparea_checkbox.place(relx= 0.6, rely=0.18)

        below100_checkbox = ctk.CTkCheckBox(self.second_window, 
                                   text="Below 100€?",
                                   corner_radius=10,
                                   height=40,
                                   border_width=1,
                                   border_color="white",
                                   bg_color="#9559d9",
                                   fg_color="#9559d9",
                                   hover_color="#a27de2",
                                   variable=self.below100_check_var, 
                                   onvalue="True", 
                                   offvalue="False")
        below100_checkbox.place(relx= 0.6, rely=0.25)

        below200_checkbox = ctk.CTkCheckBox(self.second_window, 
                                   text="Below 200€?",
                                   corner_radius=10,
                                   height=40,
                                   border_width=1,
                                   border_color="white",
                                   bg_color="#9b69df",
                                   fg_color="#9b69df",
                                   hover_color="#a27de2",
                                   variable=self.below200_check_var, 
                                   onvalue="True", 
                                   offvalue="False")
        below200_checkbox.place(relx= 0.6, rely=0.32)

        below300_checkbox = ctk.CTkCheckBox(self.second_window, 
                                   text="Below 300€?",
                                   corner_radius=10,
                                   height=40,
                                   border_width=1,
                                   border_color="white",
                                   bg_color="#a482e3",
                                   fg_color="#baa2da",
                                   hover_color="#a27de2",
                                   variable=self.below300_check_var, 
                                   onvalue="True", 
                                   offvalue="False")
        below300_checkbox.place(relx= 0.6, rely=0.39)

        #Button for the search
        search_button = ctk.CTkButton(self.second_window, 
                                      text="Search", 
                                      command=self.find_ticket_button,
                                      corner_radius=10,
                                      border_color="white",
                                      border_width=1,
                                      bg_color="#a380e3",
                                      fg_color="#baa2da",
                                      hover_color= "#a88ae3"
                                      )
        search_button.place(relx= 0.3, rely= 0.46)

        #Label which returns the result of the selection
        output_label = ctk.CTkLabel(self.second_window,
                                    textvariable = self.ticket_var,
                                    width = 250,
                                    height = 60,
                                    fg_color= "#b9a1db",
                                    bg_color= "#b9a1db",
                                    justify = "left",
                                    anchor="w",
                                    )
        output_label.place(relx=0.1, rely=0.53)
    
 