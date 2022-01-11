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
    
    print("letter: " + str(letter) + " | number: " + str(number))