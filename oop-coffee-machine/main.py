from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Program Requirements
#TODO: 1. Print report

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

money_machine.report()
coffee_maker.report()

#TODO: 2. Check resources sufficient?
#TODO: 3. Process coins
#TODO: 4. Check transaction successful?
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)