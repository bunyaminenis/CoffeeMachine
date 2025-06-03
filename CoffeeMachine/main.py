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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
#TODO Check if there is enough resources make the coffee
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

#TODO Calculate the entered money
def process_coins():
    pennies = 0.01
    nickles = 5*pennies
    dimes = 2*nickles
    quarters = 0.25
    amount_pennies = float(input(f"Enter the money income in Pennies: "))
    amount_nickles = float(input(f"Enter the money income in Nickles: "))
    amount_dimes = float(input(f"Enter the money income in Dimes: "))
    amount_quarters = float(input(f"Enter the money income in Quarters: "))
    cost_calculate = amount_pennies*pennies + amount_nickles*nickles + amount_dimes*dimes + amount_quarters*quarters
    return cost_calculate

#if I write in while under the 'if is_resource_sufficient(drink["ingredients"]):' it gives error for return true and false
def money_enter_transaction(money_received, coffee_cost):
    global profit
    if money_received >= coffee_cost:
        change = round(money_received - coffee_cost, 2)
        print(f"Here is the change: ${change}")
        profit += coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

#TODO When everything is right making coffee progress to calculate left resources
def make_coffee(coffee_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your coffee {coffee_name}")
    return True

#TODO If there are enough resources to make that drink, off function

turn_off = True
while turn_off:
    coffe_choice = input('“What would you like? (espresso/latte/cappuccino): ” ')
    if coffe_choice == "off":
        turn_off = False
    elif coffe_choice == "report":
        print(f"Water: {resources['water']}\n"
              f"Milk: {resources['milk']}\n"
              f"Coffee: {resources['coffee']}\n"
              f"Money : ${profit}")
    else:
        drink = MENU[coffe_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if money_enter_transaction(payment, drink["cost"]):
                make_coffee(coffe_choice, drink["ingredients"])

#if coffe_choice == "espresso" and water < 50:
#    print("Sorry there is not enough water.")
#if coffe_choice == "espresso" and coffee < 18:
#    print("Sorry there is not enough coffee.")
#
#if coffe_choice == "latte" and water < 200:
#    print("Sorry there is not enough water.")
#if coffe_choice == "latte" and coffee < 24:
#    print("Sorry there is not enough coffee.")
#if coffe_choice == "latte" and coffee < 150:
#    print("Sorry there is not enough milk.")
#
#if coffe_choice == "cappuccino" and water < 250:
#    print("Sorry there is not enough water.")
#if coffe_choice == "cappuccino" and coffee < 24:
#    print("Sorry there is not enough coffee.")
#if coffe_choice == "cappuccino" and coffee < 100:
#    print("Sorry there is not enough milk.")

#TODO coins