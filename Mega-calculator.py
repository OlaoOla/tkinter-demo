

"""
# Importing the tkinter module
from tkinter import *

"""
# creating the window instance
win = Tk()

#we dont want the window to be resizable
win.resizable(0, 0)

#Giving a geometry to our window
win.geometry("400x300")

#Title of the application
win.title("MEGA-CALCULATOR")

# Defining all our needed functions to make the calculator work efficiently
# creating a button to update our text field anytime a number is keyed in or any button