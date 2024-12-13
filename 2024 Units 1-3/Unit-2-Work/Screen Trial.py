from tkinter import *
import customtkinter as ctk
root = Tk()
root.title("hello")
root._state_before_windows_set_titlebar_color = 'zoomed'

top = Toplevel(root)
top.title("Python")
top._state_before_windows_set_titlebar_color = 'zoomed'
top.mainloop()