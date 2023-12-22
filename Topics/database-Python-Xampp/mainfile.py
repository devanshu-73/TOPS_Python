import pymysql

mydb= pymysql.connect(host="localhost", user="root",passwd="", database="topspython")
mycursor=mydb.cursor()

menu="""

      press 1 for add student
      press 2 for update student
      press 3 for delete student
      press 4 for display student

"""

def addOperations():
   print("-------- ADD STUDENT --------")
   name=input("Enter name : ")
   subject=input("Enter Subject : ")
   
   args=(name,subject)
   query="insert into student (name,subject) values ('%s','%s')"
   
   mycursor.execute(query % args)

   mydb.commit()
   
   print("succefully added!!")
   
def updtateOperation():
   id = int(input("Which student do you want to update : "))
   name=input("Enter update name : ")
   subject=input("Enter update subject : ")
   
   args=(name,subject,id)
   query="update student set name='%s', subject='%s', where id=%s"
   
   mycursor.execute(query % args)
   mydb.commit()
   
def searchStudent():
   name=input("Enter your name : ")
   query = "select * from Student where name='%s'"
   args=(name)
   
   mycursor.execute(query % args)
   res = mycursor.fetchone()
   
   print(res[0])
   print(res[1])
   print(res[2])

status=True

while status:
   print(menu)
   
   choice=int(input("Enter your choice : "))
   
   if choice==1:
      addOperations()
   elif choice==2:
      updtateOperation()
   elif choice==4:
      searchStudent()
      
   more=input("Do you want to continue? [y/n]: ")
   
   if more=="Y" or more=="y":
      status=True
   else:
      status=False