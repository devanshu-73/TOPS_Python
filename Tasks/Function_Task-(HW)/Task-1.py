# Task : 1 :
        
# Accomplish below tsk using Function : 

# ============Welcome To TOPS Restaurent==============

	# Srno.	Item		Price
	# 1	Pizza		90/-
	# 2	Burgur		89/-
	# 3	Pani-Puri	100/-
	# 4	Dosa		80/-

# 	Enter Your Choice from choice : 3
	
# 	Your Item : Pani-puri
# 	Enter Quantity : 2
# 	Total Price : 200/-

# 	Do You want Anything else ? ['y/n']:

# 	---------------------------------------------------
# 	if n 
# 	Thank You 
# 	Your Total Bill : 200 rs.

# 	----------------------------------------------------
# 	if y

# 	Enter choice from MENU : 1

# 	your Item : Pizza
# 	Enter Quantity : 3
# 	Total Price : 270/-

# 	Do You want Anything Eles ?['y/n']: 

# 	if n
# 	Thank You
# 	your Total Bill : 470rs.

print("""
    ============Welcome To TOPS Restaurent==============
	     
        Sr   Item		Price
        1	 Pizza		90/-
        2	 Burgur		89/- 
        3	 Pani-Puri      100/-
	4	 Dosa		80/-
      """)

result = True
while result:
    choice = int(input("Enter Your Choice from choice :"))
    if(choice == 1):
        print("Your Item : Pizza")
        quantity = int(input("Enter Quantity : "))
        total_price = 90*quantity
        print(f"Total Price : {total_price}")
    elif(choice == 2):
        print("Your Item : Burgur")
        quantity = int(input("Enter Quantity : "))
        total_price = 89*quantity
        print(f"Total Price : {total_price}")
    elif(choice == 3):
        print("Your Item : Pani-Puri")
        quantity = int(input("Enter Quantity : "))
        total_price = 100*quantity
        print(f"Total Price : {total_price}")
    elif(choice == 4):
        print("Your Item : Dosa")
        quantity = int(input("Enter Quantity : "))
        total_price = 80*quantity
        print(f"Total Price : {total_price}")
    else:
        print("You Entered Wrong Input...")
    more = input("Do You want Anything else ? ['y/n'] :")
    if(more != 'y'):
        print(f"""
              Thank You...
              Your Total Bill : {total_price} rs.
              """)
        result = False