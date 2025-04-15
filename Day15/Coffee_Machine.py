import math
from values import Menu

materials = {
    "Water" : 1500,
    "Milk"  : 300,
    "Coffee" : 250,
    "Money" : 0
}

# Amount receiving and Calculation
def coin_check(order_rate):
    quarters = int(input("How many quarters?: "))*0.25
    dimes = int(input("How many dimes?: "))*0.1
    nickels = int(input("How many nickels?: "))*0.05
    pennies =int(input("How many pennies?: "))*0.01
    
    total_amount = quarters+dimes+nickels+pennies
    
    if total_amount == order_rate:
        change = total_amount - order_rate
        print(f"No Change, you have given ${order_rate} correctly equals to ${order_rate}")
        return True
    elif total_amount > order_rate:
        change = math.floor((total_amount - order_rate)*100)/100
        print(f"Here is your ${change} in change.")
        return True
    else:
        print("Sorry,that's not enough money. Money Refunded")
        return False

#Report Generator     
def report():
    
    for i in materials:
        if i != 'Money' and i != "Coffee":
            print(f"{i}: {materials[i]}ml ")
        elif i == "Coffee":
            print(f"{i}: {materials[i]}mg")
        elif i == "Money":
            print(f"{i}: ${materials[i]}")

# Expresso Method   
def expresso():

    if materials["Water"] >= Menu["expresso"]["ingredients"]["Water"]:
        if materials["Coffee"] >= Menu["expresso"]["ingredients"]["Coffee"]:
            print("Please insert coins.")
            res = coin_check(Menu["expresso"]["expresso_rate"])
            if res:
                print("Here is your ☕ expresso Enjoy!")
                materials["Water"] -= Menu["expresso"]["ingredients"]["Water"]
                materials["Coffee"] -= Menu["expresso"]["ingredients"]["Coffee"]
                materials["Money"] += Menu["expresso"]["expresso_rate"]
            else:
                None
        else:
            print("Insufficient coffee")
    else:
        print("Insufficient water")

# Latte Method
def latte():
    
    
    if materials["Milk"] >= Menu["latte"]["ingredients"]["Milk"]:
        if materials["Coffee"] >= Menu["latte"]["ingredients"]["Coffee"]:
            if materials['Water'] >= Menu["latte"]["ingredients"]["Water"]:
                res = coin_check(Menu["latte"]["latte_rate"])
                if res:
                    print("Here is your ☕ latte Enjoy!")
                    materials["Milk"] -= Menu["latte"]["ingredients"]["Milk"]
                    materials["Coffee"] -= Menu["latte"]["ingredients"]["Coffee"]
                    materials["Water"] -= Menu["latte"]["ingredients"]["Water"]
                    materials["Money"] += Menu["latte"]["latte_rate"]
                else:
                    None
            else:
                print("Insufficient water")
        else:
            print("Insufficient coffee")
    else:
        print("Insufficient milk")

# Cappaccino Method
def cappuccino():
    
    
    if materials["Water"] >= Menu["cappuccino"]["ingredients"]["Water"]:
        if materials["Coffee"] >= Menu["cappuccino"]["ingredients"]["Coffee"]:
            if materials["Milk"] >= Menu["cappuccino"]["ingredients"]["Milk"]:
                res = coin_check(Menu["cappuccino"]["cappuccino_rate"])
                if res:
                    print("Here is your ☕ cappuccino enjoy!")
                    materials["Water"] -= Menu["cappuccino"]["ingredients"]["Water"]
                    materials["Coffee"] -= Menu["cappuccino"]["ingredients"]["Coffee"]
                    materials["Milk"] -= Menu["cappuccino"]["ingredients"]["Milk"]
                    materials["Money"] += Menu["cappuccino"]["cappuccino_rate"]
                else:
                    None
            else:
                print("Insufficient milk")
        else:
            print("Insufficient coffee")
    else:
        print("Insufficient water")
    

is_on = True
while(is_on):
    user_input = input("What would you to prefer? (Expresso/Latte/Cappuccino): ").lower()

    if user_input == 'report':
        report()
    elif user_input == 'expresso':
        expresso()
    elif user_input == 'latte':
        latte() 
    elif user_input == 'cappuccino':
        cappuccino()
    elif user_input == 'off':
        is_on = False
    else:
        print("I think you mistyped something else, please try again>>>")