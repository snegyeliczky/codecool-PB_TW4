import os
import time
import random

print("Hello gamer!!!")


board = [['_','_','_'],['_','_','_'],['_','_','_',]]


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


def win_cond_X():
    for i in range(len(board)):
        for j in range(len(board)-2):
            if board[i][j] == "X" and (board[i][j+1] == "X" and board[i][j+2]) == "X":
                win_printer_X()
    for i in range(len(board)-2):
        for j in range(len(board)):
            if board[i][j] == "X" and (board[i+1][j] == "X" and board[i+2][j]) == "X":
                win_printer_X()
    if board[0][0] == "X" and (board[1][1] == "X" and board[2][2]) == "X":
                win_printer_X()
    if board[0][2] == "X" and (board[1][1] == "X" and board[2][0]) == "X":
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
    if board[0][0] == "O" and (board[1][1] == "O" and board[2][2]) == "O":
                win_printer_O()
    if board[0][2] == "O" and (board[1][1] == "O" and board[2][0]) == "O":
              win_printer_O()

def win_printer_O():
    #os.system("clear")
    board_printer(board)
    print("O Won!")
    quit()

def win_printer_X():
    os.system("clear")
    board_printer(board)
    print("X Won!")
    quit()


def AI_first_step():
    if board[1][1] == "X":
        step = random.randint(1,4)
        if step == 1:
            board[0][0] = "O"
        elif step == 2:
            board[0][2] = "O"
        elif step == 3:
            board[2][0] = "O"
        elif step == 4:
            board[2][2] = "O"
    elif board[1][1] == "_":
        board[1][1] = "O"


def AI_def_step():
    for i in range(0,3):
        if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "_":
            board[i][2] = "O"
            return
        elif board[i][0] == "_" and board[i][1] == "X" and board[i][2] == "X":
            board[i][0] = "O"
            return
        elif board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "_":
            board[2][i] = "O"
            return
        elif board[0][i] == "_" and board[1][i] == "X" and board[2][i] == "X":
            board[0][i] = "O"
            return
        elif board[0][i] == "X" and board[2][i] == "X" and board[1][i] == "_":
            board[1][i] = "O"
            return
        elif board[i][0] == "X" and board[i][2] == "X" and board[i][1] == "_":
            board[i][1] = "O"
            return
    if board[0][0] == "_" and board[1][1] == "X" and board[2][2] == "X":
        board[0][0] = "O"
        return
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "_":
        board[2][2] = "O"
        return
    elif board[0][2] == "_" and board[1][1] == "X" and board[2][0] == "X":
        board[0][2] = "O"
        return
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "_":
        board[2][0] = "O"
        return
    else:
        AI_rand_step()

def AI_off_step(off):
    for i in range(0,3):
        if board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "_":
            board[i][2] = "O"
            off = True
            return
        elif board[i][0] == "_" and board[i][1] == "O" and board[i][2] == "O":
            board[i][0] = "O"
            off = True
            return
        elif board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "_":
            board[2][i] = "O"
            off = True
            return
        elif board[0][i] == "_" and board[1][i] == "O" and board[2][i] == "O":
            board[0][i] = "O"
            off = True
            return
        elif board[0][i] == "O" and board[2][i] == "O" and board[1][i] == "_":
            board[1][i] = "O"
            return
        elif board[i][0] == "O" and board[i][2] == "O" and board[i][1] == "_":
            board[i][1] = "O"
            return
    if board[0][0] == "_" and board[1][1] == "O" and board[2][2] == "O":
        board[0][0] = "O"
        off = True
        return
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "_":
        board[2][2] = "O"
        off = True
        return
    elif board[0][2] == "_" and board[1][1] == "O" and board[2][0] == "O":
        board[0][2] = "O"
        off = True
        return
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "_":
        board[2][0] = "O"
        off = True
        return

def AI_rand_step():
    i = random.randint(0,2)
    j = random.randint(0,2)
    if board[i][j] == "_":
        board[i][j] = "O"
    else:
        AI_rand_step()


#Main 
os.system("clear")
def main():
    board_printer(board)
    set_position_X()
    AI_first_step()
    os.system("clear")
    while True:
        off = False
        board_printer(board)
        set_position_X()
        win_cond_X()
        os.system("clear")
        AI_off_step(off)
        win_cond_O()
        if off == False:
            AI_def_step()
        win_cond_O()


main()