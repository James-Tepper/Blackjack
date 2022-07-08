'''
------------------------------
Author: James Tepper
Email: jamesatepper@gmail.com
------------------------------
Everything is still in the works
Any changes or optimizations are highly appreciated!
------------------------------
TODO
Fix Reset function
Implement something that stops the game if still_in is False for everyone
Implement gradual_print
Make output more readable and organized
    remove --------- in print statements
Consider making ACEs an object
'''

import random
import sys
import time


class Player:
    '''
    User's attributes
    '''
    def __init__(self, name) -> None:
        self.name: str = name
        self.bets: int = 0
        self.hand: list[Card] = []
        self.total_card_sum: int = 0
        self.chips: int = 500
        self.still_in: bool = True

        if self.name == "Dealer":
            self.dealer_in = True


    def check_for_blackjack(self):
        '''
        Only used after draw to check for blackjack, payout 3/1
        '''
        if self.total_card_sum == 21:

            payout = self.bets * 3

            print(f'''
{self.name} has gotten a Blackjack!!!
Payout: {payout} chips!!!''')

            self.chips += payout
            self.still_in = False


    def check_for_win_loss_tie(self, dealer) -> int:
        '''
        TODO ONLY USE IF DEALER'S total is >= 17
        ONLY WHEN DEALER CAN NO LONGER HIT
        Checks Player's hand against dealer's and sees if dealer has to hit or not
        '''
        Player.calculate_card_sum(self)
        Player.calculate_card_sum(dealer)

        Player.results(self, dealer)

        #Player wins
        if dealer.total_card_sum < self.total_card_sum:

            payout = self.bets * 2
            self.chips += payout

            print(f'''
            You've Won {payout} chips!!!
            CHIPS REMAINING: {self.chips}''')
        #Player ties
        elif dealer.total_card_sum == self.total_card_sum:

            self.chips += self.bets

            print(f'''
            You break even...
            CHIPS REMAINING: {self.chips}''')
        #Player loses
        else:
            print(f'''
            {self.name} has lost their {self.bets} chip bet...)
            CHIPS REMAINING: {self.chips}''')


        self.bets = 0
        self.still_in = False


    def results(self, dealer) -> str:
        '''
        Prints player and dealer's cards and totals
        '''
        print(f'''
{self.name}'s Cards and Total:
{Player.print_just_hand(self)}
{self.total_card_sum}

Dealer's Cards Total:
{Player.print_just_hand(dealer)}
{dealer.total_card_sum}'''.title().replace("s'" , "'s"))


    def bust(self):
        '''
        Takes player out of game and removes their bet
        '''
        if self.total_card_sum > 21:

            if not self.name == "Dealer":
                print(f'''
{self.name} has busted...
CHIPS LOST: {self.bets}
CHIPS REMAINING {self.chips}''')

                self.bets = 0
                self.still_in = False

            else:
                self.dealer_in = False


    def does_player_lose_to_dealer(self , dealer) -> bool:
        '''
        Checks if dealer has higher value hand than player
        '''
        if dealer.total_card_sum > self.total_card_sum:

            print(f'''
            {self.name} has lost their {self.bets} chip bet...)
            CHIPS REMAINING: {self.chips}''')

            self.bets = 0
            self.still_in = False



    def calculate_card_sum(self) -> int:
        '''
        Calculates the sum of a hand and **checks for aces** (DOESN'T PRINT)
        '''
        self.total_card_sum = 0
        temp_sum = 0

        for card in self.hand:
            self.total_card_sum += card.value


        if self.total_card_sum > 21:

            for card in self.hand:

                if card.index == "ace":

                    card.value = 1

                temp_sum += card.value

            self.total_card_sum = temp_sum

            if self.total_card_sum > 21:
                Player.bust(self)


    def print_hand_and_sum(self) -> str:
        '''
        Outputs sum and individual cards (calculate_card_sum prior to use)
        '''
        print(f'''
{self.name}'s Total Value: {self.total_card_sum}''')

        counter = 1

        for card in self.hand:

            print(f'''
Card #{counter}: {card.index} Of {card.suit}'''.title())

            counter += 1

        return "\033[F"


    def print_just_hand(self) -> str:
        '''
        Only output cards **No values*
        '''
        counter = 1

        for card in self.hand:

            print(f'''
Card #{counter}: {card.index} Of {card.suit}'''.title())

            counter += 1


    def reset(self):
        '''
        Resets bets, still in, and cards in deck from player
        '''
        self.bets = 0
        self.total_card_sum = 0
        self.still_in = True

        for card in self.hand:

            if card.index == "ace":
                card.value = 11

            DECK.append(card.index , card.suit)



    # def get_card_names(self) -> str:
    #     '''
    #     Outputs just the name of cards. Ex. Ace, Jack, Three
    #     '''
    #     temp_list: list[str] = []

    #     for card in self.hand:

    #         temp_list.append(card.index)

    #         return ", ".join(temp_list)




