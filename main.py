# Ingredients description for each drink as dictionary
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

# Initial amount of resource
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Initial amount of profit
profit = 0.00

# TODO: 3. After a 'drink' is selected, it will confirm if the remaining resources are sufficient.
#  if not, it will print 'Sorry, there is not enough {resource}'
# Function that compares the amount of resources left to the ordered drink
def enough_resource(ordered_ingred):
    """Determine if order can proceed with True or False"""
    # Start the loop as True
    enough_ingred = True
    # For the ingredient item in choice_of_drink ordered_ingred
    for item in ordered_ingred:
        # If the ingredient in the ordered_ingred is greater or equal to the ingredient in the storage resources
        if ordered_ingred[item] >= resources[item]:
            # Print out a statement that says:
            print(f"Sorry, there is not enough {item}.")
            # Convert enough_ingred to False which will stop the program
            enough_ingred = False
    # Return a boolean statement as enough_ingred
    return enough_ingred

# TODO: 4. Create input for each individual coin that has been inserted
# Function that finds the sum of USD coins
def process_coins():
    """Return the total calculated from coins inserted."""
    print('Please insert coins.')
    # TODO: 4.1 Sum up the coins and compare it with the 'drink' price. If it is insufficient,
    #  print out 'Sorry that's not enough money. Money refunded."
    total = int(input("How Many $1.00 coin(s)?: "))
    total += int(input("How Many $0.50 coin(s)?: ")) * .5
    total += int(input("How Many $0.20 coin(s)?: ")) * .2
    total += int(input("How Many $0.10 coin(s)?: ")) * .1
    return total


# Function to see if the transaction is successful
def is_trans_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if not enough money"""
    # TODO: 4.2 If more than sufficient, then the sum of the coins will be subtracted from the price of the 'drink'
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"Here's ${change} returned")
        return True
    else:
        print("Sorry but you did not put enough coins in.  Money refunded.")
        return False

def make_coffee(drink_name, order_ingred):
    """Deduct the required ingredients from the resource."""
    for item in order_ingred:
        resources[item] -= order_ingred[item]
    print(f"Here is your {drink_name}")

# TODO: 1. Print a copy of all the resources

# TODO: 2. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# TODO: 2.1 create a new variable called 'drink' & convert the input text to lower case

# Start the while loop as True
operating = True

while operating:
    drink = (input("What would you like? (espresso/latte/cappuccino):")).lower()
    if drink == 'latte' or drink == 'espresso' or drink == 'cappuccino':
        # print(drink)
        choice_of_drink = MENU[drink]
        if enough_resource(choice_of_drink["ingredients"]):
            payment = process_coins()
            # TODO: 5. Once the drink is served, subtract the materials used from resource and add the cost of drink
            #  to the sum of 'Money'
            if is_trans_successful(payment, choice_of_drink["cost"]):
                make_coffee(drink, choice_of_drink["ingredients"])

    # TODO: 2.2 If the input text == 'report', then it will print a report that shows the current resource values
    elif drink == 'report': # To generate a report of current material resources
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    # TODO: 2.3 If the input text == 'off', then it will print 'the system is shutting down. goodbye.'
    elif drink == 'off': # For maintenance
        operating = False
    else:
        print('Your drink is not listed')



