import random
import emoji
import art

def deal_card():
    print(art.art)
    cards  = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return emoji.emojize("Draw :upside_down_face:", language="alias")
    elif c_score == 0:
        return emoji.emojize("Lose, opponent has Blackjack :cry:", language="alias")
    elif u_score == 0:
        return emoji.emojize("You Win with a Blackjack :sunglasses:", language="alias")
    elif u_score > 21:
        return emoji.emojize("You went over. You Lose :sob:", language="alias")
    elif c_score > 21:
        return emoji.emojize("Opponent went over, You Win :grin:", language="alias")
    elif u_score > c_score:
        return emoji.emojize("You Win :smiley:", language="alias")
    else:
        return emoji.emojize("You Lose :triumph:", language="alias")
    
def play_game():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards : {user_cards}, current score : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get an another card, Type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards : {user_cards}, final score: {user_score}")
    print(f"Computer final cards : {computer_cards}, final score: {computer_score}")
    print(compare(user_score , computer_score))

while input("Do you want to play game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)
    play_game()