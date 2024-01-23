from cardBegin import *
from cardShuffle import *
from foundation import *

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

def moveFoundation(cardArray, foundation):
    cardWasMoved = True
    moveableCards = getMoveableCards(cardArray)
    currentFoundation = foundation
    currentCardArray = cardArray.copy()
    while cardWasMoved == True:
        bountyArray = []
        cardWasMoved = False
        for card in currentFoundation:
            bountyCard = [card[0]+1, card[1]]
            bountyArray.append(bountyCard)
        for card in bountyArray:
            for i in range(0,len(moveableCards)-1):
                if card == moveableCards[i]:
                    if card[1] == "S":
                        currentFoundation = foundationChange(currentFoundation,card,0,0,0)
                    if card[1] == "C":
                        currentFoundation = foundationChange(currentFoundation,0,card,0,0) 
                    if card[1] == "H":
                        currentFoundation = foundationChange(currentFoundation,0,0,card,0) 
                    if card[1] == "D":
                        currentFoundation = foundationChange(currentFoundation,0,0,0,card) 
                    currentCardArray = currentCardArray[i].pop(-1)
                cardWasMoved = True
    return currentCardArray, currentFoundation
    




def main():
    cardArray = cardShuffle(generateCards())
    i = 0
    for card in cardArray:
        print( str(i) + " " + str(card) + "\n")
        i += 1
    cardArray, foundation = moveFoundation(cardArray, foundationInitialize())
    i = 0
    for card in cardArray:
        print( str(i) + " " + str(card) + "\n")
        i += 1
    print(foundation)
    


if __name__ == "__main__":
    main()
