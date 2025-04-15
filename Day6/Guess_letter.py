import random

list = ['camel' , 'elephant' , 'lion' , 'tiger']

Guess_word = random.choice(list)

print("Guess the word!")

Your_letter = input("Type your guessed letter : ").lower()

present = False

for i in range(len(Guess_word)):
    
    if(Your_letter == Guess_word[i]):
        present = True
        
if present:
    print(Guess_word)
    print("Right")
else:
    print(Guess_word)
    print("Wrong")