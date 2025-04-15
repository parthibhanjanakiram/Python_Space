def life_in_weeks(age):
    total_lifetime = 90*52
    
    spent_lifetime = age*52
    
    Remaining_lifetime = total_lifetime - spent_lifetime
    
    print(f"You have {Remaining_lifetime} weeks left.")
    
    
    
age = int(input("What is your current age?"))

life_in_weeks(age)