#!/usr/bin/python
import  sys
import  copy

def issafe(board, col, row, n):
    for i in range(n):
        if board[i][col] == 1:
            return False

    for j in range(n):            #Checkin for same row
        if board[row][j] == 1:
            return  False

    for  k in range(col):
        columndifference = col - k
        if row - columndifference >= 0 and board[row - columndifference][k] == 1:
            return  False
        if row + columndifference < n and board[row + columndifference][k] == 1:
            return  False

    return True


def placequeen(board, col, n):
    flag = False
    if col  == n:
        Global.resultboard.append(copy.deepcopy(board))
        return 
        #return  True
    for i in range(n) :
        if issafe(board, col, i, n):
            board[i][col] = 1
            #if placequeen(board, col +1, n):
            placequeen(board, col +1, n)
            board[i][col] = 0
             #   flag = True
            #else :
            #    flag = False
            #    board[i][col] = 0
    #if flag and col == n -1 :
    #    return  True
    #return  False
    return


def nqueens(n):
    board =  [[0 for j in range(n)] for i in range(n)]
    placequeen(board, 0, n)
        #print Global.resultboard
    if Global.resultboard != []:
        for k in range(len(Global.resultboard)):
            print "___________solution: {0}__________________".format(k+1)
            for i in range(n):
                for j in range(n):
                    print Global.resultboard[0][i][j],
                print ""



class Global:
    resultboard = []



if __name__=="__main__":
    n = sys.argv[1]
    result =  nqueens(int(n) )

