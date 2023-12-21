class PizzaOrderSystem:
    def __init__(self):
        self.total_order_amount = 0
        self.total_payment_received = 0
        self.total_pizza_sold = 0
        self.total_pasta_sold = 0
        self.total_soft_drinks_given = 0
        self.total_bruschetta_given = 0
        self.total_chocco_brownies_given = 0

    def menu(self):
        print(
            """1. Large pizza = 100\n2. Large Pizzas = 200\n3. Large Pizzas = 300
***Buy 4 or more pizzas and get 1.5lt of soft drink free***
1. Pasta = 50\n2. Pastas = 100\n3. Pastas = 150
***Buy 4 or more pastas and get 2 bruschetta free.***
***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.***
--------------------------------"""
        )

    def order(self):
        name = input("Enter your name: ")
        print(f"Welcome, {name}")

        num_pizzas = int(input("How many pizzas do you want? : "))
        pizza_amount = num_pizzas * 100
        print(f"Your pizza order amount is: {pizza_amount}")

        if num_pizzas >= 4:
            print("***Congratulations!! 1.5lt soft drink free***")
            self.total_soft_drinks_given += 1

        num_pastas = int(input("\nHow many pastas do you want? : "))
        pasta_amount = num_pastas * 50
        print(f"Your pasta order amount is: {pasta_amount}")

        if num_pastas >= 4:
            print("***Congratulations!! Get 2 bruschetta free***")
            self.total_bruschetta_given += 2

        if num_pizzas >= 4 and num_pastas >= 4:
            print("***Congratulations!! Get 2 chocco brownies ice cream free***")
            self.total_chocco_brownies_given += 2

        total_order = pizza_amount + pasta_amount
        print(f"Your total order is: {total_order}")

        self.total_order_amount += total_order
        self.total_payment_received += total_order
        self.total_pizza_sold += num_pizzas
        self.total_pasta_sold += num_pastas

    def collections(self):
        print("\n----------- Pizza and pasta Bill --------------")
        print(f"Payment received today: {self.total_payment_received}")
        print(f"Number of pizzas sold in one shift: {self.total_pizza_sold}")
        print(f"Number of pastas sold in one shift: {self.total_pasta_sold}")
        print(f"Number of 1.5lt soft drink bottles given: {self.total_soft_drinks_given}")
        print(f"Number of bruschetta given to customers: {self.total_bruschetta_given}")
        print(
            f"Number of chocco brownies ice cream given to customers: {self.total_chocco_brownies_given}"
        )
        print("\nBye Bye!!!")


pizza_system = PizzaOrderSystem()

while True:
    print("\nWelcome to Tops Restaurant")
    print("1. Order menu")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        pizza_system.display_menu()
        pizza_system.order()
    elif choice == "2":
        pizza_system.collections()
        break
