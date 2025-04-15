def is_prime(num):
    i = 1
    count = 0
    
    while i <= num:
        
        if num % i == 0:
            count += 1
        else:
            None      
        i += 1
        
    if count == 2:
        return True
    else:
        return False

print(is_prime(73))