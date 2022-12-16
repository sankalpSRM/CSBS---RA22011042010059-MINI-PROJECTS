name = input("Enter your Name: ")
print("Hello",name)
game = input("What game would you like to play(Hangman or Pattern Maker ): ")
if(game=='Pattern Maker'):
    pattern = input("Please enter the pattern you would like to make (Options: Pyramid,N,H,Number Pyramid,T,Quadilateral,Downward Pyramid,Sandglass,Diamond,Half Pyramid) : ")
    if(pattern=='pyramid' or pattern=='Pyramid'):
        rows = int(input("Enter the number of rows: "))
        column = 1
        for i in range(1,rows+1):
            for j in range(rows-i):
                print("   ", end = "")
            for k in range(column):
                print(" * ", end="")
            column = column+2
            print("")
    elif(pattern=='N' or pattern=='n'):
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the columns: "))
        for i in range(rows):
            for j in range(columns):
                if i == 0 or i == rows-1:
                    if j == 0 or j == columns-1:
                        print(" * ", end="")
                    else:
                        print("   ", end="")
                else:
                    if j == 0 or j == columns-1:
                        print(" * ", end="")
                    elif i == j:
                        print(" * ", end="")
                    else:
                        print("   ", end="")
            print("")
    elif(pattern=="Number Pyramid" or pattern=='number pyramid'):
        rows = int(input("Enter the number of rows: "))
        column = 1
        for i in range(1,rows+1):
            for j in range(rows-i):
                print("   ", end = "")
            for k in range(column):
                if i == 1 or i == rows:
                    print(" * ", end="")
                else:
                    if k == 0 or k ==column-1:
                        print(" * ", end="")
                    else :
                        print(" 1 ", end="")

            column = column+2
            print("")
    elif(pattern=="H" or pattern=='h'):
        rows = int(input("Enter rows: "))
        column = int(input("Enter columns: "))
        for i in range(0,rows):
            for j in range(0,column):
                if i == (rows//2):
                    print(" 1 ", end="")
                else:
                    if j == 0 or j == column-1:
                        print(" 1 ", end="")
                    else :
                        print("   ", end="")

            print("")
    elif(pattern=="T" or pattern=='t'):
        rows = int(input("Enter Rows: "))
        columns = int(input("Enter Columns: "))

        for i in range(rows):
            for j in range(columns):
                if i == 0 :
                    print(" 1 ", end="")
                else :
                    if j == (columns//2):
                        print(" 1 ", end="")
                    else:
                        print("   ", end ="")

            print("")

    elif(pattern=="Quadilateral" or pattern=='quadilateral'):
        length = int(input("Enter the Length of the Shape: "))
        breadth = int(input("Enter the Breadth: "))
        if(length>breadth or length<breadth):
            print("The reactangle is as follows:")
        if(length==breadth):
            print("The square is as follows:")
        for i in range(0,length):
            for j in range(0,breadth):
                if i == 0 or i == length-1:
                    print(" * ",end="")
                else:
                    if j == 0 or j == (breadth-1):
                        print(" * ", end="")
                    else:
                        print("   ", end="")
            print("")
    elif (pattern=='Downward Pyramid' or pattern=='downward pyramid'):
        rows = 5
        k = 2 * rows - 2
        for i in range(rows, -1, -1):
            for j in range(k, 0, -1):
                print(end=" ")
            k = k + 1
            for j in range(0, i + 1):
                print("*", end=" ")
            print("")
    elif(pattern=='Sandglass' or pattern == 'sandglass'):
        rows = 5
        i = 0
        while i <= rows - 1:
            j = 0
            while j < i:

                print('', end=' ')
                j += 1
            k = i
            while k <= rows - 1:
                print('*', end=' ')
                k += 1
            print()
            i += 1

        i = rows - 1
        while i >= 0:
            j = 0
            while j < i:
                print('', end=' ')
                j += 1
            k = i
            while k <= rows - 1:
                print('*', end=' ')
                k += 1
            print('')
            i -= 1
    elif(pattern=='Diamond' or pattern=='diamond'):
        rows = 5
        k = 2 * rows - 2
        for i in range(0, rows):
            for j in range(0, k):
                print(end=" ")
            k = k - 1
            for j in range(0, i + 1):
                print("* ", end="")
            print("")

        k = rows - 2

        for i in range(rows, -1, -1):
            for j in range(k, 0, -1):
                print(end=" ")
            k = k + 1
            for j in range(0, i + 1):
                print("* ", end="")
            print("")
    elif(pattern=='Half Pyramid' or pattern=='half pyramid'):
        num_rows = int(input("Enter the number of rows: "));
        k = 1
        for i in range(0, num_rows):
            for j in range(0, k):
                print("* ", end="")
            k = k + 1
            print()

elif(game=='Hangman'):
    print("Below is a game of hangman")
    print("Enter the names of players")
    player1 = input("Player1: ")
    player2 = input("Player2: ")
    print(player1, " enter a word for ", player2, " to guess")
    ip = (input("Enter the word"))  # ip stores the word input by player1
    nchar = 0
    for char in ip:  # this for loop calculates the number of characters in the word
        nchar = nchar + 1
        print("The word has", nchar, " characters")

        print("Guess the characters: ")  # the guessing game starts here

        guesses = ''  # all the guesses are stored here
        chances = 12  # any number of turns can be used here

    while chances > 0:
        wchar = 0  # counts the number of times a wrong character is input
        for char in ip:  # comparing that character with the characters in guesses
            if char in guesses:
                print(char)
            else:
                print("_")
                wchar += 1  # for every wrong input wchar is incremented

        if wchar == 0:
            print("You Win")  # if there is no wrong input the player wins
            print("The word is: ", ip)  # this prints the correct input
            break

    # if player has input the wrong alphabet then it will ask the player to input again
        guess = input("guess a character: ")
        guesses += guess  # every input character will be stored in guesses
        if guess not in ip:  # check input with the character in word
            chances -= 1
            print("Wrong")  # if the character does not match , wrong is given as output
            print("You have", + chances, 'more chances')  # prints the number of chances left for the user
        if chances == 0:
            print("You Loose")
            print("The word is: ", ip)  # this prints the correct input

else:
    print("Invalid Try Again")
