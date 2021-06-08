# importing tkinter for our interface design

import tkinter as tk #using the alias tk instead of the normal tkinter
from tkinter import ttk

#create an intance of tk
window = tk.Tk()

# Giving out window a title 
window.title( "our demo app" )

# restricting window resizing
window.resizable( True, True)

# introducing our first label
ttk.Label(window, text = "Guess my name"). grid(column =0, row= 0)
lblName = ttk.Label ( window, text = "Guess my name")
lblName.grid( column = 0, row = 0)

#Starting our button up for an event
def reveal_me() :
    action.configure( text = "Mystery Solved!")
    lblName.configure( foreground = "blue")
    lblName.configure( text = "Benjamin Benson") # Name revealed 

# Starting up our textfield event
def click_me():
    text_action.configure( text = "Hello " + name.get()) #Displaying the user's name

#setting our text label
lblText = ttk.Label(window, text = "Please enter a name", padding = 3,)
lblText.grid (column =0, row = 2)

# Adding our textbox widget
name = tk.StringVar ()
user_name = ttk.Entry( window, width = 14, textvariable= name)
user_name.grid( column = 0 , row = 3)

#Adding our button
action = ttk.Button( window, text = 'Open Sesame!', command = reveal_me) #Activating the button
action.grid( column =1, row = 0)

#Adding our text button
text_action = ttk.Button( window, text="Click to greet", command = click_me)
text_action.grid( column =1, row =3)

# starting the GUI
window.mainloop()