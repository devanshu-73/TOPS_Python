import os # operating system

if os.path.exists("firstfolder"):
    print("Already exists")
    os.rmdir("firstfolderW")
else:
    os.mkdir("firstfolder")
    print("Created")