class Card:
    '''
    Ex. index = Jack (key) , suit = Clubs , value = 10 (value from cardValues)
    '''
    def __init__(self, index: str, suit: str):
        self.index = index
        self.suit = suit
        self.value = cardvalues[index]

    # TODO Remove
    # def __str__(self) -> str: 
    #     return print(f'''{self.index} of {self.suit}'''.title())


cardvalues = {
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

DECK: list[Card] = []

def create_deck(cardvalues : dict[str , int], new_deck : list[Card]) -> list[Card]:
    '''
    Creates DECK of cards
    '''
    for index in cardvalues:

        for suit in ["spades", "hearts", "diamonds", "clubs"]:

            new_deck.append(Card(index, suit))


# def start():
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
            amount = int(
                input("How many people will be playing? [Min 1, Max 7]: \n"))

            if 1 <= amount <= 7:
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
    players: list[Player] = []

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
    Users place bets between 10 , max chips
    '''
    for player in players:

        if player.chips < 10:

            print(f'''
{player.name} has less an insufficient amount of chips''')
            player.still_in = False

            continue

        while True:

            try:

                place_bet = (int(input(f'''{player.name}. You have {player.chips}
How much would you like to bet? [Type and number between 10 and {player.chips} chips]:\n''')))

                if 10 <= place_bet <= player.chips:

                    player.bets = place_bet
                    player.chips -= player.bets
                    print(f'''\n{player.name} has bet {place_bet} chips!\n''')

                    break

            except ValueError:
                print("INVALID INPUT")

                continue


def deal_cards(players : list[Player], dealer : object) -> list[Card]:
    '''
    Players are dealt a card then the dealer (2x)
    Dealer's second card is shown to players
    '''
# Player takes a card
    for player in players:

        card = random.choice(DECK)  # Player picks up a card
        player.hand.append(card)  # Player puts card into their hand
        DECK.remove(card)  # DECK removes taken card

        print(f'''------------------------------------
{player.name}'s First Card: {card.index} Of {card.suit}
''')

# Dealer takes a card
    print("The Dealer takes his first card.")
    card = random.choice(DECK)
    dealer.hand.append(card)
    DECK.remove(card)

    for player in players:

        card = random.choice(DECK)
        player.hand.append(card)
        DECK.remove(card)

        print(f'''------------------------------------
{player.name}'s Second Card: {card.index} Of {card.suit}
------------------------------------''')

        print('''
    Starting Hand''')

        Player.calculate_card_sum(player)
        Player.print_hand_and_sum(player)

    card = random.choice(DECK)
    dealer.hand.append(card)
    DECK.remove(card)
    print(f'''
Dealer's Second Card: {card.index} Of {card.suit}
------------------------------------''')

    return players, dealer


def check_for_blackjack_after_draw(players : list[Player]):
    '''
    Sees if user got a blackjack off from deal_cards
    '''
    for player in players:

        Player.check_for_blackjack(player)

    return players


def hit_or_stand(players : list[Player]):
    '''
    Prompts players to hit or stand
    '''
    for player in players:

        while player.still_in:

            Player.calculate_card_sum(player)

            user_hit_or_stand = input(f'''
{Player.print_hand_and_sum(player)}
{player.name}, Would you like to Hit or Stand?: \n'''.title().replace("s'" , "'s")).upper()

            if not user_hit_or_stand == "HIT" and not user_hit_or_stand == "STAND":

                print("Invalid Input")
                continue

            if user_hit_or_stand == "STAND":

                print(f'''
{player.name} has chosen to stand.
Your total is {player.total_card_sum}''')
                break

            if user_hit_or_stand == "HIT":

                card = random.choice(DECK)
                player.hand.append(card)

                print(f'''\n{player.name} has drawn a {card.index} Of {card.suit}'''.title())

                Player.calculate_card_sum(player)

        continue

    return players


def end_game(players : list[Player], dealer : object):
    '''
    Compares dealer's hand to players still in
    '''
    print("The Dealer reveals his hand...")

    for player in players:

        payout = 0

        if not player.still_in:
            continue

        Player.does_player_lose_to_dealer(player , dealer)

        Player.calculate_card_sum(dealer)
        Player.print_hand_and_sum(dealer)

        if 17 <= dealer.total_card_sum <= 21:
            print(f'''
        The Dealer has to stand...
        Dealer's Card Value: {dealer.total_card_sum}''')

            Player.check_for_win_loss_tie(player, dealer)

            continue

        while dealer.total_card_sum <=16:

            if dealer.total_card_sum < player.total_card_sum:

                print(f'''
Dealer's Total: {dealer.total_card_sum}
It's less than 17 so he must draw a card!''')

                card = random.choice(DECK)
                dealer.hand.append(card)
                DECK.remove(card)

                print(f'''The Dealer has drawn a {card.index} Of {card.suit}'''.title())

                Player.calculate_card_sum(dealer)
                Player.bust(dealer)
                Player.does_player_lose_to_dealer(player , dealer)

                if dealer.dealer_in is False:
                    break

            else:
                Player.check_for_win_loss_tie(player , dealer)
                break

        if dealer.dealer_in is False:

            payout = player.bets * 2
            player.chips += payout

            print(f'''
The Dealer has busted!
All players that are still in win!!!
{player.name}'s Payout: {payout} chips''')

            player.still_in = False
            continue

    return players , dealer


