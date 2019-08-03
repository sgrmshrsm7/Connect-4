board = [[' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ']]

uplayer = [6 , 6 , 6 , 6 , 6 , 6 , 6]

quit = False

while quit == False:
    name1 = str(raw_input("Enter name of person_1('O') : "))
    name2 = str(raw_input("Enter name of person_2('X') : "))

    turn = 0
    win = False

    while win == False:
        pass

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
