import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ["Hearts", "Diamonds", "Clubs", "Spades"] for value in range(1, 14)]

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        ace_count = 0

        for card in self.cards:
            if card.value > 10:
                value += 10
            elif card.value == 1:
                value += 11
                ace_count += 1
            else:
                value += card.value
        
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1

        return value

class Game:
    def __init__(self):
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.deck = Deck()
        self.deck.shuffle()

    def deal_initial(self):
        for i in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())

    def player_turn(self):
        while self.player_hand.get_value() < 21:
            print(f"Your hand: {self.player_hand.cards} ({self.player_hand.get_value()})")
            hit_or_stand = input("Do you want to hit or stand? ").lower()
            if hit_or_stand == "hit":
                self.player_hand.add_card(self.deck.deal())
            else:
                break

    def dealer_turn(self):
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal())

    def check_win(self):
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()

        if player_value > 21:
            print("You bust. Dealer wins.")
        elif dealer_value > 21:
            print("Dealer busts. You win!")
        elif player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("Dealer wins.")
        else:
            print("It's a tie.")

    def play_again(self):
        return input("Do you want to play again? ").lower().startswith("y")

    def play(self):
        print("Let's play BlackJet!")
        while True:
            self.deal_initial()
            self.player_turn()
            self.dealer_turn()

            print(f"Dealer's hand: {self.dealer_hand.cards} ({self.dealer_hand.get_value()})")
            self.check_win()

            if not self.play_again():
                print("Thanks for playing!")
                break

game = Game()
game.play()
