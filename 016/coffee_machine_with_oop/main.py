from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()

run_machine = True

while run_machine == True:
    order = input(f"What would you like?({menu.get_items()}): ").lower()
    if order == "off":
        run_machine = False
    elif order == "report":
        machine.report()
        money_machine.report()
    else:
        current_drink = menu.find_drink(order)
        if machine.is_resource_sufficient(current_drink) and money_machine.make_payment(current_drink.cost):
                machine.make_coffee(current_drink)
            


