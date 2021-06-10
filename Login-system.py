# importing our tkinter module
from tkinter import *
from tkinter import ttk # importing the ttk class
from tkinter.messagebox import showinfo

#setting up our window
win = Tk()
win.geometry( "400x350" )
win.title( "My Login System" )

def message():
    if len( strVar1.get()) != 0 and len( strVar2.get()) != 0 and len( strVar3.get()) != 0 and len( strVar4.get()) != 0:
        showinfo( "Message", f"You are sucessfully logged in!" )
    else: 
        showinfo( "Message", f"please enter the correct username and password" )


# Design our username
lblUsername = Label(win, text = "Username", font = ( "Arial Bold" , 15) )
lblUsername.place(x = 50, y = 50)

# Design Username text field
strVar1 = StringVar()
txtUsername = Entry( win, width = 20, textvariable = strVar1 )
txtUsername.place(x = 170, y = 50 )


# Design our email 
lblemail = Label(win, text = "Email", font = ( "Arial Bold" , 15) )
lblemail.place(x = 50, y = 100)

# Design Email text field
strVar2 = StringVar()
txtemail = Entry( win, width = 20, textvariable = strVar2 )
txtemail.place(x = 170, y = 100 )

# Design our Contact 
lblcontact = Label(win, text = "Contact", font = ( "Arial Bold" , 15) )
lblcontact.place(x = 50, y = 150)

# Design contact text field
strVar3 = StringVar()
txtcontact = Entry( win, width = 20, textvariable = strVar3 )
txtcontact.place(x = 170, y = 150 )



# Designing our password label
lblPassword = Label(win, text = "Password", font = ( "Arial bold", 15))
lblPassword.place(x =50, y = 200 )

# Designing our password text field
strVar4 = StringVar()
txtpassword = Entry( win, width = 20, textvariable = strVar4 )
txtpassword.place( x = 170, y = 200 )


# Designing our Login Button
btnlogin = Button( win, text = "login", width = 20, command = message )
btnlogin.place( x = 100, y = 300 )




win.mainloop()