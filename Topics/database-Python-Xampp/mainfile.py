import pymysql

mydb= pymysql.connect(host="localhost", user="root",passwd="", database="class")
cursor=mydb.cursor()

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
   query="insert into class1 (name,subject) values ('%s','%s')"
   
   cursor.execute(query % args)

   mydb.commit()
   
   print("succefully added!!")
   
def updateOperation():
   id = int(input("Which student do you want to update : "))
   name=input("Enter update name : ")
   subject=input("Enter update subject : ")
   
   args=(name,subject,id)
   query="update class1 set name='%s', subject='%s', where id=%s"
   
   cursor.execute(query % args)
   mydb.commit()
 
def searchStudent():
   
   name=input("Enter your name : ")
   # 1nd Way
   query = f"select * from class1 where name='{name}'"
   cursor.execute(query)

   # 2rd Way : string formating with placeholder
   # query = ("select * from class1 where name='{}'").format(name)
   
   # 3nd Way
   # query = "select * from class1 where name='%s'"
   # args=(name)
   # cursor.execute(query % args)
   
   res = cursor.fetchone()
   
   print("Id :",res[0])
   print("Name :",res[1])
   print("Subject :",res[2])

def deleteOperation():
   
   id = int(input("enter the ID of the student you want to delete: "))
  
   # 1st Way
   query = f"delete from class1 where id ={id}"
   cursor.execute(query)
   
   # 2nd Way
   # query = "delete from class1 where id = %s"
   # args = (id,)
   # cursor.execute(query, args)
   
   # 3rd Way
   # query = "delete from class1 where id = {}".format(id)
   # cursor.execute(query)
   print("Student Deleted Successfully !")
   mydb.commit()

status=True

while status:
   print(menu)
   
   choice=int(input("Enter your choice : "))
   
   if choice==1:
      addOperations()
   elif choice==2:
      updateOperation()
   elif choice==3:
      deleteOperation()
   elif choice==4:
      searchStudent()
      
   more=input("Do you want to continue? [y/n]: ")
    
   if more.lower() == "y":
      status = True
   else:
      status = False