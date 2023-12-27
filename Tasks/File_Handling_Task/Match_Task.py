teams = ["csk","gt","rcb","mi"]
print("============ IPL ============")
print("1) CSK")
print("2) GT")
print("3) RCB")
print("4) MI")
print("To Exit The Game Enter 'stop'")
result = True
while result:
    choice = int(input("Enter Your Team Number : "))

    if choice.lower() == 'stop':
        break

print("User inputs:", choice)
