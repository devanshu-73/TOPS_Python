import pymysql


# Database Creation

# mydb = pymysql.connect(host="localhost",user="root",passwd="")
# cursor = mydb.cursor()
# cursor.execute("create database class")
# mydb.commit()


# if Database already exists then

mydb = pymysql.connect(host="localhost",user="root",passwd="",database="class")
cursor = mydb.cursor()
cursor.execute("create table if not exists class1 (id int primary key auto_increment , name varchar(20), subject varchar(20))")
mydb.commit()







# Drop the topspython database
# cursor.execute("DROP DATABASE IF EXISTS topspython")

# Commit the changes
# mydb.commit()

# Close the connection
# mydb.close()
