import os
import time
import random

print("Hello gamer!!!")


board = []
def board_maker(quantity):
    for i in range(0,quantity):
        board.append([])
        for a in range(0,quantity):
            board[i].append('_')


def board_printer(board):
    print(" ",end='')
    for i in range(len(board)):
        print(" "+ str(i+1), end='')
    print("")    
    line_number=0
    for i in board:
        line_number+=1
        print('| ', end='')
        for a in i:
            print(a+' ',end='')
        print('|'+str(line_number))


def set_position_X ():
    try:
        row = int(input("add meg az X sort: "))
        column = int(input("add meg az X oszlopot: "))
        if (row or column ) > len(board):
            print("megfelelo szamokat adj meg!")
            set_position_X()
        elif board[row-1][column-1]!="_":
            print("Ez a mezö már foglalt")
            set_position_X()
        else:
            board[row-1][column-1]="X"
    except ValueError:
        print("SZÁMOT adj meg.")
        set_position_X()

def set_position_O ():
    try:
        row = int(input("add meg az O sort: "))
        column = int(input("add meg az O oszlopot: "))
        if (row or column ) > len(board):
            print("megfelelo szamokat adj meg!")
            set_position_O()
        elif board[row-1][column-1]!="_":
            print("Ez a mezö már foglalt")
            set_position_O()
        else:
            board[row-1][column-1]="O"
    except ValueError:
        set_position_O()

def win_cond_X():
    for i in range(len(board)):
        for j in range(len(board)-2):
            if board[i][j] == "X" and (board[i][j+1] == "X" and board[i][j+2]) == "X":
                win_printer_X()
    for i in range(len(board)-2):
        for j in range(len(board)):
            if board[i][j] == "X" and (board[i+1][j] == "X" and board[i+2][j]) == "X":
                win_printer_X()
    for i in range(len(board)-2):
        for j in range(len(board)-2):
            if board[i][j] == "X" and (board[i+1][j+1] == "X" and board[i+2][j+2]) == "X":
                win_printer_X()
    for i in range(2,len(board)-2):
        for j in range(len(board)):
            if board[i][j] == "X" and (board[i-1][j+1] == "X" and board[i-2][j+2]) == "X":
                win_printer_X()

def win_cond_O():
    for i in range(len(board)):
        for j in range(len(board)-2):
            if board[i][j] == "O" and (board[i][j+1] == "O" and board[i][j+2]) == "O":
                win_printer_O()
    for i in range(len(board)-2):
        for j in range(len(board)):
            if board[i][j] == "O" and (board[i+1][j] == "O" and board[i+2][j]) == "O":
                win_printer_O()
    for i in range(len(board)-2):
        for j in range(len(board)-2):
            if board[i][j] == "O" and (board[i+1][j+1] == "O" and board[i+2][j+2]) == "O":
                win_printer_O()
    for i in range(2,len(board)-2):
        for j in range(len(board)):
            if board[i][j] == "O" and (board[i-1][j+1] == "O" and board[i-2][j+2]) == "O":
              win_printer_O()

def win_printer_O():
    os.system("clear")
    board_printer(board)
    print("O Won!")
    quit()

def win_printer_X():
    os.system("clear")
    board_printer(board)
    print("X Won!")
    quit()

#Main
board_maker(int(input("Add meg milyen legyen a mezö: ")))
os.system("clear")
while True:
    board_printer(board)
    set_position_O()
    win_cond_O()
    os.system("clear")
    board_printer(board)
    set_position_X()
    win_cond_X()
    os.system("clear")
