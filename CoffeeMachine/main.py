MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report():
    """Prints report on the available resources to make coffee"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${profit}")


def check_resources(coffee_ingredients):
    """Check if there are enough resources to make a coffee drink."""
    for item in coffee_ingredients:
        if resources[item] < coffee_ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        return True


def process_coins():
    """Calculates the total amount of coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.25
    total += int(input("How many nickles?: ")) * 0.25
    total += int(input("How many pennies?: ")) * 0.25
    return total


def update_resources(coffee_ingredients):
    """Deduct resources based on the coffee type."""
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]


# Switch to turn on/off the machine
machine_on = True
client_coins = []
client_total = 0
profit = 0

while machine_on:
    selected_coffee = input("What would you like? (espresso/latte/cappuccino): ")

    # Check if the maintainers want to turn the machine off
    if selected_coffee == "off":
        machine_on = False
    # Check if a user wants to see available resources to make a coffee drink
    elif selected_coffee == "report":
        print_report()
    else:
        selected_coffee_ingredients = MENU[selected_coffee]['ingredients']
        # Check if there are enough resources to make a coffee drink
        if check_resources(selected_coffee_ingredients):
            payment = process_coins()
            print(f"You've inserted: ${payment}")

            drink_cost = MENU[selected_coffee]['cost']
            change = round((payment - drink_cost), 2)

            if change >= 0:
                profit += drink_cost
                print(f"Here is ${change} in change.")

                update_resources(selected_coffee_ingredients)
                
                print(f"Here is your {selected_coffee}. Enjoy!")
            else:
                print("​Sorry that's not enough money. Money refunded.​")
            
            client_total = 0
            client_coins = []
    