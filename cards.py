class Card:
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    

if __name__ == "__main__":
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    cards = []
    for value in range(1, 14):
        for suit in suits:
            card = Card(value, suit)
            cards.append(card)

    for c in cards:
        if c == 10:
            print(c)
            # Skriver ut(KAN SKRIVA UT ANNORLUNDA BASERAT PÅ DIN KLASS-IMPLEMENTATION!:
            # Clubs 10
            # Diamonds 10
            # Hearts 10
            # Spades 10

    for c in cards:
        if c > 10 and c == "Diamonds":
            print(c)

        # Jack of Diamonds
        # Queen of Diamonds 
        # King of Diamonds 


    card = Card(5, "Diamonds")
    for c in cards:
        if c == card:
            print(c)

    # Diamonds 5

    for c in cards:
        if c == 5 and c > card:
            print(c)

    # Hearts 5
    # Spades 5
