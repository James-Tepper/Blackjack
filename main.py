'''
Everything is still in the works
Any changes or optimizations are highly appreciated!
'''

#RESET PAYOUTS!!!

import random
import sys
import time
from dataclasses import dataclass

from numpy import append


ACE_CARD = object()
#MAKE ACE CARDS AN OBJECT

class Player:

    def __init__(self , name) -> None:
        self.name : str = name
        self.bets : int = 0
        self.hand : list[Card] = []
        self.chips : int = 500
        self.still_in : bool = True

#check if ace is in hand
    def check_for_ace(self): #IMPLEMENT and OPTIMIZE
        #Hardcodes to make the value 1 (FIX)
        total_value = sum(self.hand.value)

        if total_value > 21:

            for card in self.hand:

                if card.suit == "ace":

                    card.value = 1
            
                else:
                    continue

            return self

        else:
            return

#output hand
    def print_hand(self):

        total_value = 0

        print(f'''
{self.name}'s Cards:''')

        for card in self.hand:

            total_value += card.value

            print(f'''
Suit: {card.suit}
Value: {card.value}'''.replace("_", " ").title()) 
        print(f'''
Total Value: {total_value}''')

        return

    def reset(self , dealer_hand):

        for card in self.hand:

            #fix later
            if card.value == "ace":
                card.value = 11

            DECK.append(card)

        for card in dealer_hand:

            if card.value == "ace":
                card.value = 11
            
            DECK.append(card)

        for player in self:

            player.bets = 0
            player.still_in = True

        return

'''ADD A SUM PART'''

 ###   MAYBE PASS IN ACE_CARD OBJECT


            


                #ACE == 1
                #continue


@dataclass
class Card:

    suit: str
    value: int

    def __getitem__(self) -> str:
        return f'''
Suit: {self.suit}
Value: {self.value}'''


DECK : list[Card] = [
    
    Card(suit="ace_of_spades", value=11),        # or 1
    Card(suit="ace_of_hearts", value=11),        # or 1
    Card(suit="ace_of_clubs", value=11),         # or 1
    Card(suit="ace_of_diamonds", value=11),      # or 1

    Card(suit="jack_of_spades", value=10),
    Card(suit="jack_of_hearts", value=10),
    Card(suit="jack_of_clubs", value=10),
    Card(suit="jack_of_diamonds", value=10),

    Card(suit="king_of_spades", value=10),
    Card(suit="king_of_hearts", value=10),
    Card(suit="king_of_clubs", value=10),
    Card(suit="king_of_diamonds", value=10),

    Card(suit="queen_of_spades", value=10),
    Card(suit="queen_of_hearts", value=10),
    Card(suit="queen_of_clubs", value=10),
    Card(suit="queen_of_diamonds", value=10),

    Card(suit="two_of_spades", value=2),
    Card(suit="two_of_hearts", value=2),
    Card(suit="two_of_clubs", value=2),
    Card(suit="two_of_diamonds", value=2),

    Card(suit="three_of_spades", value=3),
    Card(suit="three_of_hearts", value=3),
    Card(suit="three_of_clubs", value=3),
    Card(suit="three_of_diamonds", value=3),

    Card(suit="four_of_spades", value=4),
    Card(suit="four_of_hearts", value=4),
    Card(suit="four_of_clubs", value=4),
    Card(suit="four_of_diamonds", value=4),

    Card(suit="five_of_spades", value=5),
    Card(suit="five_of_hearts", value=5),
    Card(suit="five_of_clubs", value=5),
    Card(suit="five_of_diamonds", value=5),

    Card(suit="six_of_spades", value=6),
    Card(suit="six_of_hearts", value=6),
    Card(suit="six_of_clubs", value=6),
    Card(suit="six_of_diamonds", value=6),

    Card(suit="seven_of_spades", value=7),
    Card(suit="seven_of_hearts", value=7),
    Card(suit="seven_of_clubs", value=7),
    Card(suit="seven_of_diamonds", value=7),

    Card(suit="eight_of_spades", value=8),
    Card(suit="eight_of_hearts", value=8),
    Card(suit="eight_of_clubs", value=8),
    Card(suit="eight_of_diamonds", value=8),

    Card(suit="nine_of_spades", value=9),
    Card(suit="nine_of_hearts", value=9),
    Card(suit="nine_of_clubs", value=9),
    Card(suit="nine_of_diamonds", value=9),

    Card(suit="ten_of_spades", value=10),
    Card(suit="ten_of_hearts", value=10),
    Card(suit="ten_of_clubs", value=10),
    Card(suit="ten_of_diamonds", value=10),
]


