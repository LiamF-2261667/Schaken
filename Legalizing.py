from Piece import GetPieceType, GetPieceColor, PieceNameToLetter


def isLegal(currHor, currVer, destHor, destVer, type, color):
    if currHor == destHor and currVer == destVer:
        return "no movement"

    # Informatie over de nieuwe plaats verzamelen
    destTypeStr = GetPieceType(destHor, destVer)

    # Enkel uitvoeren als er al een stuk staat op de verlangde positie
    if destTypeStr != "null":
        destColorStr = GetPieceColor(destHor, destVer)

        # Als het stuk dat wordt genomen van uw eigen kleur is, mag dat niet
        if destColorStr == color:
            return "taking self"
        else:
            if type == "P":
                return movePawn(currHor, currVer, destHor, destVer, color, True)
    
    # Kijken of de zet mogelijk is volgens het type stuk
    if type == "K":
        return moveKing(currHor, currVer, destHor, destVer)

    elif type == "Q":
        return moveQueen(currHor, currVer, destHor, destVer)

    elif type == "B":
        return moveBishop(currHor, currVer, destHor, destVer)

    elif type == "H":
        return moveHorse(currHor, currVer, destHor, destVer)

    elif type == "R":
        return moveRook(currHor, currVer, destHor, destVer)

    elif type == "P":
        return movePawn(currHor, currVer, destHor, destVer, color, False)
    
    print(str(type))


def moveKing(currHor, currVer, destHor, destVer):
    deltaX = abs(currHor - destHor)
    deltaY = abs(currVer - destVer)

    if deltaX > 1 or deltaY > 1:
        return "illegal"
     
    return "legal"


def moveQueen(currHor, currVer, destHor, destVer):
    deltaX = destHor - currHor
    deltaY = destVer - currVer

    if deltaX == 0 or deltaY == 0:
        if deltaX > 0:
            for i in range(currHor + 1, destHor):
                if GetPieceType(i, currVer) != "null":
                    return "blocked"
    
        if deltaX < 0:
            for i in range(destHor + 1, currHor):
                if GetPieceType(i, currVer) != "null":
                    return "blocked"

        if deltaY > 0:
            for i in range(currVer + 1, destVer):
                if GetPieceType(currHor, i) != "null":
                    return "blocked"

        if deltaY < 0:
            for i in range(destVer + 1, currVer):
                if GetPieceType(currHor, i) != "null":
                    return "blocked"

        return "legal"

    rico = deltaY/deltaX
    
    if abs(rico) == 1:
        j = 0
        if deltaX > 0:
            if deltaY > 0:
                for i in range(currHor + 1, destHor):
                    j += 1
                    if GetPieceType(i, currVer + j) != "null":
                        return "blocked"

            if deltaY < 0:
                for i in range(currHor + 1, destHor):
                    j += 1
                    if GetPieceType(i, currVer - j) != "null":
                        return "blocked"
        
        if deltaX < 0:
            if deltaY > 0:
                for i in range(destHor + 1, currHor):
                    j += 1
                    if GetPieceType(i, destVer - j) != "null":
                        return "blocked"
            if deltaY < 0:
                for i in range(destHor + 1, currHor):
                    j += 1
                    if GetPieceType(i, destVer + j) != "null":
                        return "blocked"
        
        return "legal"

    return "illegal"

def moveBishop(currHor, currVer, destHor, destVer):
    deltaX = destHor - currHor
    deltaY = destVer - currVer

    if deltaX == 0:
        return "illegal"
    
    rico = deltaY/deltaX

    if abs(rico) != 1:
        return "illegal"

    j = 0
    if deltaX > 0:
        if deltaY > 0:
            for i in range(currHor + 1, destHor):
                j += 1
                if GetPieceType(i, currVer + j) != "null":
                    return "blocked"

        if deltaY < 0:
            for i in range(currHor + 1, destHor):
                j += 1
                if GetPieceType(i, currVer - j) != "null":
                    return "blocked"
    
    if deltaX < 0:
        if deltaY > 0:
            for i in range(destHor + 1, currHor):
                j += 1
                if GetPieceType(i, destVer - j) != "null":
                    return "blocked"
        if deltaY < 0:
            for i in range(destHor + 1, currHor):
                j += 1
                if GetPieceType(i, destVer + j) != "null":
                    return "blocked"

    return "legal"

def moveHorse(currHor, currVer, destHor, destVer):
    deltaX = abs(currHor - destHor)
    deltaY = abs(currVer - destVer)

    if deltaX == 2 and deltaY == 1:
        return "legal"

    if deltaY == 2 and deltaX == 1:
        return "legal"
    
    return "illegal"

def moveRook(currHor, currVer, destHor, destVer):
    deltaX = destHor - currHor
    deltaY = destVer - currVer

    if deltaX > 0:
        for i in range(currHor + 1, destHor):
            if GetPieceType(i, currVer) != "null":
                return "blocked"
    
    if deltaX < 0:
        for i in range(destHor + 1, currHor):
            if GetPieceType(i, currVer) != "null":
                return "blocked"

    if deltaY > 0:
        for i in range(currVer + 1, destVer):
            if GetPieceType(currHor, i) != "null":
                return "blocked"

    if deltaY < 0:
        for i in range(destVer + 1, currVer):
            if GetPieceType(currHor, i) != "null":
                return "blocked"

    if deltaX == 0 or deltaY == 0:
        return "legal"
    
    return "illegal"

def movePawn(currHor, currVer, destHor, destVer, color, isTakingPiece):
    deltaX = abs(currHor - destHor)
    deltaY = currVer - destVer

    if isTakingPiece == False and deltaX != 0:
        return "illegal"

    if isTakingPiece == True and deltaX == 1:

        if color == "white" and deltaY == -1:
            return "legal"

        if color == "black" and deltaY == 1:
            return "legal"
        
        return "illegal"

    if color == "white":
        if GetPieceType(destHor, destVer) != "null":
            return "blocked"

        if deltaY == -1:
            return "legal"
        
        if currVer == 2:
            if deltaY == -2:
                return "legal"

    if color == "black":
        if GetPieceType(destHor, destVer) != "null":
            return "blocked"
            
        if deltaY == 1:
            return "legal"
        
        if currVer == 7:
            if deltaY == 2:
                return "legal"
    
    return "illegal"

whiteKingHor = 5
whiteKingVer = 1

blackKingHor = 5
blackKingVer = 8

def setWhiteKingPos(hor, ver):
    global whiteKingHor
    global whiteKingVer

    whiteKingHor = hor
    whiteKingVer = ver
    
def setBlackKingPos(hor, ver):
    global blackKingHor
    global blackKingVer

    blackKingHor = hor
    blackKingVer = ver

def isKingInDanger(color):
    for i in range(1, 9):
        for j in range(1, 9):
            pieceType = GetPieceType(i, j)
            pieceColor = GetPieceColor(i, j)

            if pieceType != "null" and pieceColor != color:

                if color == "white":
                    legality = isLegal(i, j, whiteKingHor, whiteKingVer, PieceNameToLetter(pieceType), "black")

                elif color == "black":
                    legality = isLegal(i, j, blackKingHor, blackKingVer, PieceNameToLetter(pieceType), "white")

                if legality == "legal":
                    return True

    return False
