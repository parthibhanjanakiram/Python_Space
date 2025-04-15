import random
print("Welcome to the PyPassword Generator!")

list_pass = []

letters = input("How many letters would you like in your password?\n")

for i in range(1,int(letters)):
    if(i < len(letters)/2):
        list_pass.append(chr(random .randint(ord('a'), ord('z'))))
    else:
        list_pass.append(chr(random .randint(ord('A'), ord('Z'))))
        
# symbols = input("How many symbols would you like?")



# numbers = input("How many numbers would you like?")

print(list_pass)