class Card_generator:
    def generate_cards(self):
        for _ in range(4):
            for suits in ['♠', '♥', '♣', '♦']:
                for values in range(2, 11):
                    yield f'{suits}{values}'
                for values in ['J', 'Q', 'K', 'A']:
                    yield f'{suits}{values}'