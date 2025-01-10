from card_generator import Card_generator


class Game:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        self.card_generator = Card_generator()

    def start_game(self):
        pass
class Player:
    def __init__(self):
        self.name = None
        self.hand = Hand()

class Dealer:
    def __init__(self):
        self.hand = Hand()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_hand(self):
        pass

class Deck:
    def __init__(self):
        self.cards = Card_generator().generate_cards()

    def shuffle(self):
        pass

