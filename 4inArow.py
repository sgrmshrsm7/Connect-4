board = [[' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' '] , [' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ']]

uplayer = [6 , 6 , 6 , 6 , 6 , 6 , 6]

quit = False

while quit == False:
    name1 = str(raw_input("Enter name of person_1('O') : "))
    name2 = str(raw_input("Enter name of person_2('X') : "))
    
    choice = str(raw_input("Enter q for quit : "))
    if choice == 'q':
        quit = True
