def isSolved():
    # checks if nextFoundation is [0,0,0,0]

    # checks if there are no shuffles left and no more legal moves

def main():
    while (isSolved() == False):
        """
        while (refresh == True)
            refresh = false
            for card in foundation
                bountyArray.add(card.setvalue(card.getvalue + 1)) 
            for cardStack in tableau
                exposedArray.add(cardstack.last())
                for card in bountyArray:
                    if exposedArray.contains(card)
                            playCard(card)
                            refresh = True
                        else
                            for cards in card.cardStack().above(card) # maybe use array slicing 
                                for exposedCard in exposedArray:
                                    if ((exposedCard.value == cards.value+1) && (exposedCard.suit == cards.suit))
                                        addPossibleMoveToArray()    NOTE: BIG THING AI STUFF GOES HERE
                                                           ^--------Making good AI goes in that function
                                                                    It assigns a priority value to each possible move
                                                                    each possible move will be decided by Mr. Brazil himself
                                                                    because I don't know how this game works.
                                                                    would probably prioritize lowest cards to move first
                                                                    

                                        move(cards, exposedCard.getstack())
                                        refresh = True
        shuffle()


def move (cardToBeMoved, stackToMoveTo)
    cardInHand = cardToBeMoved.copy()
    cardToBeMoved.stack.delete(cardToBeMoved)
    stackToMoveTo.append(cardInHand)

shuffleAmt = 2

def card

def shuffle():
    if (shuffleAmt > 0):
        idfk shuffle the cards or whatever


"""
        isSolved()
    return

main()
