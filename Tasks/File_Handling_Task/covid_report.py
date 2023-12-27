import os
from datetime import datetime

name = input("Enter your name: ")

while True:
    age = input("Enter your age: ")
    if age.isdigit() and 1<= int(age) <= 100:
        age = int(age)
        break
    else:
        print("Please enter a valid age (integer only).")

while True:
    contact = input("Enter your contact number: ")
    if contact.isdigit():
        contact_no = int(contact)
        break
    else:
        print("Please enter a valid contact number (integer only).")

vaccine_name = input("Enter the vaccine name: ")

while True:
    dose = input("Enter the vaccine dose [1/2/3]: ")
    if dose.isdigit() and 1 <= int(dose) <= 3:
        vaccine_dose = int(dose)
        break
    else:
        print("Please enter a valid vaccine dose (1, 2, or 3).")

# Get current date and time
date_time = datetime.now()
date = date_time.strftime("%d-%m-%Y")
time = date_time.strftime("%Hh_%Mm")

# Check if the directory already exists, if not, create it
if not os.path.exists(f"vaccine_reports-{date}"):
    os.makedirs(f"vaccine_reports-{date}")
# else:
#     print("Already Exists..")
    
# Create a report file with the user's name and the current date and time
report_name = f"vaccine_reports-{date}/{name}_{date}-{time}.txt"

f = open(report_name, "w")
f.write(
    f"Vaccine Report\n"
    f"Date and Time: {date_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"Contact Number: {contact_no}\n"
    f"Vaccine Name: {vaccine_name}\n"
    f"Vaccine Dose: {vaccine_dose}\n"
)
f.close()

print(f"Vaccine report has been created: {report_name}")
