'''
Author: James Tepper
Email: jamesatepper@gmail.com
----------------------------
Everything is still in the works
Any changes or optimizations are highly appreciated!
'''





#RESET PAYOUTS!!!

import random
import sys
import time

ACE_CARD = object()
#MAKE ACE CARDS AN OBJECT

class Player:
    '''
    Defines the user
    '''

    def __init__(self , name) -> None:
        self.name : str = name
        self.bets : int = 0
        self.hand : list[Card] = []
        self.total_card_sum : int = 0
        self.chips : int = 500
        self.still_in : bool = True


    def find_sum_of_hand_and_check_for_ace(self) -> int:
        '''
        Calculate user's total card value and looks for aces if user busted
        If aces are found, they become a 1
        '''
        self.total_card_sum = 0 #to run multiple times without over adding

        for card in self.hand:

            self.total_card_sum += card.value


        if self.total_card_sum > 21:
            self.total_card_sum = 0

            for card in self.hand:

                if card.index == "ace":
                    card.value = 1

                self.total_card_sum += card.value


#output hand
    def print_hand(self) -> str:
        '''
        Outputs hand of player
        '''

        total_value = 0
        temp_suit_list = []
        temp_value_list = []

        for card in self.hand:

            total_value += card.value

            temp_suit_list.append(card.suit)
            temp_value_list.append(card.value)

        i = 1

        for suit in temp_suit_list:

            for value in temp_value_list:

                print(f'''
{self.name}:
Card #{i} {value} Of {suit}''')
                i += 1
                break

#         print(f'''
# Suit: {temp_suit_list}
# Value: {temp_value_list}'''.replace("_", " ").title())


#         print(f'''
# Total Value: {total_value}''')


    def reset(self) -> any:
        '''
        Resets bets, still in, and cards in deck from player
        '''
        self.bets = 0
        self.total_card_sum = 0
        self.still_in = True

        for card in self.hand:

            if card == "ace":
                card.value = 11
            
            DECK.append(card)



'''ADD A SUM PART'''

 ###   MAYBE PASS IN ACE_CARD OBJECT


                #ACE == 1
                #continue

class Card:
    '''
    Ex. index = Jack (key) , suit = Clubs , value = 10 (value from cardValues)
    '''
    def __init__(self, index: str, suit: str):
        self.index = index
        self.suit = suit
        self.value = cardValues[index]

    def __str__(self) -> str:
         return f'''{self.index} of {self.suit}'''.title()


cardValues = {
    "ace": 11,
    "jack": 10,
    "king": 10,
    "queen": 10,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
}


DECK : list[Card] = []

for index in cardValues:

    for suit in ["spades", "hearts", "diamonds", "clubs"]:

        DECK.append(Card(index , suit))



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


'''Not implemented yet'''
# def stats(player):

#     information = print(f'''{player.hand},
# BET: {player.bet} CHIPS
# CARD NAMES: {player.hand[Card.suit]}
# CARD VALUES: {player.hand[Card.value]}''')

#     return information

def get_amount_of_users_playing() -> int:
    '''
    Find how many users there are
    '''
    while True:

        try:
            amount = int(input("How many people will be playing? [Min 1, Max 7]: \n"))

            if amount >= 1 and amount <=7:
                break

            print("INVALID NUMBER OF PLAYERS")
            continue

        except ValueError:
            print("INVALID INPUT")

    return amount


def get_player_name_from_user(amount: int) -> list[Player]:
    '''
    Initializes Player class and stores as "players"
    '''
    players : list[Player] = []

    for i in range(amount):

        while True:

            name = input(f'''What is your name Player #{1 + i}?: 
''').title()

            if name == "Dealer":
                print("Dealer is an invalid name!")
                continue

            players.append(Player(name))
            break

    return players



