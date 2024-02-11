import pymysql

db = pymysql.connect(host='localhost',user='root',passwd='',database='class')
cursor = db.cursor()

def add():
    print("Add Operation")

def dispay():
    print("Display Operation")
    
def update():
    print("Update Operation")
    
def delete():
    print("Delete Operation")
    

menu = '''
    press 1 Create/Add
    press 2 Read/Display
    press 3 Update
    press 4 Delete
    press 5 Exit
'''
while True:
    print(menu)
    ch = int(input("Enter Your Choice : "))
    if ch == 5:
        break
    elif ch == 1:
        add()
    elif ch == 2:
        dispay()
    elif ch == 3:
        update()
    elif ch == 4:
        delete()