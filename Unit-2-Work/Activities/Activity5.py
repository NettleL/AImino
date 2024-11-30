import customtkinter as ctk

# Set the appearance mode to "light"
ctk.set_appearance_mode("dark")
ctk.set_widget_scaling(2)  # widget dimensions and text size
ctk.set_window_scaling(2)  # window geometry dimensions

# Create the main application window
loginScreen = ctk.CTk()
loginScreen.title("Login Screen")
loginScreen.geometry("400x400")

#global username
#global password_entry
global password ## SECURITY RISK BUT I DON'T KNOW HOW TO DO IT
password = ''

def clicked9():
    global password
    password = password + '9'

def clicked8():
    global password
    password = password + '8'

def clicked7():
    global password
    password = password + '7'

def clicked6():
    global password
    password = password + '6'

def clicked5():
    global password
    password = password + '5'

def clicked4():
    global password
    password = password + '4'
    
def clicked3():
    global password
    password = password + '3'

def clicked2():
    global password
    password = password + '2'

def clicked1():
    global password
    password = password + '1'

def clicked0():
    global password
    password = password + '8'
    
    
loginScreen.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
loginScreen.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

# Create a label for the username
username_label = ctk.CTkLabel(master=loginScreen, text="Username")
username_label.grid(row=0, column=1, pady=12, padx=10, sticky="w")

# Create an entry for the username
username_entry = ctk.CTkEntry(master=loginScreen)
username_entry.grid(row=0, column=2, columnspan = 2, pady=12, padx=10)

# Create a label for the password
password_label = ctk.CTkLabel(master=loginScreen, text="Password")
password_label.grid(row=1, column=1, pady=12, padx=10, sticky="w")

# Create an entry for the password
password_entry = ctk.CTkEntry(master=loginScreen, show="●")
password_entry.grid(row=1, column=2,columnspan = 2, pady=12, padx=10)

Button9 = ctk.CTkButton(master=loginScreen, text="9", command=clicked9)
Button9.grid(row=2, column=1,padx=20, pady=20,sticky="ew")

Button8 = ctk.CTkButton(master=loginScreen, text="8", command=clicked8)
Button8.grid(row=2, column=2,padx=20, pady=20,sticky="ew")

Button7 = ctk.CTkButton(master=loginScreen, text="7", command=clicked7)
Button7.grid(row=2, column=3,padx=20, pady=20,sticky="ew")

Button6 = ctk.CTkButton(master=loginScreen, text="6", command=clicked6)
Button6.grid(row=3, column=1,padx=20, pady=20,sticky="ew")

Button5 = ctk.CTkButton(master=loginScreen, text="5", command=clicked5)
Button5.grid(row=3, column=2,padx=20, pady=20,sticky="ew")

Button4 = ctk.CTkButton(master=loginScreen, text="4", command=clicked4)
Button4.grid(row=3, column=3,padx=20, pady=20,sticky="ew")

Button3 = ctk.CTkButton(master=loginScreen, text="3", command=clicked3)
Button3.grid(row=4, column=1,padx=20, pady=20,sticky="ew")

Button2 = ctk.CTkButton(master=loginScreen, text="2", command=clicked2)
Button2.grid(row=4, column=2,padx=20, pady=20,sticky="ew")

Button1 = ctk.CTkButton(master=loginScreen, text="1", command=clicked1)
Button1.grid(row=4, column=3,padx=20, pady=20,sticky="ew")

Button0 = ctk.CTkButton(master=loginScreen, text="0", command=clicked0)
Button0.grid(row=5, column=2,padx=20, pady=20,sticky="ew")
    

    
# Define the login function
def login():
    username = username_entry.get()
    
    # Print the entered username and password to the console (for debugging purposes)
    print(f"Username: {username}\nPassword: {password}")
    
    # Destroy the login window and open the main menu
    #loginScreen.destroy()
    open_main_menu(username)
    
# Create a login button
login_button = ctk.CTkButton(master=loginScreen, text="Login", command=login)
login_button.grid(row=6, column=2, pady=12, padx=10)

# Function to open the main menu
def open_main_menu(username):
    main_menu = ctk.CTk()
    main_menu.title("Main Menu")
    main_menu.geometry("300x300")
    
    # Create grid to the main menu
    menu_frame = ctk.CTkFrame(master=main_menu)
    menu_frame.grid(row=0, column=0, pady=20, padx=60)

    # Adding label widgets
    welcome_label = ctk.CTkLabel(master=menu_frame, text="Welcome to the Main Menu")
    welcome_label.grid(row=0, column=0, pady=20, padx=10, columnspan=2)

    welcome_label = ctk.CTkLabel(master=menu_frame, text=username)
    welcome_label.grid(row=1, column=0, pady=20, padx=10, columnspan=2)

    # Add more widgets, such as a button to do stuff
    action_button = ctk.CTkButton(master=menu_frame, text="Do Something...or nothing")
    action_button.grid(row=2, column=0, pady=10, padx=10)

    # Add an exit button to close the application
    exit_button = ctk.CTkButton(master=menu_frame, text="Exit", command=main_menu.destroy)
    exit_button.grid(row=3, column=0, pady=10, padx=10)
    
    # Run the main menu window
    main_menu.mainloop()

# Run the application
loginScreen.mainloop()