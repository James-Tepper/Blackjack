'''
Everything is still in the works
Any changes or optimizations are highly appreciated!
'''

import random
import sys
from dataclasses import dataclass
from time import sleep


ACE_CARD = object()


class Player:

    def __init__(self , name) -> None:
        self.name : str = name
        self.bets : int = 0
        self.hand : list[Card] = []
        self.chips : int = 500
        self.still_in : bool = True     #<--- fix


@dataclass
class Card:

    suit: str
    value: int

    def __getitem__(self) -> str:
        return f'''
Suit: {self.suit}
Value: {self.value}'''

DECK : list[Card] = [
    
    Card(suit="ace_spades", value=11),        # or 1
    Card(suit="ace_hearts", value=11),        # or 1
    Card(suit="ace_clubs", value=11),         # or 1
    Card(suit="ace_diamonds", value=11),      # or 1

    Card(suit="jack_spades", value=10),
    Card(suit="jack_hearts", value=10),
    Card(suit="jack_clubs", value=10),
    Card(suit="jack_diamonds", value=10),

    Card(suit="king_spades", value=10),
    Card(suit="king_hearts", value=10),
    Card(suit="king_clubs", value=10),
    Card(suit="king_diamonds", value=10),

    Card(suit="queen_spades", value=10),
    Card(suit="queen_hearts", value=10),
    Card(suit="queen_clubs", value=10),
    Card(suit="queen_diamonds", value=10),

    Card(suit="two_spades", value=2),
    Card(suit="two_hearts", value=2),
    Card(suit="two_clubs", value=2),
    Card(suit="two_diamonds", value=2),

    Card(suit="three_spades", value=3),
    Card(suit="three_hearts", value=3),
    Card(suit="three_clubs", value=3),
    Card(suit="three_diamonds", value=3),

    Card(suit="four_spades", value=4),
    Card(suit="four_hearts", value=4),
    Card(suit="four_clubs", value=4),
    Card(suit="four_diamonds", value=4),

    Card(suit="five_spades", value=5),
    Card(suit="five_hearts", value=5),
    Card(suit="five_clubs", value=5),
    Card(suit="five_diamonds", value=5),

    Card(suit="six_spades", value=6),
    Card(suit="six_hearts", value=6),
    Card(suit="six_clubs", value=6),
    Card(suit="six_diamonds", value=6),

    Card(suit="seven_spades", value=7),
    Card(suit="seven_hearts", value=7),
    Card(suit="seven_clubs", value=7),
    Card(suit="seven_diamonds", value=7),

    Card(suit="eight_spades", value=8),
    Card(suit="eight_hearts", value=8),
    Card(suit="eight_clubs", value=8),
    Card(suit="eight_diamonds", value=8),

    Card(suit="nine_spades", value=9),
    Card(suit="nine_hearts", value=9),
    Card(suit="nine_clubs", value=9),
    Card(suit="nine_diamonds", value=9),

    Card(suit="ten_spades", value=10),
    Card(suit="ten_hearts", value=10),
    Card(suit="ten_clubs", value=10),
    Card(suit="ten_diamonds", value=10),
]


'''
main functions needs some work 
'''
def main(): 

    how_many_players(amount)
    bet(players)
    draw(players , dealer_hand)
    post_draw(players , still_in)
    hit_or_stand(still_in)
    end_game(players , still_in , dealer_hand)
    final_part(players , still_in , dealer_hand)
    post_game(players)

#def start():
welcome_prompt = ('''
Welcome to Blackjack!
Rules: Input the amount of people playing along with your names.
From there you will be prompted to place a bet.
    Note: The minimum bet is 10 chips!
You will then be dealt two cards.
The objective of the game is for your cards to have a higher sum than the Dealer's without going over 21.
Afterwards you are prompted to either HIT or STAND
    HIT: Take another card from the deck
    STAND: Lock-in your current hand
Good luck and have fun!!!

''')

for char in welcome_prompt:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()

while True:

    try:
        amount = int(input("How many people will be playing? \n"))
    except ValueError:
        print("INVALID INPUT")

    if amount > 7 or amount <= 0:
        print("INVALID AMOUNT OF PLAYERS")
        continue

    else:
        break


dealer_hand = [] 
players : list[Player] = []

still_in : list[players] = []

'''Not implemented yet'''
# def stats(player):

#     information = print(f'''{player.hand},
# BET: {player.bet} CHIPS
# CARD NAMES: {player.hand[Card.suit]}
# CARD VALUES: {player.hand[Card.value]}''')

#     return information


def how_many_players(amount) -> int:

    for _ in range(amount):
        name = input("What is your name?").upper()
        players.append(Player(name))

    return players
    


def shuffle():    #SHUFFLING CARDS (NOT NECESSARY BUT KINDA COOL)
    random.shuffle(DECK)
    print("DEALER: Shuffling the cards!")

    return DECK
        


def bet(players):

        for player in players:

            while True:
                place_bet = (int(input(f'''{player.name}. You have {player.chips}
How much would you like to bet? [Type and number between 10 and {player.chips}]''')))

                if place_bet >= 10 and place_bet <= player.chips:
                    player.bets = place_bet
                    player.chips -= player.bets
                    print(f'''{player.name} has bet {place_bet}''')
                    break

                else:
                    print("Invalid Input")
                    continue

        return players


