def main():
    # Displaying the menu for pizza price calculator
    print("""    
                 BPP Pizza Price Calculator                
               ===============================
          1)..........Number of pizza..........
          2)..........Delivery required or not..........    
          3)..........Tuesday or not..........
          4)..........App used or not..........
          """)
    print()
    # Enables getting the user's choice from the given Menu
    choice = input_choice()

    if choice in [1, 2, 3, 4]:
        num_pizzas = num_of_pizzas()
        delivery_required = delivery_option()
        is_tuesday = tuesday_option()
        used_app = app_option()

        # Calculate and display the total price
        total_price, breakdown = calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app)
        print("\nBilling Summary:")
        print("BPP Pizza Price Calculator")
        print(f"="*30)
        print(f"Number of Pizzas: {num_pizzas}")
        print(f"Delivery Required: {'Yes' if delivery_required else 'No'}")
        print(f"Tuesday Discount: {'Applied' if is_tuesday else 'Not Applied'}")
        print(f"App Discount: {'Applied' if used_app else 'Not Applied'}")
        print("\n" + "="*30)
        print(breakdown)
        print("="*30)
        print(f"Total Price: £{total_price:.2f}.")


def calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app):
    pizza_price = 12.0
    delivery_cost = 2.5
    discount_tuesday = 0.5
    discount_app = 0.25

    # Calculate the total price of pizzas
    total_pizza_cost = num_pizzas * pizza_price
    breakdown = f"Pizza Cost ({num_pizzas} pizzas): £{total_pizza_cost:.2f}\n"

    # Applying Discounts based on conditions
    if is_tuesday:
        discount_amount_tuesday = total_pizza_cost * discount_tuesday
        total_pizza_cost -= discount_amount_tuesday
        breakdown += f"Tuesday Discount (-£{discount_amount_tuesday:.2f}): £{total_pizza_cost:.2f}\n"

    if delivery_required:
        delivery_charge = delivery_cost if num_pizzas < 5 else 0
        total_pizza_cost += delivery_charge
        breakdown += f"Delivery Charge (+£{delivery_charge:.2f}): £{total_pizza_cost:.2f}\n"

    if used_app:
        discount_amount_app = total_pizza_cost * discount_app
        total_pizza_cost -= discount_amount_app
        breakdown += f"App Discount (-£{discount_amount_app:.2f}): £{total_pizza_cost:.2f}\n"

    return total_pizza_cost, breakdown

    
def input_choice():
    # Getting Users choice for the menu option
      while True:
        user_input = input("Press the Enter key to start: ")
        if user_input == '':
            return 1  # Assuming Enter key press corresponds to option 1
        else:
            print("Please press the Enter key to start.")

def num_of_pizzas():
    # Getting the num of pizzas from the user
    while True:
        try:
            num_pizzas = int(input("Enter the number of pizzas: "))
            if num_pizzas >= 1:
                return num_pizzas
            else:
                print("Please enter a positive integer!.")
        except ValueError:
            print("Invalid input. Please enter a valid integer!.")


def delivery_option():
    # Getting the user's choice for the delivery option
    while True:
        option = input("Is delivery required? (y/n): ").lower()
        if option in ['y', 'n']:
            return option == 'y'
        else:
            print("Please enter 'y' for Yes or 'n' for No.")


def tuesday_option():
    # Getting user's choice for whether it is Tuesday
    while True:
        option = input("Is it Tuesday? (y/n): ").lower()
        if option in ['y', 'n']:
            return option == 'y'
        else:
            print("Please enter 'y' for Yes or 'n' for No.")


def app_option():
    # Getting user's choice for whether the app was used
    while True:
        option = input("Did the customer use the app? (y/n): ").lower()
        if option in ['y', 'n']:
            return option == 'y'
        else:
            print("Please enter 'y' for Yes or 'n' for No.")


if __name__ == "__main__":
    # Execute the main function if the script is run as the main program
    main()
