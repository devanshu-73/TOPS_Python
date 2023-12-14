'''

Tkinter : Library im python for GUI

tkinter : module to get the GUI elements

'''

from tkinter import Tk,Label,Entry,Button
from tkinter import messagebox as msg

# Tk : class from tkinter module

# object creation of Tk class
obj = Tk()

obj.title("My Tkinter Window")
obj.geometry('400x400')
obj.resizable(False,False)

def get_data():
    data=e_name.get()
    msg.showinfo('Title',data)


# to write any text on window use Label Class
heading = Label(obj, text="Welcome to Sports Club",bg="black",fg="white", font=('Arial 12 bold'))
heading.place(x=100,y=40)

#=====================Label====================================
name = Label(obj, text="Enter Name : ", font=('Arial 11'))
name.place(x=50,y=90)


#=====================Entry====================================
e_name=Entry(obj,)
e_name.place(x=150,y=90)


#=====================Button====================================
btn=Button(obj, text="SUBMIT", command=get_data)
btn.place(x=150,y=130)

# to close the tkinter window
# obj.mainloop()








