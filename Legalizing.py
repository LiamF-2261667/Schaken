from Piece import GetPieceType, GetPieceColor, PieceColorToCode


def isLegal(currHor, currVer, destHor, destVer, type, color):
    if currHor == destHor and currVer == destVer:
        return "no movement"

    # Informatie over de nieuwe plaats verzamelen
    destTypeStr = GetPieceType(destHor, destVer)

    # Enkel uitvoeren als er al een stuk staat op de verlangde positie
    if destTypeStr != "null":
        destColorStr = GetPieceColor(destHor, destVer)
        destColor = PieceColorToCode(destColorStr)

        # Als het stuk dat wordt genomen van uw eigen kleur is, mag dat niet
        if destColor == color:
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


def moveKing(currHor, currVer, destHor, destVer):
    deltaX = abs(currHor - destHor)
    deltaY = abs(currVer - destVer)

    if deltaX > 1 or deltaY > 1:
        return "illegal"
     
    return "legal"


def moveQueen(currHor, currVer, destHor, destVer):
    deltaX = abs(currHor - destHor)
    deltaY = abs(currVer - destVer)

    if deltaX == 0:
        return "legal"

    rico = abs(deltaY/deltaX)

    if rico == 1 or rico == 0:
        return "legal"
    
    return "illegal"

def moveBishop(currHor, currVer, destHor, destVer):
    deltaX = abs(currHor - destHor)
    deltaY = abs(currVer - destVer)

    if deltaX == 0:
        return "illegal"

    rico = abs(deltaY/deltaX)

    if rico == 1:
        return "legal"
    
    return "illegal"

def moveHorse(currHor, currVer, destHor, destVer):
    deltaX = abs(currHor - destHor)
    deltaY = abs(currVer - destVer)

    if deltaX == 2 and deltaY == 1:
        return "legal"

    if deltaY == 2 and deltaX == 1:
        return "legal"
    
    return "illegal"

def moveRook(currHor, currVer, destHor, destVer):
    deltaX = abs(currHor - destHor)
    deltaY = abs(currVer - destVer)

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
            return "illegal"

        if deltaY == -1:
            return "legal"
        
        if currVer == 2:
            if deltaY == -2:
                return "legal"

    if color == "black":
        if GetPieceType(destHor, destVer) != "null":
            return "illegal"
            
        if deltaY == 1:
            return "legal"
        
        if currVer == 7:
            if deltaY == 2:
                return "legal"
    
    return "illegal"