#def start():
WELCOME_PROMPT = ('''
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


dealer_hand : list[Card] = [] 
players : list[Player] = []


'''Not implemented yet'''
# def stats(player):

#     information = print(f'''{player.hand},
# BET: {player.bet} CHIPS
# CARD NAMES: {player.hand[Card.suit]}
# CARD VALUES: {player.hand[Card.value]}''')

#     return information


def get_player_name_from_user(amount: int) -> None:

    #players : list[Player] = []
    '''^put there instead, fix later'''

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
How much would you like to bet? [Type and number between 10 and {player.chips} chips]''')))

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

        
        print(f'''
First Card''')
        Player.print_hand(player)

#Dealer takes a card
    card = random.choice(DECK)
    dealer_hand.append(card)
    DECK.remove(card)


    for player in players:

        card = random.choice(DECK)
        player.hand.append(card)
        DECK.remove(card)

        print(f'''
Starting Hand''')
        Player.print_hand(player)

    card = random.choice(DECK)
    dealer_hand.append(card)
    DECK.remove(card)
    print(f"The Dealer's second card is a {card}")

    return players , dealer_hand


def check_for_blackjack_after_draw(players):

    for player in players:

        payout = 0 

        if sum(player.hand.value) == 21:
    #ADD ARGS!!!!!!!!!!!!!!!!!!!
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

        payout = 0

        while player.still_in == True:         #loop 1

            hit_or_stand = input(
f'''
{Player.print_hand(player)})
{player.name}'s accumulated value is {sum(player.hand.card.value)}
Would you like to Hit or Stand?\n''').upper()

            if not hit_or_stand == "HIT" or "STAND":
                print("Invalid Input")
                continue

            else:

                if hit_or_stand == "STAND":
                    print(f'''{player.name} has chosen to stand.
Your total is {sum(player.hand.card.value)}''')
                    break

                elif hit_or_stand == "HIT":

                    #def hit(player)

                    card = random.choice(DECK)
                    player.hand.append(card)
                    print(f'''You have drawn a {player.hand.card.suit[-1]}''')


                    if sum(player.hand.card.value) > 21:
                        print(f'''{player.name} has BUSTED...
    You have lost {player.bets} chip bet''')
                        player.still_in = False

                        break


                    elif sum(player.hand.card.value) == 21:
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

        if sum(dealer_hand.card.value) > sum(player.hand.card.value):

            print(f'''
{player.name}'s Total {sum(player.hand.card.value)} 
Dealer's Total: {sum(dealer_hand.card.value)}
You lose your {player.bets} chip bet''')
            player.still_in = False

        else:
            continue

    while player.still_in == True: #checks if list is empty 

        print(f'''The Dealer has a {dealer_hand.card.suit}
Dealer Total: {sum(dealer_hand.card.value)}''')

        if sum(dealer_hand.card.value) == 21:

            print("The Dealer has a Blackjack!!!")

            for player in player:
                print(f"{player.name} has lost {player.bet} chips")
                player.still_in = False

            break

        elif sum(dealer_hand.card.value) <= 16:

            print(f'''
Dealer Total: {sum(dealer_hand.card.value)}
The dealer has to draw a card!!!''')

            card = random.choice(DECK)
            dealer_hand.append(card)
            DECK.remove(card)

            print(f'''The dealer has drawn a {dealer_hand.card.suit[-1]}''')

            break

        else:
            print(f'''
The Dealer has to stand...
Dealer's Card Value: {dealer_hand.card.value}''')

            return players , dealer_hand



def final_part(players , dealer_hand):
    
    for player in players:

        payout = 0

        if sum(dealer_hand.card.value) > sum(player.hand(Card.value)):

            print(f'''
{player.name}'s Total {sum(player.hand(Card.value))} 
Dealer's Total: {sum(dealer_hand.card.value)}
You lose your {player.bets} chip bet''')
            player.still_in = False 

        elif sum(sum(dealer_hand.card.value)) == sum(player.hand.card.value):
            print(f'''
{player.name} has the same total value as the Dealer
You break even.''')
            player.chips += player.bet

        else:
            print(f'''
{player.name}'s Total Value: {player.hand.card.value})
Dealer's Total Value: {dealer_hand.card.value})
{player.name} has won {player.bet * 2}!!!''')
            payout = player.bet * 2
            player.chips += payout

        player.still_in = False
        continue

    return player



def post_game(players , dealer_hand):

    for player in players:

        print(f'''
{player.name}'s Total Chips: {player.chips}''')

    Player.reset(players , dealer_hand)

    return players


'''
main functions needs some work 
'''

def gradually_print(output: str):
    for char in output:
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()




def main(): #Inconsistencies in functions CHECK

    ###gradually_print(WELCOME_PROMPT)

    #Make get_amount_of_players function
    while True:

        try:
            amount = int(input("How many people will be playing? [Min 1, Max 7]: \n"))

            if amount >= 1 and amount <=7: 
                break

            else:
                print("INVALID NUMBER OF PLAYERS")
                continue

        except ValueError:
            print("INVALID INPUT")

            
    get_player_name_from_user(amount)
    bet(players)
    shuffle()
    draw(players , dealer_hand)
    check_for_blackjack_after_draw(players)
    hit_or_stand(players) 
    end_game(players , dealer_hand)
    final_part(players, dealer_hand)
    post_game(players , dealer_hand)
        #also resets game
    return 0

if __name__ == "__main__":
        raise SystemExit(main())





