import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from datetime import date
import time

colour_text = '#0B2027'
colour_button_1 = '#578783'
colour_button_2 = '#70A9A1'
colour_bg_dark = '#CFD7C7'
colour_bg_light = '#FCFAEE'

header_font = ("Helvetica", 20, "bold")
text_font = ("Helvetica", 16)
italic_font = ("Helvetica", 14, "italic")


class WelcomeScreen:
    def __init__(self, parent):
        self.parent = parent
        
        self.welcome_frame = ctk.CTkFrame(self.parent, fg_color=colour_bg_dark)
        self.welcome_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.welcome_frame.grid_rowconfigure((0, 2), weight=1, uniform="row")
        self.welcome_frame.grid_rowconfigure(1, weight=6, uniform="row")
        self.welcome_frame.grid_columnconfigure((0,2), weight=1, uniform="column")
        self.welcome_frame.grid_columnconfigure(1, weight=6, uniform="column")
    
        self.welcome_center_frame = ctk.CTkFrame(self.welcome_frame, fg_color=colour_bg_light)
        self.welcome_center_frame.grid(row=1, column=1, sticky="nsew")
        
        self.welcome_center_frame.grid_rowconfigure((0,1,2,3,4), weight=4)
        self.welcome_center_frame.grid_rowconfigure(2, weight=1)
        self.welcome_center_frame.grid_columnconfigure((0,1,2), weight=1)
        
        
        self.label = ctk.CTkLabel(self.welcome_center_frame, text="""TANEBASCON
The bank you can rely on""", font=italic_font)
        self.label.grid(row=2, column=1, sticky="n")
        
        self.label = ctk.CTkLabel(self.welcome_center_frame, text="Welcome to The Aquideck National Exchange Bank And Savings Company Of Newportlandia", font=text_font)
        self.label.grid(row=3, column=1, sticky="n")


        self.display_button = ctk.CTkButton(self.welcome_center_frame, text="START", fg_color=colour_button_1, hover_color=colour_button_2, command=self.show_main_menu)
        self.display_button.grid(row=4, column=1, padx=10, pady=10)

    def display(self):
        self.welcome_frame.lift()
        
    def show_main_menu(self):
        self.main_menu = MainMenu(self.parent)
        self.main_menu.display()
    
class MainMenu:
    def __init__(self, parent):
        self.parent = parent
       
        # Create the main menu frame but do not grid it yet
        self.main_menu_frame = ctk.CTkFrame(self.parent, fg_color=colour_bg_dark)
        self.main_menu_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        #self.main_menu_frame.grid(row=0, column=0, sticky="nsew")
    
        self.main_menu_frame.grid_rowconfigure((0, 2), weight=1, uniform="row")
        self.main_menu_frame.grid_rowconfigure(1, weight=6, uniform="row")
        self.main_menu_frame.grid_columnconfigure((0,2), weight=1, uniform="column")
        self.main_menu_frame.grid_columnconfigure(1, weight=6, uniform="column")
        
        self.main_menu_center_frame = ctk.CTkFrame(self.main_menu_frame, fg_color=colour_bg_light)
        self.main_menu_center_frame.grid(row=1, column=1, sticky="nsew")
        
        self.main_menu_center_frame.grid_rowconfigure((0,1,2,3), weight=1, uniform="row")
        self.main_menu_center_frame.grid_columnconfigure((0,1,2), weight=1, uniform="column")
        self.main_menu_center_frame.grid_propagate(False) 
        
        #self.label = ctk.CTkLabel(self.main_menu_center_frame, text="CHOOSE A TRANSACTION", font=header_font)
        #self.label.grid(row=0, column=0, columnspan=4)
    
        self.main_menu_button_frame = ctk.CTkFrame(self.main_menu_center_frame, fg_color=colour_bg_dark)
        self.main_menu_button_frame.grid(row=1, column=1)
        
        self.main_menu_button_frame.grid_rowconfigure((0,), weight=1, uniform="row")
        self.main_menu_button_frame.grid_columnconfigure(0, weight=1, uniform="column")   
        self.main_menu_button_frame.grid_propagate(False)    
        
        self.a = ctk.CTkFrame(self.main_menu_center_frame, fg_color="red")
        self.a.grid(row=1, column=2)
        
        self.b = ctk.CTkFrame(self.main_menu_center_frame, fg_color="orange")
        self.b.grid(row=1, column=3)
        
        self.c = ctk.CTkFrame(self.main_menu_center_frame, fg_color="yellow")
        self.c.grid(row=2, column=1)

        self.d = ctk.CTkFrame(self.main_menu_center_frame, fg_color="green")
        self.d.grid(row=2, column=2)
        
        self.e = ctk.CTkFrame(self.main_menu_center_frame, fg_color="blue")
        self.e.grid(row=2, column=3)
        
        self.f = ctk.CTkFrame(self.main_menu_center_frame, fg_color="purple")
        self.f.grid(row=3, column=1)
        
        self.g = ctk.CTkFrame(self.main_menu_center_frame, fg_color="pink")
        self.g.grid(row=3, column=2)

        self.h = ctk.CTkFrame(self.main_menu_center_frame, fg_color="gray")
        self.h.grid(row=3, column=3)
        
        self.i = ctk.CTkFrame(self.main_menu_center_frame, fg_color="yellow")
        self.i.grid(row=0, column=1)

        self.j = ctk.CTkFrame(self.main_menu_center_frame, fg_color="green")
        self.j.grid(row=0, column=2)
        
        self.k = ctk.CTkFrame(self.main_menu_center_frame, fg_color="blue")
        self.k.grid(row=0, column=3)
         
        
        # Main menu buttons
        self.button4 = ctk.CTkButton(self.main_menu_button_frame, text="Log Out", fg_color=colour_button_1, hover_color=colour_button_2, command=self.show_welcome)
        self.button4.grid(row=0, column=0, padx=20, pady=10)


    def display(self):
        # Show the main menu frame
        self.main_menu_frame.lift()
        
    def show_welcome(self):
        # Hide the center_frame and show the main_menu_frame
        self.welcome = WelcomeScreen(self.parent)
        self.welcome.display()
        

def main():
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    root._state_before_windows_set_titlebar_color = 'zoomed'
    # _------------------
    root.title("Screen")
       
        # Create the main frame that fills the whole window
    main_frame = ctk.CTkFrame(root, fg_color=colour_bg_light)
    main_frame.pack(fill=ctk.BOTH, expand=True)
    
    # _------------------

    app = WelcomeScreen(main_frame)

    root.mainloop()

if __name__ == "__main__":
    main()