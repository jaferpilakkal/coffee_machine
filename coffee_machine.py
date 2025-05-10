MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
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
    "coffee": 100
}
collected_money = 0

def bill(pennies, nickels, dimes, quarters):
    return pennies * 0.01 + nickels * 0.05 + dimes * 0.10 + quarters * 0.25

def available(drink):
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry. The {item} is not enough")
            return False
    return True



# TODO: 1 ask user what would you like? print as per the input and after coffee dispensed keep asking for the next user
working = True
while working:

    user_selection = input("What would You like? espresso/latte/cappuccino: ").lower()

#TODO: 2 turn off the app by pressing off
    if user_selection == "off".lower():
        working = False
        continue

#TODO: 3 when user types report , print report of available resources
    if user_selection == "report".lower():
        for key,value in resources.items():
            print(f"{key} : {value} ml")
        print(f"Collected Money : ${collected_money}")
        continue

    if user_selection not in MENU:
        print("invalid Input. Select a drink: espresso/latte/cappuccino")
        continue

#TODO: 4 Check resources sufficient or not, if not sufficient, print " sorry there is not enough water" and ask for another item
 # TODO: 5 if there are sufficient resources , prompt for coin inputs, each coin and check whether coins sufficient after adding the values. Add the money to the report and if coins are more print "her is the change"

    if available(user_selection):
        try:
            print("Please insert your coins.")
            penny = int(input("how many pennies?: "))
            nickel = int(input("how many nickels?: "))
            dime = int(input("how many dimes?: "))
            quarter = int(input("how many quarters?: "))
        except ValueError:
            print("Invalid input. Transaction cancelled.")
            continue

        # TODO: 6 make the coffee is and print "here is your latte. enjoy", then deduct the resources used from resources
        total_coins = bill(penny,nickel,dime,quarter)

        if total_coins >= MENU[user_selection]['cost']:
            collected_money += MENU[user_selection]['cost']
            for key in MENU[user_selection]["ingredients"]:
                resources[key] -= MENU[user_selection]["ingredients"][key]
            if total_coins > MENU[user_selection]['cost']:
                change = total_coins - MENU[user_selection]['cost']
                print(f"Here is your change: ${round(change, 2)}")
            print(f"Here is your {user_selection}. Enjoy")
        elif total_coins < MENU[user_selection]['cost']:
            print("Sorry. That's not enough money. Money refunded")

            











