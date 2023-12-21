class PizzaSystem:
    def __init__(self):
        self.total_order_amount = 0
        self.total_pizza_sold = 0
        self.total_pasta_sold = 0
        self.total_soft_drinks_given = 0
        self.total_bruschetta_given = 0
        self.total_ice_cream_given = 0

    def display_menu(self):
        print("Welcome to Amazing Pizza and Pasta Pizzeria")
        print("\n1 large pizza = 10.99 AUD\n2 large Pizzas = 20.99 AUD\n3 Large Pizzas = 29.99 AUD")
        print("***Buy 4 or more pizza and get 1.5lt of soft drink free***\n")
        print("1 large pasta = 9.5 AUD\n2 large pastas = 17.00 AUD\n3 large pastas = 27.50 AUD")
        print("***Buy 4 or more pastas and get 2 bruschetta free.***")
        print("***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.\n")

    def take_order(self, name):
        print(f"\nEnter your name : {name}\n")
        print(f"Welcome, {name}")

        pizza_quantity = int(input("Enter number of pizza orders you want: "))
        pizza_amount = self.calculate_amount(pizza_quantity, 10.99)
        print(f"\nYour pizza order amount is: {pizza_amount:.2f}")

        if pizza_quantity >= 4:
            print("*** Congratulations!! 1.5lt soft drink free ***")
            self.total_soft_drinks_given += 1

        pasta_quantity = int(input("\nEnter number of pasta orders you want: "))
        pasta_amount = self.calculate_amount(pasta_quantity, 9.5)
        print(f"\nYour pasta order amount is: {pasta_amount:.2f}")

        if pasta_quantity >= 4:
            print("*** Congratulations!! Get 2 bruschetta free ***")
            self.total_bruschetta_given += 2

        if pizza_quantity + pasta_quantity >= 4:
            print("*** Congratulations!! Get 2 chocco brownies ice cream free ***")
            self.total_ice_cream_given += 2

        total_order = pizza_amount + pasta_amount
        print(f"\nYour total order is: {total_order:.2f}")

        self.total_order_amount += total_order
        self.total_pizza_sold += pizza_quantity
        self.total_pasta_sold += pasta_quantity

    def calculate_amount(self, quantity, price_per_item):
        return quantity * price_per_item

    def display_summary(self):
        print("\n----------- Pizza and Pasta Bill --------------")
        print(f"Payment received from pizza: {self.total_pizza_sold * 10.99:.2f}")
        print(f"Payment received from pasta: {self.total_pasta_sold * 9.5:.2f}")
        print(f"Payment received today: {self.total_order_amount:.2f}")
        print(f"Number of pizza and pasta sold in one shift: {self.total_pizza_sold + self.total_pasta_sold}")
        print(f"Number of 1.5lt soft drink bottles given: {self.total_soft_drinks_given}")
        print(f"Number of bruschetta given to customer: {self.total_bruschetta_given}")
        print(f"Number of chocco brownies ice cream given to customer: {self.total_ice_cream_given}")
        print("\nBye Bye!!!")


if __name__ == "__main__":
    pizza_system = PizzaSystem()

    while True:
        print("\n1: Order Menu\n2: Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            pizza_system.display_menu()
            name = input("\nEnter your name: ")
            pizza_system.take_order(name)
            continue
        elif choice == "2":
            pizza_system.display_summary()
            break
