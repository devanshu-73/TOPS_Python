#nested conditions


m1=int(input("Enter marks 1 : "))

if m1>=40:
    m2=int(input("Enterr marks 2 : "))
    if m2>=40:
        m3=int(input("Enterr marks 3 : "))
        if m3>=40:
            print("PASS")
        else:
            print("FAIL")
    else:
        print("FAIL")
else:
    print("FAIL")
