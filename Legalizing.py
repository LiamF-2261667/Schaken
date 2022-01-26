from Piece import GetPieceType, GetPieceColor, PieceNameToLetter


# Een functie om te kijken als een zet legaal is (returnt "legal" of een fout)
def isLegal(currHor, currVer, destHor, destVer, type, color):
    # Testen als er daadwerkelijk is bewogen
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
            # In het geval van een pion zijn er andere bewegingen als hij een stuk kan nemen of geblokkeerd wordt
            if type == "P":
                # Geef True door om dit duidelijk te maken
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
    
    print("ERROR: Type " + str(type) + " onbekend!")


def moveKing(currHor, currVer, destHor, destVer):
    deltaX = abs(currHor - destHor)
    deltaY = abs(currVer - destVer)

    # Als de koning meer dan 1 plaats beweegt
    if deltaX > 1 or deltaY > 1:
        return "illegal"
     
    return "legal"


def moveQueen(currHor, currVer, destHor, destVer):
    deltaX = destHor - currHor
    deltaY = destVer - currVer

    # Als de dame verticaal of horizontaal beweegt
    if deltaX == 0 or deltaY == 0:
        # naar rechts
        if deltaX > 0:
            # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
            for i in range(currHor + 1, destHor):
                if GetPieceType(i, currVer) != "null":
                    # Indien dat het geval is, geef de foutcode "blocked"
                    return "blocked"
    
        # naar links
        if deltaX < 0:
            # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
            for i in range(destHor + 1, currHor):
                if GetPieceType(i, currVer) != "null":
                    # Indien dat het geval is, geef de foutcode "blocked"
                    return "blocked"

        # naar boven
        if deltaY > 0:
            # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
            for i in range(currVer + 1, destVer):
                if GetPieceType(currHor, i) != "null":
                    # Indien dat het geval is, geef de foutcode "blocked"
                    return "blocked"

        # naar onder
        if deltaY < 0:
            # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
            for i in range(destVer + 1, currVer):
                if GetPieceType(currHor, i) != "null":
                    # Indien dat het geval is, geef de foutcode "blocked"
                    return "blocked"

        # Er staat geen stuk in de weg, dus is de beweging legaal
        return "legal"

    rico = deltaY/deltaX

    # Als er diagonaal wordt bewogen    
    if abs(rico) == 1:
        j = 0

        # Als de dame naar rechts gaat
        if deltaX > 0:
            # naar boven
            if deltaY > 0:
                # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
                for i in range(currHor + 1, destHor):
                    j += 1
                    if GetPieceType(i, currVer + j) != "null":
                        return "blocked"

            # naar onder
            if deltaY < 0:
                # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
                for i in range(currHor + 1, destHor):
                    j += 1
                    if GetPieceType(i, currVer - j) != "null":
                        return "blocked"
        
        # Als de dame naar links gaat
        if deltaX < 0:
            # naar boven
            if deltaY > 0:
                # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
                for i in range(destHor + 1, currHor):
                    j += 1
                    if GetPieceType(i, destVer - j) != "null":
                        return "blocked"

            # naar onder
            if deltaY < 0:
                # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
                for i in range(destHor + 1, currHor):
                    j += 1
                    if GetPieceType(i, destVer + j) != "null":
                        return "blocked"
        
        # Indien er geen stuk in de weg is, is deze beweging legaal
        return "legal"
    
    # Als er niet diagonaal, verticaal of horizontaal wordt bewogen is het illegaal
    return "illegal"

def moveBishop(currHor, currVer, destHor, destVer):
    deltaX = destHor - currHor
    deltaY = destVer - currVer

    # Als er geen horizontale beweging is, is het illegaal (voor later niet te delen door 0)
    if deltaX == 0:
        return "illegal"
    
    rico = deltaY/deltaX

    # Als er niet diagonaal wordt bewogen is het illegaal
    if abs(rico) != 1:
        return "illegal"

    j = 0

    # Als de loper naar rechts gaat
    if deltaX > 0:
        # naar boven
        if deltaY > 0:
            # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
            for i in range(currHor + 1, destHor):
                j += 1
                if GetPieceType(i, currVer + j) != "null":
                    return "blocked"

        # naar onder
        if deltaY < 0:
            # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
            for i in range(currHor + 1, destHor):
                j += 1
                if GetPieceType(i, currVer - j) != "null":
                    return "blocked"
    
    # Als de loper naar links gaat
    if deltaX < 0:
        # naar boven
        if deltaY > 0:
            # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
            for i in range(destHor + 1, currHor):
                j += 1
                if GetPieceType(i, destVer - j) != "null":
                    return "blocked"

        # naar onder            
        if deltaY < 0:
            # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
            for i in range(destHor + 1, currHor):
                j += 1
                if GetPieceType(i, destVer + j) != "null":
                    return "blocked"

    # Als er geen stuk in de weg staat, is het legaal
    return "legal"

