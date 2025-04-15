import random
from art import art_Guess_Num

print(art_Guess_Num)
print("Welcome Guess Number Game!!!")
print("I'm thinking of a number between 1 to 100..")

attempts = 0

comp_Guessed_Num = random.randint(1, 100)
            
def game():
    global attempts
    while attempts >= 0:
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            player_Guessed_Num = int(input("Make a guess: "))
            
            if player_Guessed_Num == comp_Guessed_Num:
                print(f"YOU WIN {player_Guessed_Num} is correct")
                break
            elif player_Guessed_Num > comp_Guessed_Num:
                print("Too High")
                attempts -= 1
            elif player_Guessed_Num < comp_Guessed_Num:
                print("Too Low")
                attempts -= 1
            else:
                print("you entered wrong input")
                break
        else:
            print(f"You have {attempts} attempts YOU LOSE, Better luck next time..")
            break
    

difficulty = input("Choose a Difficulty, Type 'Easy' or 'Hard': ").lower()

if difficulty == 'easy':
    attempts = 10
    game()
elif difficulty == 'hard':
    attempts = 5
    game()
else:
    print("Better see you again >>>..")
    
