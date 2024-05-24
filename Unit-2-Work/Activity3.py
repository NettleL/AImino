#https://www.geeksforgeeks.org/build-a-basic-form-gui-using-customtkinter-module-in-python/
# Python program to create a basic form 
# GUI application using the customtkinter module
import customtkinter as ctk
import tkinter as tk
 
# Sets the appearance of the window
# Supported modes : Light, Dark, System
# "System" sets the appearance mode to 
# the appearance mode of the system
ctk.set_appearance_mode("Dark")   
 
# Sets the color of the widgets in the window
# Supported themes : green, dark-blue, blue    
ctk.set_default_color_theme("dark-blue")    
 
# Dimensions of the window
appWidth, appHeight = 600, 700
 
 
# App Class
class App(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        # Sets the title of the window to "App"
        self.title("Sleep Deprivation")   
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{appWidth}x{appHeight}")    
 
        # Name Label
        self.nameLabel = ctk.CTkLabel(self,
                                text="Name")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self,
                          placeholder_text="Name")
        self.nameEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
 
        #self.label3 = ctk.CTkLabel(self, text="Button")
        #self.label3.grid(row=1, column=0, padx=20, pady=20, sticky="e")
        self.Button = ctk.CTkButton(self,
                                         text="Click to prove you are not a robot",
                                         command=self.button)
        self.Button.grid(row=1, column=1, columnspan=3,
                                        padx=20, pady=20,
                                        sticky="ew")
 
        # Gender Label
        self.genderLabel = ctk.CTkLabel(self,
                                  text="Gender")
        self.genderLabel.grid(row=2, column=0, 
                              padx=20, pady=20,
                              sticky="ew")
 
        # Gender Radio Buttons
        self.genderVar = tk.StringVar(value="They are")
 
        self.maleRadioButton = ctk.CTkRadioButton(self,
                                   text="Male",
                                   variable=self.genderVar,
                                         value="He is")
        self.maleRadioButton.grid(row=2, column=1,
                                  padx=20, pady=20,
                                  sticky="ew")
 
        self.femaleRadioButton = ctk.CTkRadioButton(self,
                                     text="Female",
                                     variable=self.genderVar,
                                     value="She is")
        self.femaleRadioButton.grid(row=2, column=2,
                                    padx=20, pady=20,
                                    sticky="ew")
         
        self.noneRadioButton = ctk.CTkRadioButton(self,
                                    text="Prefer not to say",
                                    variable=self.genderVar,
                                    value="They")
        self.noneRadioButton.grid(row=2, column=3, padx=20,
                                  pady=20, sticky="ew")
        #Slider Label
        self.sliderLabel = ctk.CTkLabel(self,
                                        text="Sleep (Hrs)")
        self.sliderLabel.grid(row=3, column=0,
                              padx=20, pady=20,
                              sticky="ew")   
        #Slider
        self.sliderVar = tk.IntVar(value=8)
        #self.slider = ctk.CTkSlider(self,text="Sleep (Hrs)",variable=self.sliderVar)
        #self.slider.grid(row=3, column=1, padx=20, pady=20,sticky="ew" )    
        self.tkslider = tk.Scale(self, from_=0, to=24, orient='horizontal', variable=self.sliderVar)
        self.tkslider.grid(row=3, column=1,
                              padx=20, pady=20,
                              sticky="ew")
        # Choice Label
        self.choiceLabel = ctk.CTkLabel(self,
                                        text="Mental Health")
        self.choiceLabel.grid(row=4, column=0,
                              padx=20, pady=20,
                              sticky="ew")
 
        # Choice Check boxes
        self.checkboxVar = tk.StringVar(value="neither")
         
        self.choice1 = ctk.CTkCheckBox(self,
                             text="Stressed",
                             variable=self.checkboxVar,
                             onvalue="stressed", offvalue="")
        self.choice1.grid(row=4, column=1,
                          padx=20, pady=20,
                          sticky="ew")
 
        self.choice2 = ctk.CTkCheckBox(self,
                            text="Lethargic",
                            variable=self.checkboxVar,
                            onvalue="lethargic",
                            offvalue="")                               
        self.choice2.grid(row=4, column=2,
                          padx=20, pady=20,
                          sticky="ew")
 
        # Occupation Label
        self.occupationLabel = ctk.CTkLabel(self,
                                    text="Occupation")
        self.occupationLabel.grid(row=5, column=0,
                                  padx=20, pady=20,
                                  sticky="ew")
 
        # Occupation combo box
        self.occupationOptionMenu = ctk.CTkOptionMenu(self,
                                       values=["Student",
                                       "Working Professional", "Retiree"])
        self.occupationOptionMenu.grid(row=5, column=1,
                                       padx=20, pady=20,
                                       columnspan=2, sticky="ew")
 
        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                         text="Generate Results",
                                         command=self.generateResults)
        self.generateResultsButton.grid(row=6, column=1,
                                        columnspan=2, padx=20, 
                                        pady=20, sticky="ew")
 
        # Text Box
        self.displayBox = ctk.CTkTextbox(self,
                                         width=200,
                                         height=100)
        self.displayBox.grid(row=7, column=0,
                             columnspan=4, padx=20,
                             pady=20, sticky="nsew")
 
 
    # This function is used to insert the 
    # details entered by users into the textbox
    def generateResults(self):
        self.displayBox.delete("0.0", "200.0")
        text = self.createText()
        self.displayBox.insert("0.0", text)
 
    # This function is used to get the selected 
    # options and text from the available entry
    # fields and boxes and then generates 
    # a prompt using them
    def createText(self):
        checkboxValue = ""
 
        # .get() is used to get the value of the checkboxes and entryfields
 
        if self.choice1._check_state and self.choice2._check_state:
            checkboxValue += "both " + self.choice1.get() + " and " + self.choice2.get()
        elif self.choice1._check_state:
            checkboxValue += self.choice1.get()
        elif self.choice2._check_state:
            checkboxValue += self.choice2.get()
        else:
            checkboxValue = "neither " + self.choice1._onvalue + " nor " + self.choice2._onvalue
 
        # Constructing the text variable
        text = f"{self.nameEntry.get()} : \n{self.genderVar.get()} {checkboxValue} and sleeps for {self.sliderVar.get()} hours.\n"
        text += f"{self.genderVar.get()} currently a {self.occupationOptionMenu.get()}"
 
        return text

    def button(self):
        print('Not A Robot :)')
        
 
if __name__ == "__main__":
    app = App()
    # Used to run the application
    app.mainloop()      