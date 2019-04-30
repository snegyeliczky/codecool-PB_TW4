import os
import time
import random

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

def get_input():
    row = input("Add meg a sort: ")  
    column =  input("Add meg az oszlopot: ")         
    return row, column

def set_position_X ():
    row = int(input("add meg a sort: "))
    column= int(input("add meg az oszlopot: "))
    board[row-1][column-1]="x"

def set_position_O ():
    row = int(input("add meg a sort: "))
    column= int(input("add meg az oszlopot: "))
    board[row-1][column-1]="O"



board_maker(int(input("Add meg milyen legyen a mezö: ")))

while True:
    board_printer(board)
    #get_input()
    set_position_X()
    board_printer(board)
    set_position_O()
    #print(board)

'''
def game_over(game_board):
    for i in range(1,8,3):
        if game_board[i] == "X" and game_board[i+1] == "X" and game_board[i+2] == "X":
            print("X won!")
            quit()
        if game_board[i] == "O" and game_board[i+1] == "O" and game_board[i+2] == "O":
            print("O won!")
            quit()
    for i in range(1,4):
        if game_board[i] == "X" and game_board[i+3] == "X" and game_board[i+6] == "X":
            print("X won!")
            quit()
        if game_board[i] == "O" and game_board[i+3] == "O" and game_board[i+6] == "O":
            print("O won!")
            quit()
    if game_board[1] == "X" and game_board[5] == "X" and game_board[9] == "X":
        print("X won!")
        quit()
    if game_board[3] == "X" and game_board[5] == "X" and game_board[7] == "X":
        print("X won!")
        quit()
    if game_board[1] == "O" and game_board[5] == "O" and game_board[9] == "O":
        print("O won!")
        quit()
    if game_board[3] == "O" and game_board[5] == "O" and game_board[7] == "O":
        print("O won!")
        quit()

    x = 0
    for i in range(1,17):
        if game_board[i] == " ":
             x+=1
    if x == 0:
        print("Draw!")
        quit()

def input_choiceX():
    try:
        position = int(input("Please choose an empty space for X: "))
        if position < 1 or position > 16:
            raise ValueError
        elif board[position] == " ":
            board[position] = "X"
        else:
            print("Sorry this place is reserved")
            time.sleep(1)
            raise ValueError
    except:
        print("Pleas give a valid position!")
        input_choiceX()

def input_choiceY():
    try:
        position = int(input("Please choose an empty space for O: "))
        if position < 1 or position > 16:
            raise ValueError
        elif board[position] == " ":
            board[position] = "O"
        else:
            print("Sorry this place is reserved")
            time.sleep(1)
            raise ValueError
    except:
        print("Pleas give a valid position!")
        input_choiceY()


while True:
    os.system("clear")
    print_board()

    input_choiceX()
    os.system("clear")
    print_board()
    game_over(board)
        
    input_choiceY()
    os.system("clear")
    print_board()
    game_over(board)
  '''      
    
    
