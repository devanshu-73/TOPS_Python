from tkinter import *
from tkinter import messagebox as msg
import mysql.connector


root=Tk()
root.title('My Tkinter DB Connect')
root.geometry('500x400')
root.resizable(False,False)

# declare string variable for radiobutton
var=StringVar()

#==========================DB Connectivity===========================

def connection():
    return mysql.connector.connect(
        user='root',
        host="localhost",
        password='',
        database="college_data",
        )


def save_data():
    if e_name.get()=="" or e_age.get()=="" or var.get()=="" or e_email.get()=="":
        msg.showinfo("Insert Status","Data Entered Fail")
    else:
        conn=connection()
        cursor=conn.cursor()
        query="insert into student(name,age,gender,email) values(%s,%s,%s,%s)"
        args=(e_name.get(),e_age.get(),var.get(),e_email.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_name.delete(0,'end')
        e_age.delete(0,'end')
        e_email.delete(0,'end')
        msg.showinfo("Insert Status","Data Entered successfully")
        
def retrive_data():
    if e_email.get()=="":
        msg.showinfo("Data Retrive Status","Email is Mandatory !!!")
    else:
        conn=connection()
        cursor=conn.cursor()
        query="select * from student where email=%s"
        args=(e_email.get(),)
        cursor.execute(query,args)
        e_name.delete(0,'end')
        e_age.delete(0,'end')
        e_email.delete(0,'end')
        row=cursor.fetchall()
        print(row)
        e_name.insert(0,row[0][1])
        e_age.insert(0,row[0][2])
        e_email.insert(0,row[0][4])
        conn.commit()
        conn.close()
        msg.showinfo("Insert Status","Data Entered successfully")


#=================Labels======================

head=Label(root,text="Student Management System", font=('Arial 14 bold'))
head.place(x=100,y=30)

name=Label(root,text="Enter Name : ",font=('Arial 12'))
name.place(x=50, y=100)

age=Label(root,text="Enter Age : ",font=('Arial 12'))
age.place(x=50, y=150)

gender=Label(root,text="Select Gender : ",font=('Arial 12'))
gender.place(x=50, y=200)

email=Label(root,text="Enter Email : ",font=('Arial 12'))
email.place(x=50, y=250)

#=======================Entry==================

e_name=Entry(root,)
e_name.place(x=200,y=100)

e_age=Entry(root,)
e_age.place(x=200,y=150)

e_male=Radiobutton(root,text="male",variable=var,value="male")
e_male.place(x=200,y=200)

e_female=Radiobutton(root,text="female",variable=var,value="female")
e_female.place(x=250,y=200)

e_email=Entry(root,)
e_email.place(x=200,y=250)

#===================Buttons===================


save=Button(root, text="SAVE", font=('Arial 12'), command=save_data)
save.place(x=70,y=330)

retrive=Button(root, text="RETRIVE", font=('Arial 12'), command=retrive_data)
retrive.place(x=150,y=330)

update=Button(root, text="UPDATE", font=('Arial 12'))
update.place(x=250,y=330)

delete=Button(root, text="DELETE", font=('Arial 12'))
delete.place(x=350,y=330)















