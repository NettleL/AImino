import customtkinter as ctk
import tkinter as tk
# A. ------
#Sets appearance of application
ctk.set_appearance_mode("System") 
#Sets widget colour
ctk.set_default_color_theme("blue")

# Create App class
class App(ctk.CTk):
# Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# Sets the title of our window to "App"
        self.title("App")    
# Dimensions of the window will be 200x200
        self.geometry("300x300")  
#column?
# Configure the grid layout
        self.grid_columnconfigure((0, 1), weight=1) # 2 Columns 
        self.grid_rowconfigure((0, 1, 2), weight=1) # 3 Rows
# Weight represents which is to be larger or smaller.
        self.label1 = ctk.CTkLabel(self, text="Yes")
        self.label1.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        
        self.Button1 = ctk.CTkButton(self,
                                         text="Button 1",
                                         command=self.button1
                                         )
        self.Button1.grid(row=0, column=1,
                                        padx=10, pady=10,
                                        sticky="ew")
        self.label2 = ctk.CTkLabel(self, text="Maybe")
        self.label2.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.Button2 = ctk.CTkButton(self,
                                         text="Button 2",
                                         command=self.button2
                                         )
        self.Button2.grid(row=1, column=1,
                                        padx=20, pady=20,
                                        sticky="ew"
                                        )
        self.label3 = ctk.CTkLabel(self, text="No")
        self.label3.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.Button3 = ctk.CTkButton(self,
                                         text="Button 3",
                                         command=self.button3)
        self.Button3.grid(row=2, column=1,
                                        padx=20, pady=20,
                                        sticky="ew"
                                        )
        
    def button1(self):
        print('Button 1 Clicked - Yes')
    def button2(self):
        print('Button 2 Clicked - Maybe')
    def button3(self):
        print('Button 3 Clicked - No')

if __name__ == "__main__":
    app = App()
    # Runs the app
    app.mainloop() 