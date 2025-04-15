art = '''  
             ___________
             \         /
              )_______(
              |"""""""|_.-._,.---------.,_.-._
              |       | | |               | | ''-.
              |       |_| |_             _| |_..-'
              |_______| '-' `'---------'` '-'
              )"""""""(
             /_________\
              '-------'
            .-------------.
           /_______________\
'''


print(art)
print("Welcome Bidding Auction")

Auction_List = {}

present = True

max_bid = 0
winner_name = ""

while(present):
    name = input("What is your name : ").lower()
    input_val = int(input("What is your bidding price : $ "))
    
    Auction_List.update({name : input_val})
    
    continue_auction = input("Are there any Bidders? 'yes' or 'no'\n")
    if continue_auction == 'no':
        present = False
        for key in Auction_List:
            if Auction_List[key] > max_bid:
                max_bid = Auction_List[key]
                winner_name = key
            else:
                None
    else:
        None
                
print(f"The winner is {winner_name} with a bid of ${max_bid}")
    

# other way

# max(Auction_List, key = Auction_List.get)