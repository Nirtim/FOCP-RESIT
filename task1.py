PIZZA_COST = 12
POSSIBLE_INPUT_LIST = ['n', 'no', 'y', 'yes']

def calculate_delivery_charge(num_of_pizzas):
    """Calculate delivery charge if needed."""
    return 0 if num_of_pizzas >= 5 else 2.50

def apply_tuesday_discount(total_price, is_tuesday):
    """Apply Tuesday discount if applicable."""
    return total_price * 0.5 if is_tuesday in ['y', 'yes'] else total_price

def apply_app_discount(total_price, used_app):
    """Apply app discount if applicable."""
    return total_price * 0.75 if used_app in ['y', 'yes'] else total_price

def calculate_total_price(num_of_pizzas, needs_delivery, is_tuesday, used_app):
    """Calculate total price based on inputs."""
    # Calculate base price of pizzas
    total_price = num_of_pizzas * PIZZA_COST
    
    # Apply Tuesday discount if it's Tuesday
    total_price = apply_tuesday_discount(total_price, is_tuesday)

    # Calculate and add delivery charge if needed
    if needs_delivery in ['y', 'yes']:
        delivery_cost = calculate_delivery_charge(num_of_pizzas)
        total_price += delivery_cost

    # Apply app discount if used
    return round(apply_app_discount(total_price, used_app), 2)


def main():
    """Handle user input and display total price."""
    print("""
BPP Pizza Price Calculator
==========================
          """)

    while True:
        num_of_pizzas = int(input("How many pizzas would you like to order?  "))
        while num_of_pizzas <= 0:
            print("Please enter a positive number")
            num_of_pizzas = int(input("How many pizzas would you like to order? "))

        needs_delivery = input("Do you require delivery? (Y/N) ").lower()
        while needs_delivery not in POSSIBLE_INPUT_LIST:
            print("Invalid response. Please enter either 'y, n, yes, or no'")
            needs_delivery = input("Do you require delivery? (Y/N) ").lower()

        is_tuesday = input("Is today Tuesday? (Y/N)").lower()
        while is_tuesday not in POSSIBLE_INPUT_LIST:
            print("Invalid response. Please enter either 'y, n, yes, or no'")
            is_tuesday = input("Is today Tuesday? ").lower()

        used_app = input("Did you use our mobile app for ordering? (Y/N)").lower()
        while used_app not in POSSIBLE_INPUT_LIST:
            print("Invalid response. Please enter either 'y, n, yes, or no'")
            used_app = input("Did you use our mobile app for ordering? ").lower()

        total_price = calculate_total_price(num_of_pizzas, needs_delivery, is_tuesday, used_app)
        print(f"The total cost of your order is: £{total_price:.2f}")

        another_order = input("\nWould you like to place another order? (Y/N) ").lower()
        if another_order not in ['y', 'yes']:
            break

main()