# def final_part(players : list[Player], dealer : object):
#     '''
#     Calls method to finalize comparing dealer and player hands
#     '''
#     for player in players:

#         Player.check_for_win_loss_tie(player , dealer)

#     return players , dealer

def checking_if_worked(players : list[Player]) -> any:
    '''
    Checking if worked...
    '''
    for player in players:

        if player.still_in is True:

            print("IT DIDN'T WORKKKKKKKK")


def post_game(players : list[Player], dealer : Player):
    '''
    Prints total chips and resets bets, still_in, and hand
    '''
    for player in players:

        print(f'''
{player.name}'s Total Chips: {player.chips}''')

        Player.reset(player)

    Player.reset(dealer)

    return players


def gradual_print(output: str):
    '''Nicer way out outputting text'''
    for char in output:
        time.sleep(0.025)
        sys.stdout.write(char)
        sys.stdout.flush()


def main():
    """
    Initializes program
    """
    #gradual_print(WELCOME_PROMPT)
    create_deck(cardvalues , DECK)
    dealer = Player("Dealer")
    amount = get_amount_of_users_playing()
    players = get_player_name_from_user(amount)

    bet(players)
    deal_cards(players, dealer)
    check_for_blackjack_after_draw(players)
    hit_or_stand(players)
    end_game(players, dealer)
    checking_if_worked(players)         #TODO (Delete)
    # final_part(players, dealer)       #TODO (Maybe remove)
    post_game(players, dealer)
    # also resets game
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
