class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows = len(board)
        cols = len(board[0])

        #idea is to take the boundary ones which are O's name them as T
        #and identify connecting inner O's through dfs
        #afterwards we change all the inner O's after dfs to X
        #change back the T to O


        def dfs(row,col):

            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != "O":
                return

            board[row][col] = "T"

            dfs(row+1,col)
            dfs(row,col-1)
            dfs(row-1,col)
            dfs(row,col+1)

        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1 and board[i][j] == "O": #border cells
                    dfs(i,j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"