#!/usr/bin/python

from tkinter import *

window = Tk()
window.minsize(450, 550)
window.maxsize(450, 550)
positionRight = int(window.winfo_screenwidth() / 2 - 225)
positionDown = int(window.winfo_screenheight() / 2 - 275)
window.geometry('+{}+{}'.format(positionRight, positionDown))
window.configure(background='#ffd2a5')
window.title('4inarow')

gridcolor = '#a5d2ff'
gridtxt = '#000000'
btncolor = '#d2a5ff'
uplayer = [6 , 6 , 6 , 6 , 6 , 6 , 6]
name = 'Player1'
name1 = 'Player1'
name2 = 'Player2'
char = 'O'
turn = 0

vslabel = Label(window, text = name1 + ' vs ' + name2, font = 'Helvetica 22 bold', bg = '#ffd2a5', fg = '#222222')
vslabel.place(relx = 0.5, y = 25, anchor = CENTER)

grid = [[0 for x in range(7)] for y in range(7)]
for a in range(7):
        for b in range(7):
                grid[a][b] = Button(window, text = ' ', fg = gridtxt, bg = gridcolor, font = 'Helvetica 22 bold', borderwidth = 0)
                grid[a][b].place(x = (50 + 50 * b), y = (50 + 50 * a), height = 50, width = 50)

label = Label(window, text = name + '\'s turn', font = 'Helvetica 22 bold', bg = '#ffd2a5', fg = '#222222')
label.place(relx = 0.5, y = 500, anchor = CENTER)

def playagain():
        global turn
        global name
        global char
        for i in range(7):
                for j in range(7):
                        grid[i][j]['text'] = ' '
                        grid[i][j]['bg'] = gridcolor
        turn = 0
        char = 'O'
        name = 'Player1'
        exitbutton.place_forget()
        playagainbutton.place_forget()
        label['text'] = name + '\'s turn'
        label.place(relx = 0.5, y = 500, anchor = CENTER)
        for a in range(7):
                btn[a].place(x = (50 + 50 * a), y = 400, height = 50, width = 50)
                uplayer[a] = 6

playagainbutton = Button(window, text = ' Play Again ', fg = '#ffffff', bg = '#0080ff', command = playagain, font = 'Helvetica 22 bold', borderwidth = 0)
exitbutton = Button(window, text = ' Exit ', fg = '#ffffff', bg = '#0080ff', command = window.destroy, font = 'Helvetica 22 bold', borderwidth = 0)

def wincheck():
        win = False
        for i in range(7):
                for j in range(4):
                        if grid[i][j]['text'] != ' ' and grid[i][j]['text'] == grid[i][j + 1]['text'] == grid[i][j + 2]['text'] == grid[i][j + 3]['text']:
                                win = True
                                grid[i][j]['bg'] = '#ee9090'
                                grid[i][j + 1]['bg'] = '#ee9090'
                                grid[i][j + 2]['bg'] = '#ee9090'
                                grid[i][j + 3]['bg'] = '#ee9090'
                        elif grid[j][i]['text'] != ' ' and grid[j][i]['text'] == grid[j + 1][i]['text'] == grid[j + 2][i]['text'] == grid[j + 3][i]['text']:
                                win = True
                                grid[j][i]['bg'] = '#ee9090'
                                grid[j + 1][i]['bg'] = '#ee9090'
                                grid[j + 2][i]['bg'] = '#ee9090'
                                grid[j + 3][i]['bg'] = '#ee9090'
        for i in range(4):
                for j in range(4):
                        if grid[i][j]['text'] != ' ' and grid[i][j]['text'] == grid[i + 1][j + 1]['text'] == grid[i + 2][j + 2]['text'] == grid[i + 3][j + 3]['text']:
                                win = True
                                grid[i][j]['bg'] = '#ee9090'
                                grid[i + 1][j + 1]['bg'] = '#ee9090'
                                grid[i + 2][j + 2]['bg'] = '#ee9090'
                                grid[i + 3][j + 3]['bg'] = '#ee9090'
        for i in range(3 , 7):
                for j in range(4):
                        if grid[i][j]['text'] != ' ' and grid[i][j]['text'] == grid[i - 1][j + 1]['text'] == grid[i - 2][j + 2]['text'] == grid[i - 3][j + 3]['text']:
                                win = True
                                grid[i][j]['bg'] = '#ee9090'
                                grid[i - 1][j + 1]['bg'] = '#ee9090'
                                grid[i - 2][j + 2]['bg'] = '#ee9090'
                                grid[i - 3][j + 3]['bg'] = '#ee9090'
        return win

def updategrid(col):
        global turn
        global name
        global name1
        global name2
        global char
        if uplayer[col] >= 0:
                grid[uplayer[col]][col]['text'] = char
                turn += 1
                uplayer[col] -= 1
        if wincheck():
                label['text'] = name + ' won the match !!!'
                for a in range(7):
                        btn[a].place_forget()
                label.place(relx = 0.5, y = 430, anchor = CENTER)
                playagainbutton.place(x = 50, y = 470, height = 50, width = 170)
                exitbutton.place(x = 230, y = 470, height = 50, width = 170)
        else:
                c = 0
                for i in uplayer:
                        c += i
                if c == -7:
                        label['text'] = 'Match drawn !!!'
                        for a in range(7):
                                btn[a].place_forget()
                        label.place(relx = 0.5, y = 430, anchor = CENTER)
                        playagainbutton.place(x = 50, y = 470, height = 50, width = 170)
                        exitbutton.place(x = 230, y = 470, height = 50, width = 170)
                else:
                        if turn % 2 == 0:
                                name = name1
                                char = 'O'
                        else:
                                name = name2
                                char = 'X'
                        label['text'] = name + '\'s turn'

btn = [0 for x in range(7)]
btn[0] = Button(window, text = 0, fg = gridtxt, bg = btncolor, font = 'Helvetica 22 bold', borderwidth = 0, command = lambda: updategrid(0))
btn[1] = Button(window, text = 1, fg = gridtxt, bg = btncolor, font = 'Helvetica 22 bold', borderwidth = 0, command = lambda: updategrid(1))
btn[2] = Button(window, text = 2, fg = gridtxt, bg = btncolor, font = 'Helvetica 22 bold', borderwidth = 0, command = lambda: updategrid(2))
btn[3] = Button(window, text = 3, fg = gridtxt, bg = btncolor, font = 'Helvetica 22 bold', borderwidth = 0, command = lambda: updategrid(3))
btn[4] = Button(window, text = 4, fg = gridtxt, bg = btncolor, font = 'Helvetica 22 bold', borderwidth = 0, command = lambda: updategrid(4))
btn[5] = Button(window, text = 5, fg = gridtxt, bg = btncolor, font = 'Helvetica 22 bold', borderwidth = 0, command = lambda: updategrid(5))
btn[6] = Button(window, text = 6, fg = gridtxt, bg = btncolor, font = 'Helvetica 22 bold', borderwidth = 0, command = lambda: updategrid(6))
for a in range(7):
        btn[a].place(x = (50 + 50 * a), y = 400, height = 50, width = 50)

window.mainloop()