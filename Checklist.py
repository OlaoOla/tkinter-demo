#importing our tkinter module
from tkinter import *
from tkinter.ttk import Combobox # Importing Combobox
# creating an instance of the Tk window
win = Tk()

numbers = ("one", "five", "Twelve", "Sixteen" )

# creating our Listbox
lbListbox = Listbox(win, height = 5, selectmode = "multiple")

# LOOPING THROUGH THE NUMBERS ONE BY ONE TO BE USED IN THE LISTBOX
for number in numbers:
    lbListbox.insert( END, number) # insert every number at the end( on the next line)

    lbListbox.place(x=250, y=150)


#creating our Combobox
data = StringVar() # Variable to record selections or inputs
data.set( numbers [0]) # taking the first value in the numbers tuple variable

cbCombobox = Combobox( win, value = numbers ) # setting the values for the combobox
cbCombobox.place( x =60, y = 150 )


# Creating a checkbutton
check1_value = IntVar() # creating a variable to hold integer values
check2_value = Intvar() # creating a variable to hold integer values
cb1Checkbox = Checkbutton( win, text = "Guava" , variable = check1_value)
cb2Checkbox = checkbutton( win, text = "Orange" , variable = check2_value )

cb1Checkbox.place( x = 70, y = 100) # position for first checkbutton
cb2Checkbox.place( x = 130, y = 100) # position for second checkbutton


#creating a radiobutton
rb_value = Intvar() 
rb_value.set( 1 )

rb1Radiobutton = Radiobutton( win, text = "Male" , variable = rb_value, value = 1 )
rb2Radiobutton = Radiobutton( win, text = "Female" , variable = rb_value, value = 1 )
rb1Radiobutton.place( x = 70, y = 50)
rb2Radiobutton.place( x = 70, y = 50)

win.title("checklist App")
win.geometry( "400x300+10+10")
win.mainloo