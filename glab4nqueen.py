def N_Queen(N):
    def safe(board,row,coll):
        for i in range(coll):
            if board[row][i]==1:
                return False
        for i,j in zip(range(row,-1,-1),range(coll,-1,-1)):
            if board[i][j]==1:
                return False
        for i,j in zip(range(row,N,1),range(coll,-1,-1)):
            if board[i][j]==1:
                    return False
            return True
    def solve(board,coll):
        if coll>=N:
            return True
        for i in range(N):
            if safe(board,i,coll):
                board[i][coll]=1
                if solve(board,coll+1):
                    return True
                board[i][coll]=0
        return False
    board = [[0 for _ in range (N)] for _ in range (N)]
    if solve(board,0):
        for row in board:
            print(' '.join(str(x) for x in row))
    else:
        print("Solution not exit ")
N = 8
N_Queen(N)


