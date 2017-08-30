#in dieser Version kam hinzu, dass zuerst die Ränder besezt werden,
#wenn es keinen anderen sinnvollen zug gibt
import random

# CoRe
def turn(board, symbol):
    def randAction():
        while 1:
            x = random.choice(range(8))
            y = random.choice(range(8))
            if getboard(board,x,y) == '#': return (x,y)

    if getboard(board,0,0) != '#' and getboard(board,1,1) == '#':
        return(1,1)
    if getboard(board,7,0) != '#' and getboard(board,6,1) == '#':
        return(6,1)
    if getboard(board,0,7) != '#' and getboard(board,1,6) == '#':
        return(1,6)
    if getboard(board,7,7) != '#' and getboard(board,6,6) == '#':
        return(6,6)

    if getboard(board,0,0) == '#' and getboard(board,1,1) != '#':
        return(0,0)
    if getboard(board,7,0) == '#' and getboard(board,6,1) != '#':
        return(7,0)
    if getboard(board,0,7) == '#' and getboard(board,1,6) != '#':
        return(0,7)
    if getboard(board,7,7) == '#' and getboard(board,6,6) != '#':
        return(7,7)
            

    poslist1 = []
    for yp in range(8):  # prueft kombinationen nebeneinander
        enemy = 0
        own = False
        count = 0
        for xp in range(8):
            if getboard(board, xp, yp) != symbol and getboard(board, xp, yp) != '#':
                if own == True:
                    x = xp + 1
                    y = yp
                    if x >= 0 and x <= 7 and getboard(board, x, y) == '#':
                        poslist1.append([enemy, x, y])  # fuegt moeglichen zug hinzu
                enemy += 1

            elif getboard(board, xp, yp) == '#':
                if enemy >= 1:
                    count += 1

            elif getboard(board, xp, yp) == symbol:
                if enemy >= 1:
                    substractor = 1 + count + enemy  # addiert freistellen und gesetzte Steine -> abzuziehender Abstand
                    x = xp - substractor
                    y = yp
                    if x >= 0 and x <= 7 and getboard(board, x, y) == '#':
                        poslist1.append([enemy, x, y])  # fuegt moeglichen zug hinzu
                own = True
                enemy = 0

    token1 = 0
    if len(poslist1) > 0:  # filtert nach sinnvollstem zug
        print(poslist1)
        for i in range(len(poslist1)):
            if poslist1[i][0] > poslist1[i - 1][0] and i > 0:
                token1 = poslist1[i]
                print("new token", token1)
            elif i == 0:
                token1 = poslist1[i]

    poslist2 = []
    for xp in range(8):  # prueft kombinationen uebereinander
        enemy = 0
        own = False
        count = 0
        for yp in range(8):
            if getboard(board, xp, yp) != symbol and getboard(board, xp, yp) != '#':
                if own == True:
                    x = xp
                    y = yp + 1
                    if y >= 0 and y <= 7 and getboard(board, x, y) == '#':
                        poslist2.append([enemy, x, y])  # fuegt moeglichen zug hinzu
                enemy += 1

            elif getboard(board, xp, yp) == '#':
                if enemy >= 1:  # zaehlt Abstand zwischen gegnerischem und eigenem Symbol
                    count += 1

            elif getboard(board, xp, yp) == symbol:
                if enemy >= 1:
                    x = xp
                    substractor = 1 + count + enemy  # addiert freistellen und gesetzte Steine -> abzuziehender Abstand
                    y = yp - substractor
                    if y >= 0 and y <= 7 and getboard(board, x, y) == '#':
                        poslist2.append([enemy, x, y])  # fuegt moeglichen Zug hinzu
                own = True
                enemy = 0

    token2 = 0
    if len(poslist2) > 0:  # filtert nach sinnvollstem zug
        print(poslist2)
        for i in range(len(poslist2)):
            if poslist2[i][0] > poslist2[i - 1][0] and i > 0:
                token2 = poslist2[i]
                print("new token", token2)
            elif i == 0:
                token2 = poslist2[i]

        print("tokens are", token1, token2)
        if token1 != 0:
            if token1[0] > token2[0]:
                result = (token1[1], token1[2])
                return result
            elif token1[0] < token2[0]:
                result = (token2[1], token2[2])
                return result

    if token1 != 0:
        result = (token1[1], token1[2])
        return result
    if token2 != 0:
        print("taking token 2")
        result = (token2[1], token2[2])
        return result


    sidelist = [0, 7]

    for xp in sidelist: #setzt an linken, dann an rechten rand(außer ecken)
        for yp in range(1,7):
            if getboard(board,xp,yp) == '#':
                return(xp,yp)

    for yp in sidelist: #setzt an oberen, dann an unteren rand(außer ecken)
        for xp in range(1,7):
            if getboard(board,xp,yp) == '#':
                return(xp,yp)
    


    return randAction()
