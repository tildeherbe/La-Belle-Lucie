from cardBegin import *
from cardShuffle import *

def getMoveableCards(cardArray):
    moveableCards = []
    for i in range(len(cardArray)):
        # items formatted [ !!this is item[ [10, C], [2, H], ~~go here[4, D]~~  ]!!  ]
        moveableCards.append(cardArray[i][-1])
    return moveableCards

def moveTableau(cardArray, moveableCards, stackFrom, stackTo, force):
    cardInHand = moveableCards[stackFrom].copy()
    cardPlacedOn = moveableCards[stackTo]
    if force or (cardInHand[0] == (cardPlacedOn[0] - 1) and cardInHand[1] == cardPlacedOn[1]):
        cardArray[stackTo].append(cardInHand)
        cardArray[stackFrom].pop(-1)
    return cardArray
    
def main():
    cardArray = cardShuffle(generateCards())
    i = 0
    for card in cardArray:
        print( str(i) + " " + str(card) + "\n")
        i += 1
    cardArray = moveTableau(cardArray, getMoveableCards(cardArray), 1, 0, True)
    i = 0
    for card in cardArray:
        print( str(i) + " " + str(card) + "\n")
        i += 1
        
main()