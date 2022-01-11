# Een functie om de letters om te zetten in cijfers
def letterToNumber(letter):
    if letter == 'A':
        return 1
    elif letter == 'B':
        return 2
    elif letter == 'C':
        return 3
    elif letter == 'D':
        return 4
    elif letter == 'E':
        return 5
    elif letter == 'F':
        return 6
    elif letter == 'G':
        return 7
    elif letter == 'H':
        return 8

selectedPosition = [1, 1]

# Het selecteren van een stuk (bv: A6)
def selectInput():
    # Aanvragen van de input en omzetten naar een array
    selected = list(input("Geef het coordinaat van het stuk dat u wilt selecteren: "))

    # Letter in een hoofdletter zetten
    letter = str.capitalize(selected[0])
    # Testen of de eerste invoer daadwerkelijk een letter is
    if str.isalpha(letter) == False:
        print("Foutieve invoer, de eerst moet de letter gegeven worden!")
        return

    # Testen als de tweede invoer daadwerkelijk een cijfer is en omzetten van een string naar een integer
    try: 
      number = int(selected[1])
    except ValueError:
      print("Foutieve invoer, als tweede moet het cijfer gegeven worden!")
      return
    
    selectedPosition[0] = letterToNumber(letter)
    selectedPosition[1] = number

    print("hor=" + str(selectedPosition[0]) + " ver=" + str(selectedPosition[1]))