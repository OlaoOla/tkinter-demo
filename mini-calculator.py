"""
This is a mini-calclator app that is meant to register mouse clicks and keyboard hits
"""

#importing the tkinter module
from tkinter import *
class ourWindow:."""
    def __init__(self, win): 
        #setting up our labels
        self.lblFnum = label(win, text = "First Number" )
        self.lblFnum = place( x =100, y =50 ) # Setting the position for First Number label
        self.lblSnum = label(win, text = "Second Number" )
        self.lblFnum = place( x =100, y =100 ) # Setting the position for First Number label
        self.lblResult = label(win, text = "Result" )
        self.lblFnum = place( x =100, y =200 )


        #setting up our textboes(Entry fields)
        self.txtFnum = Entry()
        self.txtSnum = Entry()
        self.txtSnum = place( x = 200, y = 50) # Setting the position for First Number label
        self.txtResult = Entry( bd = 3 ) # giving the result textbox a boarder of width 3
        self.txtResult = place( x = 200, y = 200) # Setting the position for the Result Entry field
        
        # Seting up our Buttons
        self.btnAdd = Button( win, text = "Add" , command = self.add )
        self.btnSubtract = Button( win, text = "Subtract")
        self.btnSubtract = Button( win, text = "Subtract" , command = self.sub ) 
        self.btnSubtract.place( x = 200, y = 150 ) Setting the position for the Subtract button


# Defining our addition event
def add(self):
    self,txtResult.delete( 0, 'end')
    firstNumber= int( self.txtFnum.get()) # Grabbing the input from the first number entry field
    secondNumber= int( self.txtSnum.get()) # Grabbing the input from the second number entry field

result = firstNumber + secondNumber # performing the addition


# Defining our subtraction event
def sub(self):
    self,txtResult.delete( 0, 'end')
    firstNumber= int( self.txtFnum.get()) # Grabbing the input from the first number entry field
    secondNumber= int( self.txtSnum.get()) # Grabbing the input from the second number entry field

result = firstNumber + secondNumber # performing the subtraction

self.txtResult.insert( END, str( result) )

# Setting upp the window

container = Tk()
mycontainer = OurWindow(container)
container.title("Mini-Calculator")
container.geometry("400x300+10+10")
container.mainloop()