suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
faces = ["Jack", "Queen", "King", "Ace"]
numbered = [2, 3, 4, 5, 6, 7, 8, 9, 10]
import random
def draw():
    which_suit = random.choice(suits)
    which_type = random.choice([faces, numbered])
    which_card = random.choice(which_type)
    return which_card, "of", which_suit

draw()
draw()
draw()