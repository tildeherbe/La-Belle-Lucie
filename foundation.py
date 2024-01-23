# for each foundation spot we have a current card and the needed card that's 1+ the value
# of the previous card
def foundationInitialize():
    foundation = [[0, "S"], [0, "C"], [0, "H"], [0, "D"]]
    return foundation

def foundationChange(foundation, spade, club, heart, diamond):
    if spade != 0:
        foundation[0] = spade
    if club != 0: 
        foundation[1] = club
    if heart != 0:
        foundation[2] = heart
    if diamond != 0:
        foundation[3] = diamond
    return foundation

    