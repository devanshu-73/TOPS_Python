class PizzaSystem:
    def __init__(self):
        self.total_order_amount = 0
        self.total_payment_received = 0
        self.total_pizza_sold = 0
        self.total_pasta_sold = 0
        self.total_soft_drinks_given = 0
        self.total_bruschetta_given = 0
        self.total_chocco_brownies_given = 0

    def display_menu(self):
        print("1. large pizza = 100\n2. large Pizzas = 200\n3. Large Pizzas = 300")
        print("***Buy 4 or more pizza and get 1.5lt of soft drink free***")
        print("1. pasta = 50\n2. pastas = 100\n3. pastas = 150")
        print("***Buy 4 or more pastas and get 2 bruschetta free.***")
        print("***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.***")
        print("--------------------------------")

    def take_order(self):
        name = input("Enter your name: ")
        print(f"\nWelcome, {name}")

        num_pizzas = int(input("How Many Pizza Do You Want? : "))
        pizza_amount = num_pizzas * 100
        print(f"\nYour pizza order amount is : {pizza_amount}")

        if num_pizzas >= 4:
            print("***Congratulations!! 1.5lt soft drink free***")
            self.total_soft_drinks_given += 1

        num_pastas = int(input("\nHow Many Pasta Do You Want? : "))
        pasta_amount = num_pastas * 50
        print(f"\nYour pasta order amount is : {pasta_amount}")

        if num_pastas >= 4:
            print("***Congratulations!! get 2 bruschetta free***")
            self.total_bruschetta_given += 2

        if num_pizzas >= 4 and num_pastas >= 4:
            print("***Congratulations!! get 2 chocco brownies ice cream free***")
            self.total_chocco_brownies_given += 2

        total_order = pizza_amount + pasta_amount
        print(f"\nYour total order is : {total_order}")

        self.total_order_amount += total_order
        self.total_payment_received += total_order
        self.total_pizza_sold += num_pizzas
        self.total_pasta_sold += num_pastas

    def display_summary(self):
        print("\n----------- Pizza and pasta Bill --------------")
        print(f"Payment received today: {self.total_payment_received}")
        print(f"Number of pizza sold in one shift: {self.total_pizza_sold}")
        print(f"Number of pasta sold in one shift: {self.total_pasta_sold}")
        print(f"Number of 1.5lt soft drink bottles given: {self.total_soft_drinks_given}")
        print(f"Number of bruschetta given to customers: {self.total_bruschetta_given}")
        print(f"Number of chocco brownies ice cream given to customers: {self.total_chocco_brownies_given}")
        print("\nBye Bye!!!")


if __name__ == "__main__":
    pizza_system = PizzaSystem()

    while True:
        print("\nWelcome to Tops Restaurant")
        print("1. Order menu\n2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            pizza_system.display_menu()
            pizza_system.take_order()
        elif choice == "2":
            pizza_system.display_summary()
            break
