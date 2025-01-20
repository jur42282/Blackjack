from random import shuffle
from time import sleep

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_value = 0 # Sečte hodnoty karet v ruce 

    def generate_hand(self, deck):
        self.hand = deck[:2]
        del deck[:2] # Operátor del odstraňuje první 2 karty z decku

    def hit(self, deck):
        self.hand.append(deck[0])
        del deck[0]
    
    def stand(self):
        pass

    def __str__(self):
        return f"Hráč: {self.name}\nKarty: {self.hand}"

class Deck:
    def __init__(self):
        self.deck = []
        self.generate_deck()

    def generate_deck(self):
        self.deck = []
        for _ in range(4):
            for suits in ['♠', '♥', '♣', '♦']:
                for values in range(2, 11):
                    self.deck.append(f'{suits}{values}')
                for values in ['J', 'Q', 'K', 'A']:
                    self.deck.append(f'{suits}{values}')
        shuffle(self.deck)

def main():
    print("Vítej v BlackJacku!\nZadej své jméno:")
    player = Player(input())
    dealer = Player("Dealer")
    player.generate_hand(deck.deck)
    dealer.generate_hand(deck.deck)
    print(f"Karta dealera: {dealer.hand[0]}")

    while True: # Hráčova smyčka 
        print(player)
        player.hand_value = sum([card_value(card) for card in player.hand])
        if player.hand_value > 21:
            print("Přepálil jsi!")
            print(dealer)
            exit()
        if player.hand_value <= 21:
            print("Hit/stand")
            player_choice = input()
            if player_choice == "hit":
                player.hit(deck.deck)
            elif player_choice == "stand":
                break
    while True: # Dealerova smyčka
        print(dealer)
        dealer.hand_value = sum([card_value(card) for card in dealer.hand])
        sleep(1)
        print("Dealer hraje...")
        sleep(1)
        if dealer.hand_value > 21:
            print("Dealer přepálil!")
            break
        if dealer.hand_value < 17:
            dealer.hit(deck.deck)
        if dealer.hand_value == 17:
            print("Dealer stojí")
            break
        if dealer.hand_value > 17:
            print("Dealer stojí")
            break
    # Porovnání
    # print(player.hand_value)
    # print(dealer.hand_value)
    if player.hand_value > 21:
        print("Prohrál jsi!")
    elif dealer.hand_value > 21:
        print("Vyhrál jsi!")
    elif player.hand_value > dealer.hand_value:
        print("Vyhrál jsi!")
    elif player.hand_value == dealer.hand_value:
        print("Remíza!")
    else:
        print("Prohrál jsi!")

        
    
def card_value(card):
    if card[1].isdigit(): # metoda checkuje jestli je hodnota číslo, vrací T/F 
        return int(card[1:])
    if card[1] == 'A': # Eso = 11
        return 11
    return 10 # J, Q, K = 10

deck= Deck()
# print(deck.deck)
main()