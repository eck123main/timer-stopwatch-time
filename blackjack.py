import random
values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6,"7": 7, "8": 8, "9": 9, "10": 10,"J": 10, "Q": 10, "K": 10,"A": 11}

def ace_calc(total,ace):
    while total > 21 and ace > 0:
        total -= 10
        ace -= 1
    return total, ace

def player_turn(deck):
    total = 0
    ace = 0
    hand = []


    for i in range(2):
        card = deck.pop()
        hand.append(card)
        total += values[card]
        if card == "A":
            ace += 1

    total, ace = ace_calc(total, ace)



    print(f"Your total is now: {total}")
    print(f"Your hand: {hand}")

    while total < 21:
        hit = input("Would you like to hit? If so type yes: ").lower()
        if hit != "yes":
            break
        
        card = deck.pop()
        hand.append(card)
        total += values[card]
        
        if card == "A":
            ace += 1
        total, ace = ace_calc(total, ace)
        
        print(f"Your hand: {hand}, total: {total}")
        if total >= 21:
            break

    if total == 21:
        print("Blackjack! You hit 21")
    elif total > 21:
        print("You busted!")

    return total, hand

def dealer_turn(deck, player_total, dealer_hand):
    total = values[dealer_hand[0]]  # value of the first card
    ace = 0
    if dealer_hand[0] == 'A':
        ace = 1
    
    total, ace = ace_calc(total, ace)
    
    print("\nDealers turn\n")


    second_card = deck.pop()
    dealer_hand.append(second_card)
    total += values[second_card]
    if second_card == 'A':
        ace += 1
    total, ace = ace_calc(total, ace)


    print(f"Dealer second hard: {second_card}")
    print(f"Dealer total is now: {total}")
    print(f"Dealers hand: {dealer_hand}")
    print(f"Player total to beat: {player_total}\n")

    while total < 17:
        card = deck.pop()
        dealer_hand.append(card)
        total += values[card]
        if card == "A":
            ace += 1
        total, ace = ace_calc(total, ace)
        print(f"Dealer draws: {card}, their total now: {total}")
    
        if total >= 21:
            break
    if total == 21:
        print("dealer hit 21")
    elif total > 21:
        print("Dealer busted")
    
    print(f"Dealer final total: {total}")
    return total, dealer_hand

def main():
    
    deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] * 4 # full deck
    random.shuffle(deck)
    
    dealer_hand = [deck.pop()]
    print(f"Dealer shows: {dealer_hand[0]}")
    print("Other card remains hidden")


    player_total, player_hand = player_turn(deck)
    
    if player_total > 21: # plaeyer bust
        print("player busted, dealer wins")
        return  
    

    dealer_total, dealer_hand = dealer_turn(deck, player_total, dealer_hand)

    if dealer_total > 21: # dealer bust
        print("dealer busted, player wins")
        return  
        

    print("\nfinal results")
    print(f"Player hand: {player_hand}, total: {player_total}")
    print(f"Dealer hand: {dealer_hand}, total: {dealer_total}")

    if dealer_total > player_total:
        print("Dealer wins!")
    elif dealer_total == player_total:
        print("Tie! no win")
    else:
        print("Player wins!")
        

if __name__ == "__main__":
    main()