
quit = False

while quit == False:

    board = [[' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ']]

    uplayer = [6 , 6 , 6 , 6 , 6 , 6 , 6]

    name1 = str(raw_input("Enter name of person_1(O) : "))
    name2 = str(raw_input("Enter name of person_2(X) : "))
    name1 += '(O)'
    name2 += '(X)'

    turn = 0
    win = False

    while win == False:
        if turn % 2 == 0:
            name = name1
            char = 'O'
        else:
            name = name2
            char = 'X'
        for i in range(7):
            print(board[i])

        value = input('\n ' + name + '\'s turn : ')

        if (value < 0) + (value > 6):
            print('\n Invalid Entry : ')
        else:
            if uplayer[value] < 0:
                print('\n Invalid Entry : ')
            else:
                board[uplayer[value]][value] = char
                turn += 1
                uplayer[value] -= 1

                for i in range(7):
                    for j in range(4):
                        if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3]:
                            if board[i][j] != ' ':
                                win = True
                        elif board[j][i] == board[j + 1][i] == board[j + 2][i] == board[j + 3][i]:
                            if board[j][i] != ' ':
                                win = True
                for i in range(4):
                    for j in range(4):
                        if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3]:
                            if board[i][j] != ' ':
                                win = True
                for i in range(3 , 7):
                    for j in range(4):
                        if board[i][j] == board[i - 1][j + 1] == board[i - 2][j + 2] == board[i - 3][j + 3]:
                            if board[i][j] != ' ':
                                win = True

    if win == True:
        print(board[0])
        print(board[1])
        print(board[2])
        print(board[3])
        print(board[4])
        print(board[5])
        print(board[6])

        if turn % 2 != 0:
            print('\n ' + name1 + 'won the match !!!\n')
        else:
            print('\n ' + name2 + 'won the match !!!\n')
    else:
        print("\n Match drawn !!!\n")

    choice = str(raw_input("Enter q for quit, any other character to continue : "))
    if choice == 'q':
        quit = True
