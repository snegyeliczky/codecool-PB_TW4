board = [["_","X","_"],["_","X","_"],["_","_","_"]]

for i in board:
 print(i)


'''
hp=0
vp=0

for i in board:
    for a in i:
        if a =="X":
            hp=board.index(i)
            print(hp)
            vp=i.index(a)
            print(vp)
        break


if board[hp-1][vp] == "X":
    board[hp+1][vp] ="O"
elif board[hp+1][vp] =="X":
    board[hp-1][vp]="O"
elif board[hp][vp-1] == "X":
    board[hp][vp+1] ="O"
elif board[hp][vp+1] =="X":
    board[hp][vp-1]="O"
'''
def X_finder(board):
    for i in range(len(board)):
        for j in range(len(board)-1):
            if board[i][j]=="X" and board[i][j+1]=="X":
                try:
                    if board[i][j-1]=="_":
                        board[i][j-1]="O"
                        return                     
                except IndexError:
                    if board[i][j+2]=="_":
                        board[i][j+2]="O"
                        return

    for i in range(len(board)-1):
        for j in range(len(board)):
            if board[i][j]=="X" and board[i+1][j]=="X":
                try:
                    if board[i-1][j]=="_":
                        board[i-1][j]="O"
                        return                     
                except IndexError:
                    if board[i+2][j]=="_":
                        board[i+2][j]="O"
                        return


X_finder(board)
for i in board:
 print(i)