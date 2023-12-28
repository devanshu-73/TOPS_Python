import os
from datetime import datetime

name = input("Enter your name: ")

while True:
    try :
        age = int(input("Enter your age: "))
        if 1<= age <= 100:
            break
        else:
            print("Tamari Age 1 to 100 Hovi Joiye ")
    except:
        print("Plz input ma only numbers enter karo..")
while True:
    try :
        contact = input("Enter your contact number: ")
        if 6<= len(contact) <=10:
            int(contact)
            break
        else:
            print("Tamaro Contact 10 digit no hovo Joiye and Numbers Only")
    except:
        print("Plz enter valid contact number (only 10 digit no).")

vaccine_name = input("Enter the vaccine name: ")

while True:
    try :
        dose = int(input("Enter the vaccine dose [1/2/3]: "))
        if 1<= dose<=3:
            break
        else:
            print("between 1 to 3 doze enter karo ")
    except:
        print("Plz enter a valid vaccine dose (1, 2, or 3).")

# Get current date and time
date_time = datetime.now()
date = date_time.strftime("%d-%m-%Y")
time = date_time.strftime("%Hh_%Mm")

if not os.path.exists(f"vaccine_reports-{date}"):
    os.makedirs(f"vaccine_reports-{date}")
# else:
#     print("Already Exists..")
    
report_name = f"vaccine_reports-{date}/{name}_{date}-{time}.txt"

f = open(report_name, "w")
f.write(
    f"Vaccine Report\n"
    f"Date and Time: {date_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"Contact Number: {contact}\n"
    f"Vaccine Name: {vaccine_name}\n"
    f"Vaccine Dose: {dose}\n"
)
f.close()

print(f"Vaccine report created: {report_name}")
