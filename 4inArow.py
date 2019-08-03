
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

        value = input('\n ' + name + '\'s turn : ')

        if (value < 0) + (value > 6):
            print('\n Invalid Entry : ')
        else:
            if uplayer[value] < 0:
                print('\n Invalid Entry : ')
            else:
                board[value][uplayer[value]] = char

    if win == True:
        if turn % 2 == 0:
            print('\n ' + name1 + 'won the match !!!\n')
        else:
            print('\n ' + name2 + 'won the match !!!\n')
    else:
        print("\n Match drawn !!!\n")

    choice = str(raw_input("Enter q for quit : "))
    if choice == 'q':
        quit = True
