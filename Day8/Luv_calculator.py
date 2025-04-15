def calculate_love_score(name1 , name2):
    sum = 0
    for i in range(len(name1)):
        count = 0
        for j in range(len(name2)):
            if name1[i] == name2[j]:
                count += 1
            else:
                None
        sum += count
        print(f"{name1[i]} occurs {count} times")
    
    



calculate_love_score(name1 = 'Kanye West', name2 = 'Kim Kardashian')