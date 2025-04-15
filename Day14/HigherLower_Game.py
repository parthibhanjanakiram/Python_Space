from values import top_instagram_accounts
import random

flag = True
user_score = 0

def assigning_values():
    random_value_1 = random.choice(list(top_instagram_accounts))
    random_value_2 = random.choice(list(val for val in top_instagram_accounts if val != random_value_1))
    return random_value_1,random_value_2

def make_decision(user_answer, random_value_1, random_value_2):
    
    if user_answer == "a":
        name = random_value_1
        return top_instagram_accounts[random_value_1] > top_instagram_accounts[random_value_2] , name
    elif user_answer == "b":
        name = random_value_2
        return top_instagram_accounts[random_value_2] > top_instagram_accounts[random_value_1] , name
    else:
        print("You mistyped something else, Better luck next time")
        return False , None
        
def game(flag,user_score):
    while flag:  
        random_value_1,random_value_2 = assigning_values()
        
        user_answer = input(f"which one has highest followers A:{random_value_1} or B:{random_value_2} ? : ").lower()
        
        res,name = make_decision(user_answer, random_value_1, random_value_2)
        
        if name == random_value_1:
            if res : 
                print(f"Correct {name} : {top_instagram_accounts[name]} followers > {random_value_2} : {top_instagram_accounts[random_value_2]} followers")
                print("")
                user_score += 1
            else:
                print(f"Wrong answer, Your Highest Score is : {user_score}")
                flag = False
        elif name == random_value_2:
            if res : 
                print(f"Correct {name} : {top_instagram_accounts[name]} followers > {random_value_2} : {top_instagram_accounts[random_value_2]} followers")
                print("")
                user_score += 1
            else:
                print(f"Wrong answer, Your Highest Score is : {user_score}")
                flag = False
        else:
            flag = False

start_game = input("Welcome To Higher Or Lower Game, To Start Y/N : ").lower()        

if start_game == 'y':
    game(flag,user_score)
else:
    print("Huh??, Come Again Later>>>")