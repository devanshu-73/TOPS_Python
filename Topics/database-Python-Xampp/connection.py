import pymysql

mydb = pymysql.connect(host="localhost",user="root",passwd="")
cursor = mydb.cursor()
cursor.execute("create databse class")
cursor.commit()

cursor.execute()
mydb = pymysql.connect(host="localhost",user="root",passwd="",database="class")
cursor = mydb.cursor()

cursor.execute("create table if not exists class1 (id int primary key auto_increment , name varchar(20), subject varchar(20))")
cursor.commit()