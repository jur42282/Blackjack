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
    print("Vítej v BlackJacku!\nZadej počet hráčů (Max 6):")
    try:
        p_count = int(input())
    except ValueError:
        print("Zadej číslo")
        return
    if p_count < 1 or p_count > 6:
        print("Zadej číslo mezi 1 a 6")
        return

    players = [Player(f'Hráč {i+1}') for i in range(p_count)]
    for player in players:
        player.generate_hand(deck.deck)
        name = input(f"Zadej své jméno: ")
        if name != "":
            player.name = name
        else:
            player.name = f"Hráč {players.index(player)+1}"
        print(player)
        sleep(1)
        print("")
        
    dealer = Player('Dealer')
    dealer.generate_hand(deck.deck)
    print(f"{dealer.name}\nKarty: {dealer.hand[0]}, ?")
    sleep(3)
    print("")
    # Hráči
    for player in players:
        while True:
            player.hand_value = sum([card_value(card) for card in player.hand]) # Sečte hodnoty karet v listu
            print(player)
            if player.hand_value > 21:
                print(f"{player.name} přestřelil!")
                sleep(1)
                print("")
                break
            sleep(0.5)
            print(f"{player.name} hit / stand?")
            action = input().lower()
            if action == 'hit':
                player.hit(deck.deck)
                print(player)
            elif action == 'stand':
                sleep(1)
                print("")
                break
            else:
                print("Zadej hit nebo stand")
                continue
    
   # Dealer
    while True:
        dealer.hand_value = sum([card_value(card) for card in dealer.hand])
        print(dealer)
        if dealer.hand_value > 21:
            print("Dealer přestřelil!")
            sleep(1)
            print("")
            break
        if dealer.hand_value >= 17:
            print("Dealer stojí")
            sleep(1)
            print("")
            break
        if dealer.hand_value < 17:
            dealer.hit(deck.deck)
            print(dealer)
            sleep(1)
            continue

    # Vyhodnocení
    winners = 0
    for player in players:
        if player.hand_value > 21:
            continue
        if dealer.hand_value > 21 and player.hand_value <= 21:
            print(f"{player.name} vyhrál!")
            winners += 1
            sleep(1)
            print("")
        elif player.hand_value > dealer.hand_value:
            print(f"{player.name} vyhrál!")
            winners += 1
            sleep(1)
            print("")
        elif player.hand_value == dealer.hand_value:
            print(f"{player.name} push")
            winners += 1
            sleep(1)
            print("")
    if winners == 0:
        print("Dealer vyhrál!")
        sleep(1)
        print("")

            

def card_value(card):
    if card[1].isdigit(): # metoda checkuje jestli je hodnota číslo, vrací T/F 
        return int(card[1:])
    if card[1] == 'A': # Eso = 11 
            return 11
    return 10 # J, Q, K = 10

deck= Deck()
# print(deck.deck)
main()