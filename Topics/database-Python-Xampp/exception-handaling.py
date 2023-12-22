"""
Exception Handling : to handle such kind of exception using try and catch
"""

# try :
#     print(a)
# except:
#     print("something went wrong")


# try :
#     num1 = int(input("enter num 1 :"))
#     num2 = int(input("enter num 2 :"))
#     ans = num1/num2
#     print(ans)
# except ValueError:
#     print("invalid input")
# except ZeroDivisionError:
#     print("can not divide by zero")
    
try :
    num1 = int(input("enter num 1 :"))
    num2 = int(input("enter num 2 :"))
    ans = num1/num2
    print(ans)
except Exception as e:
    print(e)
