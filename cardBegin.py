def generateCards():
    baseCardArray = []
    for i in range(1,14):
        baseCardArray.append([i, 'S'])
        baseCardArray.append([i, 'C'])
        baseCardArray.append([i, 'H'])
        baseCardArray.append([i, 'D'])
        
    return baseCardArray


