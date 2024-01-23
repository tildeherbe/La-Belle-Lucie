import random
from cardBegin import *

def cardShuffle(cardArray):
    random.shuffle(cardArray)
    shuffledTableau = []

    for i in range(0, len(cardArray), 3):
        card0 = cardArray[i]
        try:
            card1 = cardArray[i + 1]
        except:
            shuffledTableau.append([card0])
            return shuffledTableau
        try:
            card2 = cardArray[i + 2]
        except:
            shuffledTableau.append([card0, card1])
            return shuffledTableau
        shuffledTableau.append([card0, card1, card2])
    return shuffledTableau 