def bet(players: list[Player]) -> int:
    '''
    Users place bets between 10 - max chips
    '''
    for player in players:

        if player.chips < 10:
            continue

        while True:
            place_bet = (int(input(f'''{player.name}. You have {player.chips}
How much would you like to bet? [Type and number between 10 and {player.chips} chips]''')))

            if place_bet >= 10 and place_bet <= player.chips:

                player.bets = place_bet
                player.chips -= player.bets
                print(f'''{player.name} has bet {place_bet}''')
                break

            print("Invalid Input")
            continue


def deal_cards(players , dealer) -> list[Card]:

#Player takes a card
    for player in players:

        card = random.choice(DECK)      #Player picks up a card
        player.hand.append(card)        #Player puts card into their hand
        DECK.remove(card)               #DECK removes taken card

        print('''First Card''')
        Player.print_hand(player)

#Dealer takes a card
    card = random.choice(DECK)
    dealer.hand.append(card)
    DECK.remove(card)

    for player in players:

        card = random.choice(DECK)
        player.hand.append(card)
        DECK.remove(card)

        print('''Starting Hand''')
        Player.print_hand(player)

    card = random.choice(DECK)
    dealer.hand.append(card)
    DECK.remove(card)
    print(f"\nThe Dealer's second card is a {Card.__str__(card)}")

    return players , dealer


def check_for_blackjack_after_draw(players):
    '''
    Sees if user got a 21 off from deal_cards
    '''
    for player in players:

        payout = 0

        Player.find_sum_of_hand_and_check_for_ace(player)

        if player.total_card_sum == 21:
    #ADD ARGS!!!!!!!!!!!!!!!!!!!
            payout = player.bets * 3    #Blackjack 3/1 payout

            print(f'''
{player.name} has gotten a Blackjack!!!
Payout: {payout} chips!!!''')

            player.chips += payout
            player.still_in = False
            continue

        else:
            continue

    return players



def hit_or_stand(players):
    '''
    Prompts players to hit or stand
    '''

    for player in players:

        payout = 0

        while player.still_in:         #loop 1

            Player.find_sum_of_hand_and_check_for_ace(player)

            hit_or_stand = input(
f'''
{player.name}'s Cards:
{Player.print_hand(player)})

{player.name}'s accumulated value is {player.total_card_sum}
Would you like to Hit or Stand?: \n''').upper()


            if not hit_or_stand == "HIT" or not hit_or_stand == "STAND":
                print("Invalid Input")
                continue

            if hit_or_stand == "STAND":
                print(f'''
{player.name} has chosen to stand.
Your total is {player.total_card_sum}''')
                break

            if hit_or_stand == "HIT":

                #def hit(player)

                card = random.choice(DECK)
                player.hand.append(card)
                print(f'''{player.name} has drawn a {player.hand.card.index[-1]}''')

                Player.find_sum_of_hand_and_check_for_ace(player)

                if player.total_card_sum > 21:
                    print(f'''{player.name} has BUSTED...
You have lost {player.bets} chip bet''')

                    player.still_in = False



                elif player.total_card_sum == 21:
                    payout = player.bets * 2
                    player.chips += payout
                    print(f'''
{player.name} has gotten 21!!!
Payout: {payout}''')
                    
                    player.still_in = False


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



def post_game(players : list[Player] , dealer_hand : list[Card]):


    for player in players:


        print(f'''
{player.name}'s Total Chips: {player.chips}''')
        player.reset(dealer_hand)

    Player.reset(players)

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
    """
    This is a function docstring
    """
    
    #gradually_print(WELCOME_PROMPT)
    dealer = Player("Dealer")
    amount = get_amount_of_users_playing()
    players = get_player_name_from_user(amount)
    bet(players)
    deal_cards(players , dealer)
    check_for_blackjack_after_draw(players)
    hit_or_stand(players) 
    end_game(players , dealer)
    final_part(players, dealer)
    post_game(players , dealer)
        #also resets game
    return 0

if __name__ == "__main__":
    raise SystemExit(main())





