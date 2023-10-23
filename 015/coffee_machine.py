from art import logo
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order):
    """Checks if there are enough resources to make current order"""
    ingredients_required = order["ingredients"]
    for ingredient in ingredients_required:
        if ingredients_required[ingredient] > resources[ingredient]:
            print(f"Sorry not enough {ingredient}")
            return False
    return True

run_machine = True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is your change ${change}")
        global profit # now we can make change to the 'profit' variable that is outside the scope
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
    
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Enjoy your {drink_name}☕!")

print(logo)

while run_machine == True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'off':
        run_machine = False
    elif order == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[order]
        if check_resources(drink):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])

