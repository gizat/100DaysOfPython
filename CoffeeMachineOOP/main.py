from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Switch to turn on/off the machine
machine_on = True

while machine_on:
    options = menu.get_items()
    selected_coffee = input(f"What would you like? ({options}): ")

    # Check if the maintainers want to turn the machine off
    if selected_coffee == "off":
        machine_on = False
    # Check if a user wants to see available resources to make a coffee drink
    elif selected_coffee == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(selected_coffee)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)