def draw(players , dealer_hand):

#Player takes a card
    for player in players:

        card = random.choice(DECK)      #Player picks up a card
        player.hand.append(card)        #Player puts card into their hand
        DECK.remove(card)               #DECK removes taken card

        
        print(f'''{player.name}'s first card is {player.hand[-1]}''')

#Dealer takes a card
    card = random.choice(DECK)
    dealer_hand.append(card)
    DECK.remove(card)


    for player in players:

        card = random.choice(DECK)
        player.hand.append(card)
        DECK.remove(card)

        print(str(f"{player.name}'s hand is {player.hand(Card.suit[-1])}"))

    card = random.choice(DECK)
    dealer_hand.append(card)
    DECK.remove(card)
    print(f"The Dealer's second card is a {card}")

    return players , dealer_hand


def post_draw(players):

    for player in players:

        if sum(player.hand(Card.value)) == 21:
    
            payout = player.bets * 3    #Blackjack 3/1 payout
            print(f'''{player.name} has gotten a Blackjack!!!
Payout: {payout} chips!!!''')
            player.chips += payout
            player.still_in = False
            continue
        else:
            continue

    return players



def hit_or_stand(players):

    for player in players:

        while player.still_in == True:         #loop 1

            hit_or_stand = input(f'''{player.name}, 
You have a {player.hand(Card.suit)})
Your accumulated value is {sum(player.hand(Card.value))}
Would you like to Hit or Stand?\n''').upper()

            if not hit_or_stand == "HIT" or "STAND":
                print("Invalid Input")
                continue

            else:

                if hit_or_stand == "STAND":
                    print(f'''{player.name} has chosen to stand.
Your total is {sum(player.hand(Card.value))}''')
                    break

                elif hit_or_stand == "HIT":

                    #def hit(player)

                    card = random.choice(DECK)
                    player.hand.append(card)
                    print(f'''You have drawn a {player.hand(Card.suit[-1])}''')


                    if sum(player.hand(Card.value)) > 21:
                        print(f'''{player.name} has BUSTED...
    You have lost {player.bets} chip bet''')
                        player.still_in = False

                        break


                    elif sum(player.hand(Card.value)) == 21:
                        print(f'''{player.name} has gotten 21!!!''')
                        payout = player.bets * 2
                        player.chips += payout
                        player.still_in = False

                        break


                    else:
                        continue

    return players


def end_game(players , dealer_hand):

    for player in players:  # checks if dealer wins by default

        if sum(dealer_hand(Card.value)) > sum(player.hand(Card.value)):

            print(f'''
{player.name}'s Total {sum(player.hand(Card.value))} 
Dealer's Total: {sum(dealer_hand(Card.value))}
You lose your {player.bets} chip bet''')
            player.still_in = False

        else:
            continue

    while player.still_in == True: #checks if list is empty 

        print(f'''The Dealer has a {dealer_hand(Card.suit)}
Dealer Total: {sum(dealer_hand(Card.value))}''')

        if sum(dealer_hand(Card.value)) == 21:

            print("The Dealer has a Blackjack!!!")

            for player in still_in:
                print(f"{player.name} has lost {player.bet} chips")
                player.still_in = False

            break

        elif sum(dealer_hand(Card.value)) <= 16:

            print(f'''
Dealer Total: {sum(dealer_hand(Card.value))}
The dealer has to draw a card!!!''')

            card = random.choice(DECK)
            dealer_hand.append(card)
            DECK.remove(card)

            print(f'''The dealer has drawn a {dealer_hand(Card.suit[-1])}''')

            break

        else:
            print(f'''
The Dealer has to stand...
Dealer's Card Value: {dealer_hand(Card.value)}''')

            return players , dealer_hand



def final_part(players , dealer_hand):
    
    for player in players:

        if sum(dealer_hand(Card.value)) > sum(player.hand(Card.value)):

            print(f'''
{player.name}'s Total {sum(player.hand(Card.value))} 
Dealer's Total: {sum(dealer_hand(Card.value))}
You lose your {player.bets} chip bet''')
            player.still_in = False 

        elif sum(dealer_hand(Card.value)) == sum(player.hand(Card.value)):
            print(f'''
{player.name} has the same total value as the Dealer
You break even.''')
            player.chips += player.bet

        else:
            print(f'''
{player.name}'s Total Value: {player.hand(Card.value)})
Dealer's Total Value: {dealer_hand(Card.value)})
{player.name} has won {player.bet * 2}!!!''')
            payout = player.bet * 2
            player.chips += payout

        player.still_in = False
        continue

    return player

def post_game(players):

    for player in players:

        print(f'''
{player.name}'s Total Chips: {player.chips}''')

    return players


def reset(players , dealer_hand):

    dealer_hand.clear()

    for player in players:

        player.bets = 0
        player.still_in = True
        player.hand.clear()

    return players , dealer_hand



if __name__ == "__main__":
    raise SystemExit(main())