def moveHorse(currHor, currVer, destHor, destVer):
    deltaX = abs(currHor - destHor)
    deltaY = abs(currVer - destVer)

    # Als er 2 horizontaal en 1 verticaal wordt bewogen
    if deltaX == 2 and deltaY == 1:
        return "legal"

    # Als er 2 verticaal en 1 horizontaal wordt bewogen
    if deltaY == 2 and deltaX == 1:
        return "legal"
    
    # Anders is het illegaal
    return "illegal"

def moveRook(currHor, currVer, destHor, destVer):
    deltaX = destHor - currHor
    deltaY = destVer - currVer

    # Als er naar rechts wordt bewogen
    if deltaX > 0:
        # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
        for i in range(currHor + 1, destHor):
            if GetPieceType(i, currVer) != "null":
                return "blocked"
    
    # Als er naar links wordt bewogen
    if deltaX < 0:
        # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
        for i in range(destHor + 1, currHor):
            if GetPieceType(i, currVer) != "null":
                return "blocked"

    # Als er naar boven wordt bewogen
    if deltaY > 0:
        # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
        for i in range(currVer + 1, destVer):
            if GetPieceType(currHor, i) != "null":
                return "blocked"

    # Als er naar onder wordt bewogen
    if deltaY < 0:
        # nagaan of er een stuk ligt tussen het startpunt en het eindpunt
        for i in range(destVer + 1, currVer):
            if GetPieceType(currHor, i) != "null":
                return "blocked"

    # Als er geen stuk in de weg ligt en hij beweegt verticaal of horizontaal, is het legaal
    if deltaX == 0 or deltaY == 0:
        return "legal"
    
    # Anders is het illegaal
    return "illegal"

def movePawn(currHor, currVer, destHor, destVer, color, isTakingPiece):
    deltaX = abs(currHor - destHor)
    deltaY = currVer - destVer

    # Als er geen stuk wordt genomen en er is een horizontale beweging, is dat illegaal
    if isTakingPiece == False and deltaX != 0:
        return "illegal"

    # Als er een stuk wordt genomen en er wordt slechts 1 horizontaal bewogen:
    if isTakingPiece == True and deltaX == 1:

        # Als het stuk 1 in de juist verticale richting beweegt, is dat legaal
        if color == "white" and deltaY == -1:
            return "legal"

        if color == "black" and deltaY == 1:
            return "legal"
        
        # Anders, illegaal
        return "illegal"

    # Als er geen stuk wordt genomen
    if color == "white":
        # kijken als er een stuk in de weg staat
        if GetPieceType(destHor, destVer) != "null":
            return "blocked"

        # kijken als er 1 verticaal in de juiste richting wordt bewogen
        if deltaY == -1:
            return "legal"
        
        # Als de pion op zijn startpositie staat, mag hij ook 2 vakjes verticaal bewegen
        if currVer == 2:
            if deltaY == -2:
                return "legal"

    # Als er geen stuk wordt genomen
    if color == "black":
        # kijken als er een stuk in de weg staat
        if GetPieceType(destHor, destVer) != "null":
            return "blocked"
            
        # kijken als er 1 verticaal in de juiste richting wordt bewogen
        if deltaY == 1:
            return "legal"
        
        # Als de pion op zijn startpositie staat, mag hij ook 2 vakjes verticaal bewegen
        if currVer == 7:
            if deltaY == 2:
                return "legal"
    
    # Anders, illegaal
    return "illegal"

# Variabelen om na te kijken als de koning niet in schaak komt door een zet
whiteKingHor = 5
whiteKingVer = 1

blackKingHor = 5
blackKingVer = 8

# Een functie om de positie in een ander file te veranderen
def setWhiteKingPos(hor, ver):
    global whiteKingHor
    global whiteKingVer

    whiteKingHor = hor
    whiteKingVer = ver
   
# Een functie om de positie in een ander file te veranderen 
def setBlackKingPos(hor, ver):
    global blackKingHor
    global blackKingVer

    blackKingHor = hor
    blackKingVer = ver


# Nakijken als een koning van een bepaalde kleur schaak staat
def isKingInDanger(color):
    # Voor elk vakje op het bord:
    for i in range(1, 9):
        for j in range(1, 9):
            # Informatie over het stuk verzamelen
            pieceType = GetPieceType(i, j)
            pieceColor = GetPieceColor(i, j)

            # Als er een stuk op het vakje staat en het is van de vijand:
            if pieceType != "null" and pieceColor != color:
                # Test als het stuk op dat vakje de koning kan nemen
                if color == "white":
                    legality = isLegal(i, j, whiteKingHor, whiteKingVer, PieceNameToLetter(pieceType), "black")

                elif color == "black":
                    legality = isLegal(i, j, blackKingHor, blackKingVer, PieceNameToLetter(pieceType), "white")

                # Als de koning kan genomen worden return True
                if legality == "legal":
                    return True

    # Anders, return False
    return False
